import type { User } from './user'

interface InboxMessage {
  id: string
  message: string
  subject: string
  read: boolean
  user_id: number
  sent_by: User
  workout_id: string
  created: string
}

export type { InboxMessage }