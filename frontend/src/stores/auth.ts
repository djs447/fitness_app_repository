import { computed, ref } from 'vue';
import { defineStore } from 'pinia';

import * as authService from '@/services/authService'

import type { User } from '@/types/user'

export const useAuthStore = defineStore('auth', () => {

  const user = ref<User | null>(null)

  const token = ref<string | null>(
    localStorage.getItem('authToken'),
  )

  const isAuthenticated = computed(() => {
    return user.value !== null && token.value !== null
  })

  async function login(
    username: string,
    password: string,
  ) {
    const response = await authService.login({
      username,
      password,
    })

    token.value = response.token

    localStorage.setItem(
      'authToken',
      response.token
    )

    user.value = await authService.getCurrentUser()
  }

  async function initialize() {
    if (!token.value) {
      return
    }

    try {
      user.value = await authService.getCurrentUser()
    } catch{
      token.value = null
      user.value = null

      localStorage.removeItem('authToken')
    }
  }

  async function logout() {
    try {
      await authService.logout()
    } finally {
      token.value = null
      user.value = null

      localStorage.removeItem('authToken')
    }
  }

  return {
    user,
    token,
    isAuthenticated,
    login,
    initialize,
    logout,
  }
});
