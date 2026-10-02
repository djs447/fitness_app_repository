<script setup lang="ts">

import { ref } from 'vue'
import type { CreateWorkout } from '@/types/workout'
import { useWorkoutStore } from '@/stores/workout'

const emit = defineEmits<{
    close: []
}>()

const workoutStore = useWorkoutStore()
const workout = ref<CreateWorkout>({ activity_type: '', duration: '', started_at: '' })

async function addWorkout(newWorkout: CreateWorkout) {
    try{
        await workoutStore.create(newWorkout)
        emit('close')
    } catch (error) {
        console.error('Error adding workout:', error)
    }
}

</script>

<template>

  <div
    class="fixed inset-0 bg-black/50"
    @click="emit('close')"
  ></div>

    <div class="bg-white fixed z-10 w-lg p-6 rounded-lg shadow-md">
        <h3 class="text-lg font-bold mb-4">Add Workout</h3>
        <form @submit.prevent="addWorkout(workout)">
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="activity_type">
                    Activity Type
                </label>
                <input
                    id="activity_type"
                    v-model="workout.activity_type"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="text"
                />
            </div>
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="started_at">
                    Started At
                </label>
                <input
                    id="started_at"
                    v-model="workout.started_at"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="datetime-local"
                />
            </div>
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="duration">
                    Duration
                </label>
                <input
                    id="duration"
                    v-model="workout.duration"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="number"
                />
            </div>
            <div class="flex items-center justify-between">
                <button
                    type="button"
                    @click="emit('close')"
                    class="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                >
                    Cancel
                </button>
                <button
                    type="submit"
                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                >
                    Add Workout
                </button>
            </div>
        </form>
    </div>
</template>

<style scoped>



</style>