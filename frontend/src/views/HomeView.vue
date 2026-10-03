<script setup lang="ts">
import WorkoutList from '../components/workouts/WorkoutList.vue'
import { useWorkoutStore } from '@/stores/workout'

import { onMounted, ref, computed } from 'vue'

const workoutStore = useWorkoutStore();
const error = ref('');
const workouts = computed(() => workoutStore.workouts)
const isLoading = ref(true);

async function fetchWorkouts(){
    error.value = ""

    try{
        isLoading.value = true
        await workoutStore.fetch()
    } catch (err) {
        console.log("error", err)
        error.value = "Error fetching workout data."
    } finally {
        isLoading.value = false
    }
}

onMounted(() => {
  fetchWorkouts();
})
</script>

<template>
  <main>
    <WorkoutList v-if="!isLoading" :workouts="workouts" />
    <LoadingView v-else />
  </main>
</template>

<style>

main {
  height: 100%;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

</style>
