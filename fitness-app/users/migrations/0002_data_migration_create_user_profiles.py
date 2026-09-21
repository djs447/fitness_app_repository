from django.conf import settings
from django.db import migrations


def create_missing_profiles(apps, schema_editor):
    User = apps.get_model(*settings.AUTH_USER_MODEL.split("."))
    Profile = apps.get_model("users", "Profile")

    existing_profile_user_ids = Profile.objects.values_list(
        "user_id",
        flat=True,
    )

    users_without_profiles = User.objects.exclude(
        id__in=existing_profile_user_ids,
    )

    Profile.objects.bulk_create(
        [
            Profile(user_id=user.id, display_name=user.full_name)
            for user in users_without_profiles.iterator()
        ]
    )


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            create_missing_profiles,
            migrations.RunPython.noop,
        ),
    ]