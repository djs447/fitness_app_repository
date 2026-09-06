<script setup lang="ts">

import { ref } from 'vue';
import mock_workout from '@/assets/mockdata/mock_workout1.json';
import mock_comments from '@/assets/mockdata/mock_comments.json';

import type { Comment } from '@/types/comment.ts';
import CommentDialog from '@/components/social/CommentDialog.vue';
import ExerciseList from '@/components/workouts/ExerciseList.vue';
import EquipmentList from '@/components/workouts/EquipmentList.vue';

const comments = ref(mock_comments);
const showCommentDialog = ref(false);

const addComment = (comment: Comment) => {
    comments.value.push(comment)
}
const toggleCommentDialog = () => {
    showCommentDialog.value = !showCommentDialog.value
}

</script>

<template>
    <h3 class="text-2xl font-bold mb-4">{{ mock_workout.name }}</h3>
    <div class="workout-details">
        <div class="workout-time">
            <p>{{ mock_workout.date }}</p>
            <p>{{ mock_workout.time }}</p>
        </div>
        <p>{{ mock_workout.description }}</p>
        <p>Duration: {{ mock_workout.duration }} minutes</p>
        <p>Difficulty: {{ mock_workout.difficulty }}</p>
    </div>
    <EquipmentList :equipment="mock_workout.equipment" />
    <ExerciseList :exercises="mock_workout.exercises" />
    <div class="workout-social">
        <button @click="toggleCommentDialog" class="text-orange-500 hover:text-blue-300 mb-2">View Comments</button>
    </div>
    <CommentDialog v-if="showCommentDialog" :comments="comments" :showCommentDialog="showCommentDialog" @addComment="addComment" @showCommentDialog="toggleCommentDialog"/>
</template>

<style scoped>

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