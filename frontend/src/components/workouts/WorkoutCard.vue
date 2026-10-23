<script setup lang="ts">

import { ref, computed, onMounted } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faPen } from '@fortawesome/free-solid-svg-icons'
import CommentDialog from '@/components/social/CommentDialog.vue'
import EditWorkoutDialog from '@/components/workouts/EditWorkoutDialog.vue'
import WorkoutOptionsMenu from '@/components/workouts/WorkoutOptionsMenu.vue'
import LikeDialog from '@/components/social/LikeDialog.vue'
import type { Comment } from '@/types/comment'
import type { Workout } from '@/types/workout'
import type { Like } from '@/types/user'
import { useWorkoutStore } from '@/stores/workout'
import { useAuthStore } from '@/stores/auth'
import { useCommentStore } from '@/stores/comments'

import { verboseDateTime } from '@/services/format'

const props = defineProps<{
    workout: Workout
}>()

const workoutStore = useWorkoutStore()

const userId = useAuthStore().user?.id

const liked = ref(props.workout.is_liked)
const like_count = ref(props.workout.like_count)
const likes = ref<Array<Like>>([])

const showCommentDialog = ref(false)
const showEditWorkoutDialog = ref(false)
const showEditButton = computed(() => {
    return props.workout?.user?.id === userId
})

const showShareDialog = ref(false)
const showLikeDialog = ref(false)

const toggleCommentDialog = () => {
    showCommentDialog.value = !showCommentDialog.value
}
const toggleShareDialog = () => {
    showShareDialog.value = !showShareDialog.value
}
const toggleLikeDialog = async () => {
    if (showLikeDialog.value) {
        showLikeDialog.value = false
        return
    }
    try{
        await workoutStore.fetchLikes(props.workout.id)
        likes.value = [...workoutStore.likes]
        showLikeDialog.value = true
    } catch (error) {
        console.error('Error fetching likes:', error)
    }
}
const toggleLike = async () => {
    try {
        console.log(liked.value)
        if (liked.value) {
            await workoutStore.unlikeWorkout(props.workout.id)
            liked.value = false
            like_count.value--
        } else {
            await workoutStore.likeWorkout(props.workout.id)
            liked.value = true
            like_count.value++
        }
    } catch (error) {
        console.error('Error toggling like:', error)
    }
}

const toggleEditWorkout = () => {
    showEditWorkoutDialog.value = !showEditWorkoutDialog.value
}

async function deleteWorkout() {
    try {
        await workoutStore.deleteWorkout(props.workout.id)
    } catch (error) {
        console.error('Error deleting workout:', error)
    }
}

</script>

<template>
    <div class="workout-card bg-white p-6 rounded-lg shadow-md">
        <div class="flex items-center justify-between">
            <h3><RouterLink :to="`/workouts/${workout.id}`">{{ workout.title }}</RouterLink></h3>
            <WorkoutOptionsMenu v-if="showEditButton" @edit="toggleEditWorkout" @delete="deleteWorkout" />
        </div>
        <p>{{  verboseDateTime(workout.started_at) }}</p>
        <p>{{ workout.activity_type }}</p>
        <p>Duration: {{ workout?.duration }}</p>
        <p>City: {{ workout.city }}</p>
        <p>County: {{ workout.county }}</p>
        <p>State: {{ workout.state }}</p>
        <div class="workout-social">
            <div>
                <button @click="toggleLike" class="hover:text-blue-300 mb-2">{{ liked ? 'Liked' : 'Like' }}</button>
                <button @click="toggleLikeDialog" class="hover:text-blue-300 mb-2">({{ like_count }})</button>
            </div>
            <button @click="toggleCommentDialog" class="hover:text-blue-300 mb-2">Comment</button>
            <button @click="toggleShareDialog" class="hover:text-blue-300 mb-2">Share</button>
        </div>
    </div>
    <CommentDialog v-if="showCommentDialog" :showCommentDialog="showCommentDialog" :workoutId="workout.id" @showCommentDialog="toggleCommentDialog"/>
    <EditWorkoutDialog v-if="showEditWorkoutDialog" :workout="workout" @close="toggleEditWorkout"/>
    <LikeDialog v-if="showLikeDialog" :showLikeDialog="showLikeDialog" :likes="likes" @showLikeDialog="toggleLikeDialog"/>
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