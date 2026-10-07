import api from '@/services/api'
import type { PaginatedWorkouts, Workout, WorkoutForm } from '@/types/workout'

export async function fetchWorkouts(url: string = '/workouts/'): Promise<PaginatedWorkouts> {
    const response = await api.get<PaginatedWorkouts>(url)
    return response.data
}

export async function getWorkout(workoutID: string | string[] | undefined): Promise<Workout> {
    const response = await api.get<Workout>('/workouts/' + workoutID)

    return response.data
}

export async function updateWorkout(workoutID: string, data: Partial<Workout>): Promise<Workout> {
    const response = await api.patch<Workout>('/workouts/' + workoutID + '/', data,)

    return response.data
}

export async function fetchMyWorkouts(url: string = '/workouts/me/'): Promise<PaginatedWorkouts> {
    const response = await api.get<PaginatedWorkouts>(url)
    return response.data
}

export async function createWorkout(workout: WorkoutForm): Promise<Workout> {
    const payload = {
        ...workout,
        started_at: new Date(workout.started_at).toISOString(),
        duration: String(workout.durationHours * 3600 + workout.durationMinutes * 60 + workout.durationSeconds)
    }
    const response = await api.post<Workout>('/workouts/me/', payload)
    return response.data
}

export async function deleteWorkout(workoutID: string): Promise<void> {
    await api.delete(`/workouts/${workoutID}/`)
}