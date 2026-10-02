import { computed, ref } from 'vue';
import { defineStore } from 'pinia';

import * as workoutService from '@/services/workoutService'

import type { Workout, CreateWorkout } from '@/types/workout'

export const useWorkoutStore = defineStore('workout', () => {

    const workout = ref<Workout | null>(null)
    const workouts = ref<Array<Workout>>([])
    const my_workouts = ref<Array<Workout>>([])

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

        const index = workouts.value.findIndex((w) => w.id === workoutID)

        if (index !== -1) {
            workouts.value[index] = response
        }

        workout.value = response
    }

    async function create(workout: CreateWorkout) {
        const response = await workoutService.createWorkout(workout)
        workouts.value.push(response)
        return response
    }

    async function fetchMyWorkouts(){
        const response = await workoutService.fetchMyWorkouts()

        my_workouts.value = response
    }

    return{
        workout,
        workouts,
        my_workouts,
        fetch,
        get,
        update,
        fetchMyWorkouts,
        create
    }
});