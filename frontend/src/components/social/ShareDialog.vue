<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'

const props = defineProps<{
    showShareDialog: boolean
    workoutId: string
}>()

const emit = defineEmits<{
    (e: 'showShareDialog'): void
}>()

const toggleShareDialog = () => {
    emit('showShareDialog')
}

const selectedUsers = ref<number[]>([])

const authStore = useAuthStore()

async function getShareableUsers(){
  try{
      await authStore.getShareableUsers(authStore.user?.id as number)
      console.log('Shareable users:', authStore.shareableUsers)
  } catch (error) {
      console.error('Error fetching shareable users:', error)
  }
}

async function shareWithUsers() {
    try {
        console.log('Selected users:', selectedUsers.value)
        await authStore.shareWorkout(props.workoutId, selectedUsers.value)
        toggleShareDialog()
    } catch (error) {
        console.error('Error sharing workout:', error)
    }
}


onMounted(() => {
    getShareableUsers()
})
</script>

<template>

    <div
        v-if="showShareDialog"
        class="fixed inset-0 z-50 flex items-center justify-center"
    >
        <div
            class="absolute inset-0 bg-black/50"
            @click="toggleShareDialog"
        ></div>

        <div class="share-dialog relative z-10 w-full max-w-lg rounded-lg bg-white p-6">
            <h3>Share Workout</h3>
            <form @submit.prevent="shareWithUsers" class="mt-4 gap-2">
                <div class="flex flex-col gap-2">
                <template v-for="user in authStore.shareableUsers" :key="user.id">
                    <label>
                        <input type="checkbox" :value="user.id" v-model="selectedUsers" />
                        {{ user.username }}
                    </label>
                </template>
                </div>
                <div class="w-full flex flex-row justify-end gap-2 mt-4">
                    <button type="submit" class="hover:text-blue-300 mb-2">Share</button>
                    <button @click="toggleShareDialog" class="hover:text-blue-300 mb-2">Close</button>
                </div>
            </form>
        </div>
    </div>
</template>

<style scoped>
.share-dialog {
    width: 35vw;
}

button {
    padding: 0.5rem 1rem;
    border: 1px solid #ccc;
    border-radius: 0.25rem;
    background-color: #f9f9f9;
    cursor: pointer;
}
</style>