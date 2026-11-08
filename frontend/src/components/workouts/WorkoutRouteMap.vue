<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from "vue";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import type { WorkoutSample } from "@/types/workout";
import { fetchWorkoutRoute } from "@/services/workoutService";

const props = defineProps<{
  workoutId: string;
}>();

const mapElement = ref<HTMLDivElement | null>(null);
const loading = ref(true);
const error = ref<string | null>(null);
let map: L.Map | undefined;

onMounted(async () => {
  if (!mapElement.value) return;

  try {
    const points: WorkoutSample[] = await fetchWorkoutRoute(props.workoutId);

    // Discard samples without usable GPS coordinates
    const validPoints = points.filter((point) => {
      if (point.latitude == null || point.longitude == null) {
        return false;
      }

      const latitude = Number(point.latitude);
      const longitude = Number(point.longitude);

      return (
        Number.isFinite(latitude) &&
        Number.isFinite(longitude) &&
        latitude >= -90 &&
        longitude >= -180 &&
        longitude <= 180 &&
        latitude <= 90
      );
    });

    if (!validPoints.length) {
      error.value = "No GPS route recorded for this workout";
      loading.value = false;
      return;
    }

    const coordinates: L.LatLngExpression[] = validPoints.map((point) => [
      Number(point.latitude),
      Number(point.longitude),
    ]);

    map = L.map(mapElement.value);

    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: "&copy; OpenStreetMap contributors",
      maxZoom: 19,
    }).addTo(map);

    const route = L.polyline(coordinates, { color: "blue", weight: 4 }).addTo(
      map,
    );

    const start = coordinates[0];
    const finish = coordinates[coordinates.length - 1];

    if (!start || !finish) return;

    L.circleMarker(start, { color: "green", radius: 8, fillOpacity: 1 })
      .bindTooltip("Start")
      .addTo(map);
    L.circleMarker(finish, { radius: 8, color: "red", fillOpacity: 1 })
      .bindTooltip("Finish")
      .addTo(map);

    map.fitBounds(route.getBounds(), {
      padding: [25, 25],
    });
  } catch (err) {
    error.value = (err as Error).message;
    loading.value = false;
  } finally {
    loading.value = false;
  }
});

onBeforeUnmount(() => {
  map?.remove();
});
</script>

<template>
  <div class="workout-route-map">
    <p v-if="loading">Loading route...</p>
    <p v-if="error">{{ error }}</p>
    <div v-else ref="mapElement" class="workout-route-map__canvas" />
  </div>
</template>

<style scoped>
.workout-route-map {
  width: 100%;
  height: 350px;
  border-radius: 12px;
}
.workout-route-map__canvas {
  width: 100%;
  height: 350px;
  border-radius: 12px;
}
</style>
