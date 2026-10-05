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

export type { Workout, WorkoutForm };