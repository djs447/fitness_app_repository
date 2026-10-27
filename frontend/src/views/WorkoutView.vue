<script setup lang="ts">

import { onMounted, ref, computed } from 'vue';
import { useRoute } from 'vue-router';

import CommentDialog from '@/components/social/CommentDialog.vue';
import { useWorkoutStore } from '@/stores/workout';
import WorkoutRouteMap from '@/components/workouts/WorkoutRouteMap.vue'
import { verboseDateTime, formatDuration, formatPace } from '@/services/format.ts';
import ExerciseList from '@/components/workouts/ExerciseList.vue';
import EquipmentList from '@/components/workouts/EquipmentList.vue';


const showCommentDialog = ref(false);
const workoutStore = useWorkoutStore();
const route = useRoute();
const error = ref('');
const workout = computed(() => workoutStore.workout)

const toggleCommentDialog = () => {
    showCommentDialog.value = !showCommentDialog.value
}

async function fetchWorkout(){
    error.value = ""

    try{
        await workoutStore.get(route.params.id)
    } catch (err) {
        console.log("error", err)
        error.value = "Error fetching workout data."
    }
}

onMounted(() => {
    fetchWorkout();
})

</script>

<template>
    <div class="back-container bg-white">
        <RouterLink class="router-link text-black" to="/workouts">← Back</RouterLink>
    </div>
    <div class="workout-container rounded-lg border-l-gray-500">
        <h3 class="text-2xl font-bold mb-4">{{ workout?.title }}</h3>
        <div class="workout-details">
            <div class="workout-time">
                <p>{{ verboseDateTime(workout?.started_at || '') }}</p>
            </div>
            <p>{{ workout?.activity_type ? workout.activity_type[0]?.toUpperCase() + workout.activity_type.slice(1) : '' }}</p>
            <div class="workout-stats">
                <p>Duration: {{ formatDuration(workout?.duration) }}</p>
                <p>Pace: {{ formatPace(workout?.pace, workout?.activity_type) }}</p>
                <p>Average Heart Rate: {{ workout?.heart_rate?.toFixed(0) }}</p>
            </div>
            <p v-if="workout?.difficulty">Difficulty: {{ workout?.difficulty }}</p>
        </div>
        <!-- TODO, add these later <EquipmentList :equipment="mock_workout.equipment" />
        <ExerciseList :exercises="mock_workout.exercises" /> -->
        <WorkoutRouteMap v-if="workout?.id" :workoutId="workout.id || ''" />
        <div class="workout-social">
            <button @click="toggleCommentDialog" class="text-orange-500 hover:text-blue-300 mb-2">View Comments</button>
        </div>
    </div>
    <CommentDialog v-if="showCommentDialog" :workoutId="workout?.id || ''" :showCommentDialog="showCommentDialog" @showCommentDialog="toggleCommentDialog"/>
</template>

<style scoped>

.router-link{
    color: black;
}

.back-container{
    width: 60px;
    margin: 10px 0px 10px 0px;
    border-radius:5%;
}

.workout-container{
    background-color: white;
    padding: 50px;
    width: 70vw;
}

.workout-details {
    margin-bottom: 1rem;
    margin-top: 1rem;
}

.workout-time {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
    align-items: center;
    justify-content: space-between;
}

.workout-stats {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
    align-items: center;
    justify-content: space-between;
}

</style>