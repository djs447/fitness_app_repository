<script setup lang="ts">

import { useAuthStore } from '@/stores/auth';
import { RouterLink, useRouter } from 'vue-router'

const router = useRouter()
const authStore = useAuthStore()

async function logout() {
    await authStore.logout()

    await router.push('/')
}

</script>

<template>
  <div class="flex gap-4 py-5 items-center">
      <nav class="flex p-5 items-center nav-container">
        <div class="nav-button-container">
          <RouterLink class="router-link" to="/home">Home</RouterLink>
          <RouterLink class="router-link" to="/about">About</RouterLink>
          <RouterLink class="router-link" to="/workouts">Workouts</RouterLink>
          <RouterLink class="router-link" to="/profile">Profile</RouterLink>
        </div>
      </nav>
  </div>
</template>

<style scoped>

.router-link {
  padding: 0.5rem 1rem;
  border: 2px solid black;
  border-radius: 6px;
  background-color: #052e16;
  color: white;
  gap: 1rem;
}

.nav-container{
  display: flex;
  justify-content: center;
  margin-left: 100px;
  gap: 1rem;
}

nav {
  font-size: 16px;
  text-align: center;
}

nav a.router-link-exact-active {
  color: black;
  background-color: var(--color-primary);
}

nav a.router-link:hover {
  background-color: transparent;
  color: black;
}

</style>