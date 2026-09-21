import { computed, ref } from 'vue';
import { defineStore } from 'pinia';

import * as profileService from '@/services/profileService'

import type { Profile } from '@/types/profile'

export const useProfileStore = defineStore('profile', () => {

    const profile = ref<Profile | null>(null)

    async function fetch() {
        const response = await profileService.fetch()

        profile.value = response
        console.log(response)
    }

    return{
        profile,
        fetch,
    }
});