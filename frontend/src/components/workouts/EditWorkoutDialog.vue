<script setup lang="ts">

import { ref } from 'vue'
import type { Workout } from '@/types/workout'
import { useWorkoutStore } from '@/stores/workout'


const props = defineProps<{
    workout: Workout
}>()

const emit = defineEmits<{
    close: []
}>()

const workoutStore = useWorkoutStore()
const editedWorkout = ref({...props.workout })

async function updateWorkout(updatedWorkout: Workout) {
    try{
        await workoutStore.update(updatedWorkout.id, updatedWorkout)
        emit('close')
    } catch (error) {
        console.error('Error updating workout:', error)
    }
}

</script>

<template>

  <div
    class="fixed inset-0 bg-black/50"
    @click="emit('close')"
  ></div>

    <div class="bg-white relative z-10 w-full p-6 rounded-lg shadow-md">
        <h3 class="text-lg font-bold mb-4">Edit Workout</h3>
        <form @submit.prevent="updateWorkout(editedWorkout)">
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="activity_type">
                    Activity Type
                </label>
                <input
                    id="activity_type"
                    v-model="editedWorkout.activity_type"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="text"
                />
            </div>
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="duration">
                    Duration
                </label>
                <input
                    id="duration"
                    v-model="editedWorkout.duration"
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
                    Update Workout
                </button>
            </div>
        </form>
    </div>
</template>

<style scoped>



</style>