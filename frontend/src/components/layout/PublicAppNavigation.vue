<script setup lang="ts">

import { RouterLink } from 'vue-router'

</script>

<template>
  <div class="flex gap-4 py-5 items-center">
      <nav class="flex py-5 items-center">
        <RouterLink class="router-link" to="/">Home</RouterLink>
        <RouterLink class="router-link" to="/login">Login</RouterLink>
        <RouterLink class="router-link" to="/register">Register</RouterLink>
      </nav>
  </div>
</template>

<style scoped>

.router-link {
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  background-color: rgba(194, 194, 194, 0.479);
}

nav {
  font-size: 16px;
  text-align: center;
}

nav a.router-link-exact-active {
  color: var(--color-text);
  background-color: var(--color-primary);
}

nav a.router-link:hover {
  background-color: transparent;
}

nav a {
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

</style>