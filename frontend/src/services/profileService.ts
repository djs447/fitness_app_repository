import api from '@/services/api'
import type { Goal, Profile } from '@/types/profile'

export async function fetch(): Promise<Profile> {
    const response = await api.get<Profile>('/users/profiles/me/')

    return response.data
}

export async function update(data: Partial<Profile>): Promise<Profile> {
    const response = await api.patch<Profile>('/users/profiles/me/', data,)

    return response.data
}

export async function updateGoal(goalId: string, data: Partial<Goal>): Promise<Goal> {
    const response = await api.patch<Goal>(`/goals/${goalId}/`, data)

    return response.data
}

export async function createGoal(data: Partial<Goal>): Promise<Goal> {
    const response = await api.post<Goal>('/goals/', data)

    return response.data
}

export async function deleteGoal(goalId: string): Promise<void> {
    await api.delete(`/goals/${goalId}/`)
}
