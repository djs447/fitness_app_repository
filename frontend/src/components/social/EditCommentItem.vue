<script setup lang="ts">
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faBan } from '@fortawesome/free-solid-svg-icons'
import type { Comment } from '@/types/comment'
import { useCommentStore } from '@/stores/comments'

const commentStore = useCommentStore()

const props = defineProps<{
  comment: Comment
}>()

const authStore = useAuthStore()
const editingCommentId = ref<string | null>(null)
const editedContent = ref(props.comment.content)

const emits = defineEmits<{
  edit: [commentId: string]
}>()

async function updateComment(commentId: string, newContent: string) {
  try {
    console.log(props.comment.workout)
    await commentStore.editComment({
      id: commentId,
      content: newContent,
      workout: props.comment.workout
    })
    editingCommentId.value = null
    emits('edit', commentId)
  } catch (error) {
    console.error('Error editing comment:', error)
  }
}

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
        <FontAwesomeIcon v-if="props.comment.user.id === authStore.user?.id" :icon="faBan" @click="emits('edit', props.comment.id)"/>
      </p>
    </div>

    <p class="text-gray-600">
        <form @submit.prevent="updateComment(props.comment.id, editedContent)">
          <input
            v-model="editedContent"
            type="text"
            class="flex-1 rounded border px-3 py-2"
          />
          <button
            type="submit"
            class="rounded bg-green-500 px-4 py-2 text-white hover:bg-green-600"
          >
            Save
          </button>
        </form>
    </p>
  </div>
</template>