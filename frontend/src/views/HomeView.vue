<script setup lang="ts">
import WorkoutList from '../components/workouts/WorkoutList.vue'
import { useWorkoutStore } from '@/stores/workout'

import { onMounted, ref, computed } from 'vue'

const workoutStore = useWorkoutStore();
const error = ref('');
const workouts = computed(() => workoutStore.workouts)

async function fetchWorkouts(){
    error.value = ""

    try{
        await workoutStore.fetch()
    } catch (err) {
        console.log("error", err)
        error.value = "Error fetching profile data."
    }
}

onMounted(() => {
  fetchWorkouts();
})
</script>

<template>
  <main>
    <WorkoutList :workouts=workouts />
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
