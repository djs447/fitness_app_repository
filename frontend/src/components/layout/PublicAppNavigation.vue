<script setup lang="ts">

import { RouterLink } from 'vue-router'

</script>

<template>
  <div class="flex gap-4 py-5 items-center">
      <nav class="flex py-5 items-center">
        <RouterLink class="router-link" to="/">Home</RouterLink>
        <div class="auth-button-container">
          <RouterLink class="router-link" to="/login">Login</RouterLink>
          <RouterLink class="router-link" to="/register">Register</RouterLink>
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
}

.auth-button-container{
  display: flex;
  width: 100%;
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

nav a {
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}



</style>