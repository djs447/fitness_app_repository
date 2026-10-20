<script setup lang="ts">

import { ref, watch } from "vue"
import { uploadProfilePicture } from "@/services/profileService"
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faCamera } from "@fortawesome/free-solid-svg-icons";

const uploading = ref(false)
const error = ref<string | null>(null)
import { API_BASE_URL } from "@/services/api"

function getPictureUrl(profilePicture: string | null): string | undefined {
    if (!profilePicture) return undefined

    if (profilePicture.startsWith("http://") || profilePicture.startsWith("https://")) return profilePicture

    return `${API_BASE_URL}${profilePicture}`
}

const props = defineProps<{
    profilePicture: string | null
}>()

const profilePicture = ref<string | null>(props.profilePicture)

watch(() => props.profilePicture, (newVal) => {
    profilePicture.value = newVal
})

async function handleUpload(event: Event) {
    const input = event.target as HTMLInputElement
    const file = input.files?.[0]
    if (!file) return

    uploading.value = true
    error.value = null
    try {
        const updatedProfile = await uploadProfilePicture(file)
        profilePicture.value = updatedProfile.profile_picture
    } catch (err) {
        error.value = (err as Error).message
    } finally {
        uploading.value = false
        input.value = ""
    }
}

const fileInput = ref<HTMLInputElement | null>(null)

function openFilePicker() {
    fileInput.value?.click()
}
</script>

<template>
    <div class="profile-picture">
        <img
            v-if="profilePicture"
            :src="getPictureUrl(profilePicture)"
            class="profile-picture__image"
            alt="Profile Picture"
        />

        <button
            v-else
            type="button"
            class="profile-picture__placeholder"
            aria-label="Upload profile picture"
            @click="openFilePicker"
        >
            <FontAwesomeIcon :icon="faCamera" size="3x" />
        </button>

        <button
            v-if="profilePicture"
            type="button"
            class="profile-picture__change text-orange-500 hover:text-blue-300"
            @click="openFilePicker"
        >
            Change picture
        </button>

        <input
            ref="fileInput"
            id="profile-picture"
            type="file"
            accept="image/jpeg,image/png"
            :disabled="uploading"
            @change="handleUpload"
            hidden
        />

        <p v-if="uploading">Uploading...</p>
        <p v-if="error" class="profile-picture__error">
            {{ error }}
        </p>
    </div>
</template>

<style scoped>
.profile-picture__placeholder {
    width: 120px;
    height: 120px;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    background: #eee;
    color: #666;
}

.profile-picture__image {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    display: block;
}

.profile-picture__change {
    margin-top: 8px;
    cursor: pointer;
}
</style>