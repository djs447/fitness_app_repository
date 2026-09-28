import { computed, ref } from 'vue';
import { defineStore } from 'pinia';

import * as workoutService from '@/services/workoutService'

import type { Workout } from '@/types/workout'

export const useWorkoutStore = defineStore('workout', () => {

    const workout = ref<Workout | null>(null)
    const workouts = ref<Array<Workout> | []>([])

    async function fetch(){
        const response = await workoutService.fetchWorkouts()

        workouts.value = response
    }

    async function get(workoutID: string | string[] | undefined) {
        const response = await workoutService.getWorkout(workoutID)

        workout.value = response
        console.log(response)
    }

    async function update(workoutID:string, data: Partial<Workout>) {
        const response = await workoutService.updateWorkout(workoutID, data)

        workout.value = response
    }

    return{
        workout,
        workouts,
        fetch,
        get,
        update,
    }
});