

<script setup lang="ts">

import type { Workout } from '@/types/workout'
import WorkoutCard from '@/components/workouts/WorkoutCard.vue'
import { ref } from 'vue'

defineProps<{
    workouts: Array<Workout>
}>()

</script>

<template>
    <div class="workout-list">
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