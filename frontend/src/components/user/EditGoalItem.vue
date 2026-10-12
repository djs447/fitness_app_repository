<script setup lang="ts">
import { ref } from 'vue'
import type { Goal } from '@/types/profile'
import { useProfileStore } from '@/stores/profile'

const profileStore = useProfileStore()

const props = defineProps<{
    goal: Goal
    mode: 'update' | 'add'
}>()

const editedGoal = ref<Goal>({...props.goal})

const emits = defineEmits<{
    edit: [goalId: string],
    close: []
}>()

async function updateGoal(updatedGoal: Goal) {
    try{
        await profileStore.updateGoal(editedGoal.value.id, updatedGoal)
        emits('edit', props.goal.id)
    } catch (error) {
        console.error('Error updating goal:', error)
    }
}

async function addGoal(newGoal: Goal) {
    try{
        await profileStore.createGoal(newGoal)
        emits('close')
    } catch (error) {
        console.error('Error adding goal:', error)
    }
}
</script>


<template>

    <div class="edit-goal-item">
        <form @submit.prevent="mode === 'update' ? updateGoal(editedGoal) : addGoal(editedGoal)">
            <div class="mb-4 flex flex-col">
                <label for="title">Title:</label>
                <input type="text" id="title" v-model="editedGoal.title" />
            </div>
            <div class="mb-4 flex flex-col">
                <label for="description">Description:</label>
                <textarea id="description" v-model="editedGoal.description"></textarea>
            </div>
            <div class="mb-4 flex flex-col">
                <label for="target_date">Target Date:</label>
                <input type="date" id="target_date" v-model="editedGoal.target_date" />
            </div>
            <div v-if="mode === 'update'" class="mb-4 flex flex-col">
                <label for="completion_date">Completion Date:</label>
                <input type="date" id="completion_date" v-model="editedGoal.completion_date" />
            </div>
            <button
                type="submit"
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            >
                Save Changes
            </button>
            <button 
                type="button"
                @click="mode === 'update' ? emits('edit', props.goal.id) : emits('close')"
                class="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            >
                Cancel
            </button>
        </form>
    </div>
</template>

<style scoped>

input, textarea {
    margin-bottom: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    width: auto;
}
</style>