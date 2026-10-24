from pathlib import Path
import re
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from datetime import timedelta

from fitparse import FitFile

from workouts.models import Workout, WorkoutSample

FITNESS_DATA_DIR = (
    Path(__file__).resolve().parents[3]
    / "media"
    / "fitness_data"
)

def get_value(values, *keys):
    """Return the first available non-None field value."""
    for key in keys:
        value = values.get(key)
        if value is not None:
            return value
    return None

def parse_fit_file(file_path):
    """Convert FIT record messages into WorkoutSample field dictionaries."""
    fit_file = FitFile(str(file_path))

    for record in fit_file.get_messages("record"):
        values = {
            field.name: field.value for field in record
        }

        timestamp = values.get("timestamp")

        if timestamp is None:
            continue

        latitude = values.get("position_lat")
        longitude = values.get("position_long")

        if latitude is not None:
            latitude = latitude * (180 / 2**31)
        if longitude is not None:
            longitude = longitude * (180 / 2**31)

        yield {
            "timestamp": timestamp,
            "heart_rate": values.get("heart_rate"),
            "speed": get_value(values, "enhanced_speed", "speed"),
            "cadence": values.get("cadence"),
            "power": values.get("power"),
            "elevation": get_value(values, "enhanced_altitude", "altitude"),
            "latitude": latitude,
            "longitude": longitude,
        }

def parse_fit_metadata(file_path):
    fit_file = FitFile(str(file_path))

    for session in fit_file.get_messages("session"):
        values = {
            field.name: field.value
            for field in session
        }

        started_at = values.get("start_time")
        duration_seconds = (values.get("total_timer_time") or values.get("total_elapsed_time"))

        if started_at is None or duration_seconds is None:
            raise ValueError(f"Missing start time or duration in {file_path}")

        return {
            "started_at": started_at,
            "duration": timedelta(seconds=duration_seconds),
            "distance": values.get("total_distance"),
            "elevation": values.get("total_ascent"),
            "activity_type": values.get("sport"),
        }

    raise ValueError(f"No session found in {file_path}")

class Command(BaseCommand):
    help = "Import FIT files from media/fitness_data."

    def add_arguments(self, parser):
        parser.add_argument(
            "--directory",
            type=str,
            default=str(FITNESS_DATA_DIR),
            help="Directory containing FIT files to import.",
        )

    def handle(self, *args, **options):
        directory = Path(options["directory"])

        if not directory.is_dir():
            raise CommandError(
                f"FIT directory does not exist: {directory}"
            )

        files = sorted(directory.glob("*.fit"))

        if not files:
            self.stdout.write("No FIT files found.")
            return

        for file_path in files:
            self.import_file(file_path, directory)

    def import_file(self, file_path, data_directory):
        # Creates the Workout and WorkoutSample records from the FIT file.

        source_file = str(file_path.relative_to(data_directory))
        title = file_path.stem.replace("_", " ")

        try:
            metadata = parse_fit_metadata(file_path)

            with transaction.atomic():
                workout, created = Workout.objects.get_or_create(
                    source_file=source_file,
                    defaults={
                        "title": title,
                        "started_at": metadata["started_at"],
                        "duration": metadata["duration"],
                        "distance": metadata["distance"],
                        "elevation": metadata["elevation"],
                        "activity_type": metadata["activity_type"],
                    }
                )

                if not created and workout.samples.exists():
                    self.stdout.write(
                        f"Skipping {file_path.name}: this file has already been imported."
                    )
                    return

                batch_size = 1000
                processed = 0
                batch = []

                for sample_data in parse_fit_file(file_path):
                    batch.append(
                        WorkoutSample(
                            workout=workout,
                            **sample_data,
                        )
                    )
                    if len(batch) >= batch_size:
                        WorkoutSample.objects.bulk_create(batch, ignore_conflicts=True, batch_size=batch_size)
                        processed += len(batch)
                        batch.clear()

                if batch:
                    WorkoutSample.objects.bulk_create(batch, ignore_conflicts=True, batch_size=batch_size)
                    processed += len(batch)

        except Exception as exc:
            self.stderr.write(self.style.ERROR(f"Error importing {file_path.name}: {exc}"))
            return

        action = "Created" if created else "Updated"
        self.stdout.write(
            self.style.SUCCESS(f"{action} workout '{workout.title}' from {file_path.name} with {processed} samples.")
        )
                    