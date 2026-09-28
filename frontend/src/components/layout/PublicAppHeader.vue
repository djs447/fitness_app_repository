<script setup lang="ts">

import { ref } from 'vue'
import PublicAppNavigation from '@/components/layout/PublicAppNavigation.vue'

</script>

<template>
    <header class="app-header">
        <div class="logo-container">
          <img alt="App logo" class="logo" src="@/assets/logo.png" width="80" height="80" />
        </div>
        <div class="title-container">
          <h1>FITNESS APP</h1>
        </div>
        <PublicAppNavigation class="navigation-bar" />
        <div></div>
    </header>
</template>

<style scoped>

header {
  background-color: var(--header-container-background-color);
  border-bottom: 1px solid var(--header-container-border-color);
  display: flex;
  margin-left: auto;
  margin-right: auto;
  width: 100%;
  justify-content: center;
  position: sticky;
  top: 0;
  z-index: 5;
  line-height: 1.5;
  max-height: 30rem;
  place-items: center;
}

.title-container{
  font-weight: 800;
  margin: auto auto;
}

.navigation-bar{
  justify-content: flex-end;
  padding-right: 16px;
}

.logo {
  margin: 0 2rem 0 0;
  padding-left: 12px;
}

</style>