<script setup lang="ts">
import WorkoutList from '@/components/workouts/WorkoutList.vue';
import AddWorkoutDialog from '@/components/workouts/AddWorkoutDialog.vue';
import LoadingView from '@/views/LoadingView.vue';
import { onMounted, onUnmounted, ref, computed, nextTick } from 'vue'
import { useWorkoutStore } from '@/stores/workout';

const workoutStore = useWorkoutStore();
const error = ref('');
const workouts = computed(() => workoutStore.my_workouts ?? [])
const showAddWorkoutDialog = ref(false);
const isLoading = computed(() => workoutStore.isLoading)
const loadMoreTrigger = ref<HTMLElement | null>(null);
const hasMore = computed(() => workoutStore.hasMore)
let observer: IntersectionObserver | null = null;

function setupObserver() {
    observer = new IntersectionObserver(
        async (entries) => {
            const entry = entries[0]
            if (!entry?.isIntersecting || isLoading.value || !hasMore.value){
                return
            }

            await workoutStore.fetchNextPage()
            console.log('Loading more workouts...')
        },
        {
            rootMargin: '0px 0px 10px 0px',
        }
    )
    if (loadMoreTrigger.value) {
        observer.observe(loadMoreTrigger.value);
    }
}

onMounted(async () =>{
    await fetchMyWorkouts();

    setupObserver();
})

onUnmounted(() => {
    observer?.disconnect();
})

const toggleAddWorkoutDialog = () => {
    showAddWorkoutDialog.value = !showAddWorkoutDialog.value;
};

async function fetchMyWorkouts(){
    error.value = ""

    try{
        await workoutStore.fetchMyWorkouts()
    } catch (err) {
        console.log("error", err)
        error.value = "Error fetching my workout data."
    }
}

</script>

<template>
    <div class="workout-banner">
        <h3 class="text-2xl font-bold text-white">My Workouts</h3>
        <button
            @click="toggleAddWorkoutDialog"
            class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        >
            Add Workout
        </button>
    </div>
    <div class="workout-list-container">
        <AddWorkoutDialog
            v-if="showAddWorkoutDialog"
            @close="toggleAddWorkoutDialog"
        />
        <WorkoutList v-if="!isLoading" :workouts="workouts" />
        <LoadingView v-if="isLoading" />
    </div>
    
    <div class="load-more-trigger" ref="loadMoreTrigger"></div>
</template>

<style scoped>

.load-more-trigger {
    height: 1px;
}

.workout-banner{
    margin: 0;
    display: flex;
    flex-direction: column;
    margin: 20px auto;
    width: 200px;
    align-items: center;
}

.workout-list-container{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 30px;
}

</style>