import api from '@/services/api'
import type { Profile } from '@/types/profile'

export async function fetch(): Promise<Profile> {
    const response = await api.get<Profile>('/users/profiles/me/')

    return response.data
}