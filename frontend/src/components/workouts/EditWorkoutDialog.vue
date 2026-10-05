<script setup lang="ts">

import { ref } from 'vue'
import type { Workout, WorkoutForm } from '@/types/workout'
import { useWorkoutStore } from '@/stores/workout'
import { formatDateTimeLocal, parseDurationToForm } from '@/services/format'


const props = defineProps<{
    workout: Workout
}>()

const emit = defineEmits<{
    close: []
}>()

const workoutStore = useWorkoutStore()
const editedWorkout = ref(
    {
        ...props.workout,
        started_at: formatDateTimeLocal(props.workout.started_at),
        durationHours: parseDurationToForm(props.workout.duration).hours || 0,
        durationMinutes: parseDurationToForm(props.workout.duration).minutes || 0,
        durationSeconds: parseDurationToForm(props.workout.duration).seconds || 0,
    }
)

async function updateWorkout(updatedWorkout: WorkoutForm) {

    const duration = String(updatedWorkout.durationHours*3600 + updatedWorkout.durationMinutes*60 + updatedWorkout.durationSeconds)
    try{
        const payload = { ...updatedWorkout, started_at: new Date(updatedWorkout.started_at).toISOString(), duration: duration, }
        await workoutStore.update(updatedWorkout.id, payload)
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
                <label class="block text-gray-700 text-sm font-bold mb-2" for="title">
                    Title
                </label>
                <input
                    id="title"
                    v-model="editedWorkout.title"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="text"
                />
            </div>
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="description">
                    Description
                </label>
                <textarea
                    id="description"
                    v-model="editedWorkout.description"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                ></textarea>
            </div>
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="notes">
                    Notes
                </label>
                <textarea
                    id="notes"
                    v-model="editedWorkout.notes"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                ></textarea>
            </div>
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="distance">
                    Distance
                </label>
                <input
                    id="distance"
                    v-model="editedWorkout.distance"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="number"
                />
            </div>
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="elevation">
                    Elevation
                </label>
                <input
                    id="elevation"
                    v-model="editedWorkout.elevation"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="number"
                />
            </div>
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="city">
                    City
                </label>
                <input
                    id="city"
                    v-model="editedWorkout.city"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="text"
                />
            </div>
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="county">
                    County
                </label>
                <input
                    id="county"
                    v-model="editedWorkout.county"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="text"
                />
            </div>
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="state">
                    State
                </label>
                <input
                    id="state"
                    v-model="editedWorkout.state"
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
                    v-model="editedWorkout.started_at"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="datetime-local"
                />
            </div>
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="duration">
                    Duration (Hours)
                </label>
                <input
                    id="durationHours"
                    v-model.number="editedWorkout.durationHours"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="number"
                    min="0"
                />
                <label class="block text-gray-700 text-sm font-bold mb-2" for="duration">
                    Duration (Minutes)
                </label>
                <input
                    id="durationMinutes"
                    v-model.number="editedWorkout.durationMinutes"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="number"
                    min="0"
                    max="59"
                />
                <label class="block text-gray-700 text-sm font-bold mb-2" for="duration">
                    Duration (Seconds)
                </label>
                <input
                    id="durationSeconds"
                    v-model.number="editedWorkout.durationSeconds"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="number"
                    min="0"
                    max="59"
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