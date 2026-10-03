import { computed, ref } from 'vue';
import { defineStore } from 'pinia';

import * as profileService from '@/services/profileService'

import type { Profile, Goal } from '@/types/profile'

export const useProfileStore = defineStore('profile', () => {

    const profile = ref<Profile | null>(null)

    async function fetch() {
        const response = await profileService.fetch()

        profile.value = response
        console.log(response)
    }

    async function update(data: Partial<Profile>) {
        const response = await profileService.update(data)

        profile.value = response
    }

    async function updateGoal(goalId: string, data: Partial<Goal>) {
        const response = await profileService.updateGoal(goalId, data)

        if (profile.value) {
            const goalIndex = profile.value.goals.findIndex((g) => g.id === goalId)
            if (goalIndex !== -1) {
                profile.value.goals[goalIndex] = response
            }
        }
    }

    async function createGoal(data: Partial<Goal>) {
        const response = await profileService.createGoal(data)

        if (profile.value) {
            profile.value.goals.push(response)
        }
    }

    async function deleteGoal(goalId: string) {
        const response = await profileService.deleteGoal(goalId)

        if (profile.value) {
            profile.value.goals = profile.value.goals.filter((g) => g.id !== goalId)
        }
    }

    return{
        profile,
        fetch,
        update,
        updateGoal,
        createGoal,
        deleteGoal,
    }
});