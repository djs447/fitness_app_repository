import * as commentService from '@/services/commentService'
import type { Comment, CommentData } from '@/types/comment'
import { ref } from 'vue'

export const useCommentStore = () => {
  const comments = ref<Comment[]>([])

  const getComments = async (workoutId: string) => {
    const response = await commentService.getComments(workoutId)
    comments.value = response
  }

  const addComment = async (commentData: CommentData) => {
    const newComment = await commentService.addComment(commentData)
    newComment.username = 'Current User' // Replace with actual username if available
    comments.value.push(newComment)
  }

  return {
    comments,
    getComments,
    addComment
  }
}