<script setup lang="ts">
import { ref } from 'vue';

const props = defineProps<{
  equipment: string[];
}>();
</script>

<template>
  <div class="equipment-list">
    <h4>Equipment:</h4>
    <ul>
      <li v-for="item in props.equipment" :key="item">
        {{ item }}
      </li>
    </ul>
  </div>
</template>

<style scoped>
.equipment-list {
  margin-top: 1rem;
}
.equipment-list h4 {
  margin-bottom: 0.5rem;
}
.equipment-list ul {
  list-style-type: disc;
  padding-left: 1.5rem;
}
.equipment-list li {
  margin-bottom: 0.25rem;
}
</style>