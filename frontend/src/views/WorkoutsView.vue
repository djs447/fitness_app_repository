<script setup lang="ts">
import WorkoutList from '@/components/workouts/WorkoutList.vue';
import { ref } from 'vue';
import mock_workouts from '@/assets/mockdata/mock_workouts.json';

const workouts = ref(mock_workouts);

</script>

<template>
    <div class="workout-list-container">
        <h3 class="text-2xl font-bold text-white">My Workouts</h3>
        <WorkoutList :workouts="workouts" />
    </div>
</template>

<style scoped>

.workout-list-container{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 30px;
}

</style>