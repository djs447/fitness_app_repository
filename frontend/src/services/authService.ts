import api from '@/services/api'
import type { User } from '@/types/user'

interface LoginCredentials {
    username: string
    password: string
}

interface LoginResponse {
    token: string
}

interface RegisterData {
    username: string
    email: string
    password: string
}

interface RegisterResponse {
    token: string
    user: User
}

export async function login(
    credentials: LoginCredentials,
): Promise<LoginResponse> {
    const response = await api.post<LoginResponse>('/auth/login/', credentials,)

    return response.data
}

export async function getCurrentUser(): Promise<User> {
    const response = await api.get<User>('/users/me/')

    return response.data
}

export async function logout(): Promise<void> {
    await api.post('/users/logout/')
}