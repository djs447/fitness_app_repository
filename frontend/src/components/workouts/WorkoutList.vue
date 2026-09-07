

<script setup lang="ts">

import mock_workouts from '@/assets/mockdata/mock_workouts.json'

import WorkoutCard from '@/components/workouts/WorkoutCard.vue'
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

const workouts = ref(mock_workouts)

</script>

<template>
    <div class="workout-list bg-amber-100">
        <div class="workout-card">
            <WorkoutCard v-for="workout in workouts" :key="workout.id" :workout="workout" />
        </div>
    </div>
</template>

<style>
.workout-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    height: 100vh;
    width: 100vw;
}

.workout-card {
    margin: 2rem;
}


</style>