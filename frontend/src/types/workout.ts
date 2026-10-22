import type { User } from '@/types/user'

interface Workout {
    id: string,
    title: string,
    description: string,
    notes: string,
    distance: number,
    elevation: number,
    city: string,
    county: string,
    state: string,
    created: string,
    modified: string,
    activity_type: string,
    started_at: string,
    duration: string,
    user: User,
    like_count: number,
    is_liked: boolean,
}

interface WorkoutForm {
    id: string,
    title: string,
    description: string,
    notes: string,
    distance: number,
    elevation: number,
    city: string,
    county: string,
    state: string,
    activity_type: string,
    started_at: string,
    durationHours: number,
    durationMinutes: number,
    durationSeconds: number,
}

interface LikeResponse {
    liked: boolean,
}

interface PaginatedWorkouts {
    results: Array<Workout>,
    next: string | null,
    count: number,
    previous: string | null,
}

export type { Workout, WorkoutForm, PaginatedWorkouts, LikeResponse };