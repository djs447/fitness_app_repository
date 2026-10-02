<script setup lang="ts">
import WorkoutList from '@/components/workouts/WorkoutList.vue';
import AddWorkoutDialog from '@/components/workouts/AddWorkoutDialog.vue';
import { onMounted, ref, computed } from 'vue'
import type { Workout } from '@/types/workout'
import { useWorkoutStore } from '@/stores/workout';

const workoutStore = useWorkoutStore();
const error = ref('');
const workouts = computed(() => workoutStore.my_workouts)
const showAddWorkoutDialog = ref(false);

const toggleAddWorkoutDialog = () => {
    showAddWorkoutDialog.value = !showAddWorkoutDialog.value;
};

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
        <button
            @click="toggleAddWorkoutDialog"
            class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        >
            Add Workout
        </button>
        <WorkoutList :workouts="workouts" />
        <AddWorkoutDialog
            v-if="showAddWorkoutDialog"
            @close="toggleAddWorkoutDialog"
        />
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