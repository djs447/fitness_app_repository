import axios from 'axios'

export const API_BASE_URL = "http://localhost:8000"
export const API_URL = `${API_BASE_URL}/api`

const api = axios.create({
    baseURL: API_URL,
})

api.interceptors.request.use((config) => {
    const token = localStorage.getItem('authToken')

    if (token) {
        config.headers.Authorization = `Token ${token}`
    }

    return config
})

export default api