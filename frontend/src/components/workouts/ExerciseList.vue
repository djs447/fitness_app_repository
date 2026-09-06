<script setup lang="ts">

const props = defineProps<{
    exercises: Array<{
        name: string
        duration: number
        averageHeartRate: number
        instructions: string
    }>
}>()

</script>

<template>
  <div class="exercise-list">
    <h4>Exercises:</h4>
    <ul>
      <li v-for="exercise in exercises" :key="exercise.name">
        {{ exercise.name }} - {{ exercise.duration }} mins
      </li>
    </ul>
  </div>
</template>

<style scoped>
.exercise-list {
  margin-top: 1rem;
}
.exercise-list h4 {
  margin-bottom: 0.5rem;
}
.exercise-list ul {
  list-style-type: disc;
  padding-left: 1.5rem;
}
.exercise-list li {
  margin-bottom: 0.25rem;
}
</style>