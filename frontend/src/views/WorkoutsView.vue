<script setup lang="ts">
import WorkoutList from '@/components/workouts/WorkoutList.vue';
import { ref } from 'vue';
import mock_workouts from '@/assets/mockdata/mock_workouts.json';

const workouts = ref(mock_workouts);

</script>

<template>
    <h3 class="text-2xl font-bold mb-4">Workouts</h3>
    <WorkoutList :workouts="workouts" />

</template>