<script setup lang="ts">
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faPen, faTrash } from '@fortawesome/free-solid-svg-icons'
import type { Comment } from '@/types/comment'

const authStore = useAuthStore()

const userCanUpdateComment = () => {
    return authStore.user?.id === props.comment.user.id
}

const props = defineProps<{
  comment: Comment
}>()

const emits = defineEmits<{
    edit: [commentId: string],
    delete: [commentId: string],
    close: []
}>()

</script>

<template>
  <div class="mb-2 pb-1">
    <div class="flex items-center gap-2">
      <p class="font-semibold">
        {{ props.comment.username }}
      </p>
      <p class="text-gray-500 text-sm">
        {{ props.comment.created }}
      </p>
      <p class="text-gray-500 text-sm">
        <FontAwesomeIcon class="hover:text-blue-300" v-if="userCanUpdateComment()" :icon="faPen" @click="emits('edit', props.comment.id)" />
      </p>
      <p class="text-gray-500 text-sm ">
        <FontAwesomeIcon class="hover:text-blue-300"v-if="userCanUpdateComment()" :icon="faTrash" @click="emits('delete', props.comment.id)" />
      </p>
    </div>

    <p class="text-gray-600">
      {{ props.comment.content }}
    </p>
  </div>
</template>