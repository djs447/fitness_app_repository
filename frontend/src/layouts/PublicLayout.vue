<script setup lang="ts">

import { ref } from 'vue';
import PublicAppHeader from '@/components/layout/PublicAppHeader.vue';
import PublicAppFooter from '@/components/layout/PublicAppFooter.vue';

</script>

<template>
    <PublicAppHeader />
    <main>
        <RouterView />
    </main>
    <PublicAppFooter />
</template>