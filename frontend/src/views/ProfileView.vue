<script setup lang="ts">

import mock_profile from '@/assets/mockdata/mock_profile.json';
import { ref } from 'vue';

const showEditBiographyDialog = ref(false);
const profile = ref(mock_profile);

const newBio = ref("");

const updateBiography = (newBio: string) => {
    profile.value.bio = newBio;
    newBio = "";
    showEditBiographyDialog.value = false;
};

const toggleEditBiographyDialog = () => {
    showEditBiographyDialog.value = !showEditBiographyDialog.value;
};


</script>

<template>
    <div class="profile">
        <h1 class="text-2xl font-bold mb-4">Profile</h1>
        <div class="profile-info">
            <div class="contact-info">
                <p><strong>Name:</strong> {{ profile.name }}</p>
                <p><strong>Email:</strong> {{ profile.email }}</p>
            </div>
            <div class="biography">
                <p><strong>Bio:</strong> {{ profile.bio }}</p>
                <button @click="toggleEditBiographyDialog" class="text-orange-500 hover:text-blue-300 mb-2">Edit Biography</button>
                <div v-if="showEditBiographyDialog" class="edit-biography-dialog">
                    <textarea v-model="newBio" class="w-full p-2 border rounded mb-2"></textarea>
                    <button @click="updateBiography(newBio)" class="text-orange-500 hover:text-blue-300 mb-2">Save</button>
                    <button @click="toggleEditBiographyDialog" class="text-gray-500 hover:text-gray-700 mb-2">Cancel</button>
                </div>
            </div>
            <p><strong>Goals:</strong></p>
            <ul>
                <li v-for="goal in profile.goals" :key="goal">{{ goal }}</li>
            </ul>
        </div>
    </div>
</template>

<style scoped>

.contact-info{
    margin-bottom: 1rem;
}

.profile-info p {
    margin-bottom: 0.5rem;
}

.biography {
    margin-bottom: 1rem;
}

</style>