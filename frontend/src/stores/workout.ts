import { computed, ref } from 'vue';
import { defineStore } from 'pinia';

import * as workoutService from '@/services/workoutService'

import type { Workout, WorkoutForm, PaginatedWorkouts } from '@/types/workout'

export const useWorkoutStore = defineStore('workout', () => {

    const workout = ref<Workout | null>(null)
    const workouts = ref<Array<Workout>>([])
    const my_workouts = ref<Workout[]>([])
    const nextPage = ref<string | null>(null)
    const isLoading = ref(false)
    const hasMore = ref(true)

    async function fetch(){

        try{
            isLoading.value = true
            const response = await workoutService.fetchWorkouts()
            workouts.value = response.results
            nextPage.value = response.next
            hasMore.value = response.next !== null
        } finally {
            isLoading.value = false
        }

    }

    async function get(workoutID: string | string[] | undefined) {
        const response = await workoutService.getWorkout(workoutID)

        workout.value = response
        console.log(response)
    }

    async function update(workoutID:string, data: Partial<Workout>) {
        const response = await workoutService.updateWorkout(workoutID, data)

        const index = my_workouts.value.findIndex((w) => w.id === workoutID)

        if (index !== -1) {
            my_workouts.value[index] = response
        }

        workout.value = response
    }

    async function create(workout: WorkoutForm) {
        const response = await workoutService.createWorkout(workout)
        my_workouts.value.push(response)
        return response
    }

    async function fetchMyWorkouts(){

        try{
            isLoading.value = true
            const response = await workoutService.fetchMyWorkouts()
            my_workouts.value = response.results
            nextPage.value = response.next
            hasMore.value = response.next !== null
        } finally {
            isLoading.value = false
        }
    }

    async function fetchMyNextPage() {
        if (!nextPage.value || isLoading.value) {
            return
        }

        try {
            const response = await workoutService.fetchMyWorkouts(nextPage.value)

            my_workouts.value.push(...response.results)

            nextPage.value = response.next
            hasMore.value = response.next !== null

        } finally{
            //isLoading.value = false
        }
    }

    async function fetchNextPage() {
        if (!nextPage.value || isLoading.value) {
            return
        }

        try {
            const response = await workoutService.fetchWorkouts(nextPage.value)

            workouts.value.push(...response.results)

            nextPage.value = response.next
            hasMore.value = response.next !== null

        } finally{
            //isLoading.value = false
        }
    }


    async function deleteWorkout(workoutID: string) {
        await workoutService.deleteWorkout(workoutID)
        my_workouts.value = workouts.value.filter((w) => w.id !== workoutID)
    }

    async function likeWorkout(workoutID: string) {
        const response = await workoutService.likeWorkout(workoutID)
        const workout = my_workouts.value.find((w) => w.id === workoutID)
        if (workout) {
            workout.is_liked = response.liked
        }
    }

    async function unlikeWorkout(workoutID: string) {
        const response = await workoutService.unlikeWorkout(workoutID)
        const workout = my_workouts.value.find((w) => w.id === workoutID)
        if (workout) {
            workout.is_liked = response.liked
        }
    }

    return{
        workout,
        workouts,
        my_workouts,
        isLoading,
        hasMore,
        fetch,
        get,
        update,
        fetchMyWorkouts,
        create,
        deleteWorkout,
        likeWorkout,
        unlikeWorkout,
        fetchNextPage,
        fetchMyNextPage,
    }
});