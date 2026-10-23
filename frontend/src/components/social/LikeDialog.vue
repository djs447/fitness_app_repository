<script setup lang="ts">
import type { Like } from '@/types/user'

defineProps<{
    showLikeDialog: boolean
    likes: Like[]
}>()
</script>

<template>
    <div v-if="showLikeDialog" class="like-dialog bg-white p-6 rounded-lg shadow-md">
        <h3 class="text-lg font-bold mb-4">Likes for {{ likes[0]?.workout.title }}</h3>
        <ul>
            <li v-if="likes.length === 0">No likes yet.</li>
            <li v-for="like in likes" :key="like.user.id">
                {{ like.user.username }}
            </li>
        </ul>
        <button class="mt-4 px-4 py-2 bg-red-500 text-white rounded" @click="$emit('showLikeDialog')">Close</button>
    </div>
</template>
