<script setup lang="ts">

import { ref, computed } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faPen } from '@fortawesome/free-solid-svg-icons'
import CommentDialog from '@/components/social/CommentDialog.vue'
import EditWorkoutDialog from '@/components/workouts/EditWorkoutDialog.vue'
import type { Comment } from '@/types/comment'
import type { Workout } from '@/types/workout'
import { useAuthStore } from '@/stores/auth'

import mock_comments from '@/assets/mockdata/mock_comments.json'


const props = defineProps<{
    workout: Workout
}>()

const userId = useAuthStore().user?.id

const liked = ref(false)
const likes = ref(0)

const newComment = ref('')
const comments = ref(mock_comments)
const showCommentDialog = ref(false)
const showEditWorkoutDialog = ref(false)
const showEditButton = computed(() => {
    console.log(props.workout)
    return props.workout?.user?.id === userId
})

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
const toggleEditWorkout = () => {
    showEditWorkoutDialog.value = !showEditWorkoutDialog.value
}

</script>

<template>
    <div class="workout-card bg-white p-6 rounded-lg shadow-md">
        <div class="flex items-center justify-between">
            <h3><RouterLink :to="`/workouts/${workout.id}`">{{ workout.id }}</RouterLink></h3>
            <FontAwesomeIcon v-if="showEditButton" class="text-gray-500 hover:text-blue-300" @click="toggleEditWorkout" :icon="faPen" />
        </div>
        <p>{{  workout.started_at}}</p>
        <p>{{ workout.activity_type }}</p>
        <p>Duration: {{ workout.duration }} minutes</p>
        <div class="workout-social">
            <button @click="toggleLike" class="hover:text-blue-300 mb-2">{{ liked ? 'Liked' : 'Like' }}</button>
            <button @click="toggleCommentDialog" class="hover:text-blue-300 mb-2">Comment</button>
            <button @click="toggleShareDialog" class="hover:text-blue-300 mb-2">Share</button>
        </div>
    </div>
    <CommentDialog v-if="showCommentDialog" :comments="comments" :showCommentDialog="showCommentDialog" @addComment="addComment" @showCommentDialog="toggleCommentDialog"/>
    <EditWorkoutDialog v-if="showEditWorkoutDialog" :workout="workout" @close="toggleEditWorkout"/>
</template>

<style scoped>

.workout-card {
    width: 35vw;
}

.workout-social {
    display: flex;
    justify-content: space-between;
    margin-top: 1rem;
    color: #052e16;
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