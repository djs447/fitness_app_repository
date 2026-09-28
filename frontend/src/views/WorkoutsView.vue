<script setup lang="ts">
import WorkoutList from '@/components/workouts/WorkoutList.vue';
import { onMounted, ref, computed } from 'vue'
import type { Workout } from '@/types/workout'
import { useWorkoutStore } from '@/stores/workout';

const workoutStore = useWorkoutStore();
const error = ref('');
const workouts = computed(() => workoutStore.my_workouts)

async function fetchMyWorkouts(){
    error.value = ""

    try{
        await workoutStore.fetchMyWorkouts()
    } catch (err) {
        console.log("error", err)
        error.value = "Error fetching my workout data."
    }
}

onMounted(() => {
  fetchMyWorkouts();
})

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