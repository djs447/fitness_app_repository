<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useCommentStore } from '@/stores/comments'
import { useAuthStore } from '@/stores/auth'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faPen } from '@fortawesome/free-solid-svg-icons'
import CommentItem from '@/components/social/CommentItem.vue'
import EditCommentItem from '@/components/social/EditCommentItem.vue'

const commentStore = useCommentStore()
const authStore = useAuthStore()

const toggleCommentDialog = () => {
  emit('showCommentDialog', !showComments.value)
}

const showComments = ref(false)
const newComment = ref('')
const comments = computed(() => commentStore.comments ?? [])
const editingCommentId = ref<string | null>(null)

const props = defineProps<{
  workoutId: string,
  showCommentDialog: boolean,
}>()

const emit = defineEmits<{
  showCommentDialog: [show: boolean]
}>()

async function addComment(){
  try{
      console.log(props.workoutId)
      await commentStore.addComment({ workout: props.workoutId, content: newComment.value })
      newComment.value = ''
  } catch (error) {
      console.error('Error adding comment:', error)
  }
}

async function getComments(){
  try{
      await commentStore.getComments(props.workoutId)
  } catch (error) {
      console.error('Error fetching comments:', error)
  }
}

async function toggleEditComment(commentId: string) {
  editingCommentId.value = editingCommentId.value === commentId ? null : commentId;
  console.log(`Toggling edit mode for comment ${commentId}`)
}

async function deleteComment(commentId: string) {
  try {
    await commentStore.deleteComment(commentId)
  } catch (error) {
    console.error('Error deleting comment:', error)
  }
}

onMounted(() => {
  getComments()
})

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
        v-for="comment in comments.value"
        :key="comment.id"
        class="mb-4 border-b pb-3"
      >

        <CommentItem v-if="editingCommentId !== comment.id" :comment="comment" @edit="toggleEditComment" @delete="deleteComment"/>
        <EditCommentItem v-else :comment="comment" @edit="toggleEditComment" />

      </div>

      <p
        v-if="comments.value.length === 0"
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
