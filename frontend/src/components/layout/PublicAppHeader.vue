<script setup lang="ts">

import { ref } from 'vue'
import PublicAppNavigation from '@/components/layout/PublicAppNavigation.vue'

</script>

<template>
    <header class="app-header bg-amber-100">
        <div></div>
        <div class="logo-container">
        <img alt="App logo" class="logo" src="@/assets/logo.png" width="50" height="50" />
        </div>
        <PublicAppNavigation />
        <div></div>
    </header>
</template>

<style scoped>

header {
  line-height: 1.5;
  height: 20%;
  max-height: 100vh;
  display: flex;
  place-items: center;
  justify-content: center;
  width: 100vw;
}

.logo {
  margin: 0 2rem 0 0;
}

</style>