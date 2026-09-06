<script setup lang="ts">

import { ref } from 'vue'
import AppNavigation from '@/components/layout/AppNavigation.vue'

</script>

<template>
    <header class="app-header">
        <div class="logo-container">
        <img alt="App logo" class="logo" src="@/assets/logo.png" width="50" height="50" />
        </div>
        <AppNavigation />
    </header>
</template>

<style scoped>

header {
  line-height: 1.5;
  height: 20%;
  max-height: 100vh;
  display: flex;
  place-items: center;
}

header .wrapper {
  display: flex;
  place-items: flex-start;
  flex-wrap: wrap;
}

.logo {
  margin: 0 2rem 0 0;
}

</style>