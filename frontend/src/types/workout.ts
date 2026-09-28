import type { User } from '@/types/user'

interface Workout {
    id: string,
    created: string,
    modified: string,
    activity_type: string,
    started_at: string,
    duration: string,
    user: User,
}

export type { Workout };