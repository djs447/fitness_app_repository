<script setup lang="ts">

import { useProfileStore } from '@/stores/profile'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faPen, faTrash } from '@fortawesome/free-solid-svg-icons'
import type { Goal } from '@/types/profile'

const profileStore = useProfileStore()

const props = defineProps<{
    goal: Goal
}>()

const emits = defineEmits<{
    edit: [goalId: string]
}>()

async function deleteGoal() {
    try {
        await profileStore.deleteGoal(props.goal.id)
    } catch (error) {
        console.error('Error deleting goal:', error)
    }
}


</script>


<template>

    <div class="goal-info">
        <span class="font-bold">{{ goal.title }}:</span> {{ goal.description }} 
    </div> 
    <div class="goal-target">
        <span class="font-bold">TARGET:</span> {{ goal.target_date }}
    </div> 
    <div class="goal-completed">
        <span class="font-bold">COMPLETED:</span> {{ goal.completion_date }}
    </div>
    <div class="goal-actions">
        <FontAwesomeIcon class="text-gray-500 hover:text-blue-300" :icon="faPen" @click="emits('edit', goal.id)" />
        <FontAwesomeIcon class="text-gray-500 hover:text-blue-300" :icon="faTrash" @click="deleteGoal"/>
    </div>

</template>

<style scoped>

.goal-info{
    min-width: 0;
}

.goal-target,
.goal-completed {
    white-space: nowrap;
    margin-right: 20px;
}

.goal-actions {
    margin-right: 0;
}


</style>
