<script setup lang="ts">

import { ref } from 'vue';
import PublicAppHeader from '@/components/layout/PublicAppHeader.vue';
// import WorkoutList from '@/components/workouts/WorkoutList.vue';
// import mock_workouts from '@/assets/mockdata/mock_workouts.json';

</script>

<template>
    <PublicAppHeader />
    <main>
        <RouterView />
    </main>
</template>