<script setup lang="ts">

import { RouterLink } from 'vue-router'

</script>

<template>
  <div class="flex gap-4 py-5 items-center">
      <nav class="flex py-5 items-center">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/workouts">Workouts</RouterLink>
        <RouterLink to="/profile/1">Profile</RouterLink>
      </nav>
  </div>
</template>

<style scoped>

nav {
  font-size: 12px;
  text-align: center;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
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