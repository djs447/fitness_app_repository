<script setup lang="ts">

import { onMounted, ref, computed } from 'vue';
import { useRoute } from 'vue-router';
import mock_comments from '@/assets/mockdata/mock_comments.json';

import type { Comment } from '@/types/comment.ts';
import CommentDialog from '@/components/social/CommentDialog.vue';
import { useWorkoutStore } from '@/stores/workout';
import ExerciseList from '@/components/workouts/ExerciseList.vue';
import EquipmentList from '@/components/workouts/EquipmentList.vue';
import type { Workout } from '@/types/workout';
import WorkoutsView from './WorkoutsView.vue';
import { fetchWorkouts } from '@/services/workoutService';

const comments = ref(mock_comments);
const showCommentDialog = ref(false);
const workoutStore = useWorkoutStore();
const route = useRoute();
const error = ref('');
const workout = computed(() => workoutStore.workout)

const addComment = (comment: Comment) => {
    comments.value.push(comment)
}
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
        <h3 class="text-2xl font-bold mb-4">{{ workout?.id }}</h3>
        <div class="workout-details">
            <div class="workout-time">
                <p>{{ workout?.started_at }}</p>
                <p>{{ workout?.duration }}</p>
            </div>
            <p>{{ workout?.activity_type }}</p>
            <p>Duration: {{ workout?.duration }} minutes</p>
            <p>Difficulty: Hard! </p>
        </div>
        <!-- TODO, add these later <EquipmentList :equipment="mock_workout.equipment" />
        <ExerciseList :exercises="mock_workout.exercises" /> -->
        <div class="workout-social">
            <button @click="toggleCommentDialog" class="text-orange-500 hover:text-blue-300 mb-2">View Comments</button>
        </div>
    </div>
    <CommentDialog v-if="showCommentDialog" :comments="comments" :showCommentDialog="showCommentDialog" @addComment="addComment" @showCommentDialog="toggleCommentDialog"/>
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

</style>