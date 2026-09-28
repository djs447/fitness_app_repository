<script setup lang="ts">

import AppNavigation from '@/components/layout/AppNavigation.vue'

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
    <header class="app-header">
        <div class="logo-container pl-5">
          <img alt="App logo" class="logo" src="@/assets/logo.png" width="80" height="80" />
        </div>
        <AppNavigation class="navigation-bar"/>
        <div class="logout-container">
          <button class="router-link" @click="logout">
            Logout
          </button>
        </div>
    </header>
</template>

<style scoped>

.app-header {
  background-color: var(--header-container-background-color);
  border-bottom: 1px solid var(--header-container-border-color);

  width: 100%;
  min-height: 80px;

  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  
  position: sticky;
  top: 0;
  z-index: 5;
}

.router-link {
  padding: 0.5rem 1rem;
  border: 2px solid black;
  border-radius: 6px;
  background-color: #052e16;
  color: white;
  transition: all 0.4s ease;
}

.navigation-bar{
  justify-content: center;
}

.logout-container{
  justify-self: end;
  padding-right: 20px;
}

.logo {
  margin: 0 2rem 0 0;
  padding-left: 12px;
  display: block;
}

.router-link-exact-active {
  color: black;
  background-color: var(--color-primary);
}

.router-link:hover {
  background-color: transparent;
  color: black;
  transition: all 0.4s ease;
}

</style>