<script setup lang="ts">

import { ref, onMounted, computed } from 'vue';

import { useProfileStore } from '@/stores/profile';
import ProfilePicture from '@/components/user/profilePicture.vue';
import LoadingView from './LoadingView.vue';
import GoalItem from '@/components/user/GoalItem.vue';
import EditGoalItem from '@/components/user/EditGoalItem.vue';
import type { Goal } from '@/types/profile'

const profileStore = useProfileStore()
const error = ref("")
const isLoading = ref(true)

async function fetchProfile(){
    error.value = ""

    try{
        isLoading.value = true
        await profileStore.fetch()
    } catch (err) {
        console.log("error", err)
        error.value = "Error fetching profile data."
    } finally {
        isLoading.value = false
    }
}

const showEditBiographyDialog = ref(false);
const editingGoalId = ref<string | null>(null);
const showAddGoalDialog = ref(false);
const addGoal = ref<Goal>({ 'id': '', 'title': '', 'description': '', 'target_date': new Date(), 'completion_date': new Date() });
const profile = computed(() => profileStore.profile)
const newBio = ref("");

async function updateBiography(){

    console.log(newBio.value)

    try{
        await profileStore.update({
            bio: newBio.value
        })

        newBio.value = ''
        showEditBiographyDialog.value = false
    } catch (err){
        console.error("Error updating biography:", err)

    }
}

const toggleEditBiographyDialog = () => {
    showEditBiographyDialog.value = !showEditBiographyDialog.value;
};

const toggleEditGoalItem = (goalId: string) => {
    editingGoalId.value = editingGoalId.value === goalId ? null : goalId;
};

const toggleAddGoalDialog = () => {
    showAddGoalDialog.value = !showAddGoalDialog.value;
};

onMounted(() => {
    fetchProfile()
})


</script>

<template>
    <div v-if="!isLoading" class="profile-container rounded-2xl">
        <h1 class="text-2xl font-bold mb-4 text-center">Profile</h1>
        <div class="profile-info">
            <ProfilePicture :profile-picture="profile?.profile_picture ?? null"/> <!--Add default prof picture -->
            <div class="contact-info">
                <p><strong>Name:</strong> {{ profile?.display_name }}</p>
            </div>
            <div class="biography">
                <p><strong>Bio:</strong> {{ profile?.bio }}</p>
                <button @click="toggleEditBiographyDialog" class="text-orange-500 hover:text-blue-300 mb-2">Edit Biography</button>
                <div v-if="showEditBiographyDialog" class="edit-biography-dialog">
                    <textarea v-model="newBio" class="w-full p-2 border rounded mb-2"></textarea>
                    <button @click="updateBiography()" class="text-orange-500 hover:text-blue-300 mb-2">Save</button>
                    <button @click="toggleEditBiographyDialog" class="text-gray-500 hover:text-gray-700 mb-2">Cancel</button>
                </div>
            </div>
            <p><strong>Goals:</strong></p>
            <ul class="goals-container">
                <li v-for="goal in profile?.goals" :key="goal.id" class="goal" :class="{'editing-goal': editingGoalId === goal.id}">
                    <GoalItem v-if="editingGoalId !== goal.id" :goal="goal" @edit="toggleEditGoalItem" />
                    <EditGoalItem v-else mode="update" :goal="goal" @edit="toggleEditGoalItem"/>
                </li>
            </ul>
            <EditGoalItem v-if="showAddGoalDialog" mode="add" :goal="addGoal" @close="toggleAddGoalDialog" />
            <button v-if="!showAddGoalDialog" @click="toggleAddGoalDialog" class="text-orange-500 hover:text-blue-300 mb-2">Add Goal</button>
        </div>
    </div>
    <LoadingView v-else />
</template>

<style scoped>

.goals-container{
    list-style: none;
    padding: 0;
}

.goal{
    display: grid;
    grid-template-columns: 1fr auto auto auto auto;
    align-items: center;
    gap: 2rem;
    padding: 1rem 0;
}

.editing-goal{
    display: block;
}

.profile-container{
    background-color: white;
    padding: 50px;
    width: 70vw;
    margin-top: 20%;
    margin-bottom: 30%;
}

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