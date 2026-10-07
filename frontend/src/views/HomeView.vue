<script setup lang="ts">
import WorkoutList from '../components/workouts/WorkoutList.vue'
import LoadingView from '@/views/LoadingView.vue'
import { useWorkoutStore } from '@/stores/workout'

import { onMounted, ref, computed, onUnmounted } from 'vue'

const workoutStore = useWorkoutStore();
const error = ref('');
const workouts = computed(() => workoutStore.workouts)
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

async function fetchWorkouts(){
    error.value = ""

    try{
        await workoutStore.fetch()
    } catch (err) {
        console.log("error", err)
        error.value = "Error fetching workout data."
    }
}

onMounted(() => {
  fetchWorkouts();

  setupObserver();
})

onUnmounted(() => {
    observer?.disconnect();
})

</script>

<template>
  <main>
    <WorkoutList v-if="!isLoading" :workouts="workouts" />
    <LoadingView v-else />
  </main>
  <div class="load-more-trigger" ref="loadMoreTrigger" />
</template>

<style>

.load-more-trigger {
    height: 1px;
}

main {
  height: 100%;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

</style>
