<script setup lang="ts">
import type { Like } from '@/types/user'

defineProps<{
    showLikeDialog: boolean
    likes: Like[]
}>()
</script>

<template>

    <div
        v-if="showLikeDialog"
        class="fixed inset-0 z-50 flex items-center justify-center"
    >
        <div
            class="absolute inset-0 bg-black/50"
            @click="$emit('showLikeDialog', false)"
        ></div>
        <div class="relative z-10 w-full max-w-lg rounded-lg bg-white p-6">
            <h3 class="text-lg font-bold mb-4">Likes for {{ likes[0]?.workout.title }}</h3>
            <ul>
                <li v-if="likes.length === 0">No likes yet.</li>
                <li v-for="like in likes" :key="like.user.id">
                    {{ like.user.username }}
                </li>
            </ul>
            <button class="mt-4 px-4 py-2 bg-red-500 text-white rounded" @click="$emit('showLikeDialog', false)">Close</button>
        </div>
    </div>
</template>
