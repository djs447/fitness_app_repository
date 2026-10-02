import api from '@/services/api'
import type { Workout, CreateWorkout } from '@/types/workout'

export async function fetchWorkouts(): Promise<Array<Workout>> {
    const response = await api.get<Array<Workout>>('/workouts/')
    console.log(response.data)
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

export async function fetchMyWorkouts(): Promise<Array<Workout>> {
    const response = await api.get<Array<Workout>>('/workouts/me/')
    console.log(response.data)
    return response.data
}

export async function createWorkout(workout: CreateWorkout): Promise<Workout> {
    const payload = {
        ...workout,
        started_at: new Date(workout.started_at).toISOString()
    }
    const response = await api.post<Workout>('/workouts/', payload)
    return response.data
}