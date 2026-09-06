<script setup lang="ts">
import { ref } from 'vue'

const toggleCommentDialog = () => {
  emit('showCommentDialog', !showComments.value)
}

const showComments = ref(false)
const newComment = ref('')

defineProps<{
  comments: Array<{
    id: number,
    author: string,
    text: string,
    workoutId: number,
  }>

  showCommentDialog: boolean,

}>()

const emit = defineEmits<{
    addComment: [comment: { id: number, author: string, text: string, workoutId: number }]
    showCommentDialog: [show: boolean]
}>()

function addComment(){
    /*
    TODO Update author
    */
    if (newComment.value.trim() !== '') {
        emit('addComment', { id: Date.now(), author: 'User', text: newComment.value, workoutId: 1 })
        newComment.value = ''
    }
}

</script>

<template>

<div
  v-if="showCommentDialog"
  class="fixed inset-0 z-50 flex items-center justify-center"
>
  <div
    class="absolute inset-0 bg-black/50"
    @click="toggleCommentDialog"
  ></div>

  <div
    class="relative z-10 w-full max-w-lg rounded-lg bg-white p-6 shadow-xl"
  >
    <div class="mb-4 flex items-center justify-between">
      <h2 class="text-xl font-bold">
        Comments
      </h2>

      <button
        @click="toggleCommentDialog"
        class="text-gray-500 hover:text-gray-800"
      >
        ✕
      </button>
    </div>

    <div class="max-h-80 overflow-y-auto">
      <div
        v-for="comment in comments"
        :key="comment.id"
        class="mb-4 border-b pb-3"
      >
        <p class="font-semibold">
          {{ comment.author }}
        </p>

        <p class="text-gray-600">
          {{ comment.text }}
        </p>
      </div>

      <p
        v-if="comments.length === 0"
        class="text-gray-500"
      >
        No comments yet.
      </p>
    </div>

    <form
      @submit.prevent="addComment"
      class="mt-4 flex gap-2"
    >
      <input
        v-model="newComment"
        type="text"
        placeholder="Add a comment..."
        class="flex-1 rounded border px-3 py-2"
      />

      <button
        type="submit"
        class="rounded bg-orange-500 px-4 py-2 text-white hover:bg-orange-600"
      >
        Post
      </button>
    </form>
  </div>
</div>

</template>
