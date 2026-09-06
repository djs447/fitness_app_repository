<script setup lang="ts">
import TheWelcome from '../components/TheWelcome.vue'
import WorkoutList from '../components/workouts/WorkoutList.vue'
import WorkoutCard from '../components/workouts/WorkoutCard.vue'

import { ref } from 'vue'

defineProps<{
    workouts: Array<{
        id: number
        name: string
        description: string
        duration: number
        difficulty: string
    }>
}>()
</script>

<template>
  <main>
    <WorkoutList :workouts="workouts" />
  </main>
</template>

<style>

main {
  height: 100%;
}

</style>
