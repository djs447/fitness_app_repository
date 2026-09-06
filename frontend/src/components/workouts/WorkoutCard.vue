<script setup lang="ts">

import { ref } from 'vue'
import CommentDialog from '@/components/social/CommentDialog.vue'
import type { Comment } from '@/types/comment'

import mock_comments from '@/assets/mockdata/mock_comments.json'


defineProps<{
    workout: {
        id: number
        name: string
        date: string
        time: string
        description: string
        duration: number
        difficulty: string
    }
}>()

const liked = ref(false)
const likes = ref(0)

const newComment = ref('')
const comments = ref(mock_comments)
const showCommentDialog = ref(false)

const showShareDialog = ref(false)

const toggleCommentDialog = () => {
    showCommentDialog.value = !showCommentDialog.value
}
const toggleShareDialog = () => {
    showShareDialog.value = !showShareDialog.value
}
const toggleLike = () => {
    liked.value = !liked.value
}

const addComment = (comment: Comment) => {
    comments.value.push(comment)
}

</script>

<template>
    <div class="workout-card bg-gray-100 p-6 rounded-lg shadow-md">
        <h3><RouterLink :to="`/workouts/${workout.id}`">{{ workout.name }}</RouterLink></h3>
        <p>{{  workout.date}} {{ workout.time }}</p>
        <p>{{ workout.description }}</p>
        <p>Duration: {{ workout.duration }} minutes</p>
        <p>Difficulty: {{ workout.difficulty }}</p>
        <div class="workout-social">
            <button @click="toggleLike" class="text-orange-500 hover:text-blue-300 mb-2">{{ liked ? 'Liked' : 'Like' }}</button>
            <button @click="toggleCommentDialog" class="text-orange-500 hover:text-blue-300 mb-2">Comment</button>
            <button @click="toggleShareDialog" class="text-orange-500 hover:text-blue-300 mb-2">Share</button>
        </div>
    </div>
    <CommentDialog v-if="showCommentDialog" :comments="comments" :showCommentDialog="showCommentDialog" @addComment="addComment" @showCommentDialog="toggleCommentDialog"/>
</template>

<style scoped>

.workout-social {
    display: flex;
    justify-content: space-between;
    margin-top: 1rem;
}

button {
    padding: 0.5rem 1rem;
    border: 1px solid var(--color-border);
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    border-color: var(--color-border-hover);
}

</style>