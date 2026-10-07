import api from '@/services/api'
import type { Comment, CommentData } from '@/types/comment'

export async function getComments(workoutId: string): Promise<Comment[]> {
  const response = await api.get(`/workouts/${workoutId}/comments/`);
  for (const comment of response.data) {
    comment.username = comment.user.username; // Assuming the API returns a user object
  }
  return response.data;
}

export async function addComment(commentData: CommentData): Promise<Comment> {
  const response = await api.post(`/workouts/${commentData.workout}/comments/`, { workout: commentData.workout, content: commentData.content });
  return response.data;
}
