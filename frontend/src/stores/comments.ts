import * as commentService from '@/services/commentService'
import { formatCommentDateTimeLocal } from '@/services/format'
import type { Comment, CommentData, EditCommentData } from '@/types/comment'
import { ref } from 'vue'

export const useCommentStore = () => {
  const comments = ref<Comment[]>([])

  const getComments = async (workoutId: string) => {
    const response = await commentService.getComments(workoutId)
    for (const comment of response) {
      comment.created = formatCommentDateTimeLocal(comment.created)
    }
    comments.value = response
  }

  const addComment = async (commentData: CommentData) => {
    const newComment = await commentService.addComment(commentData)
    newComment.username = newComment.user.username
    newComment.created = formatCommentDateTimeLocal(newComment.created)
    comments.value.push(newComment)
  }

  const deleteComment = async (commentId: string) => {
    await commentService.deleteComment(commentId)
    comments.value = comments.value.filter(comment => comment.id !== commentId)
  }

  const editComment = async (commentData: EditCommentData) => {
    const updatedComment = await commentService.editComment(commentData)
    comments.value = comments.value.map(comment => comment.id === commentData.id ? updatedComment : comment)
  }

  return {
    comments,
    getComments,
    addComment,
    deleteComment,
    editComment
  }
}