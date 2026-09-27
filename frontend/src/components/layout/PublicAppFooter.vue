<script setup lang="ts">

import { ref } from 'vue'

</script>

<template>
    <div class="footer-container">
        <div class="social-media-container">
            <a href="#" class="fa fa-facebook"></a>
            <a href="#" class="fa fa-twitter"></a>
            <a href="#" class="fa fa-instagram"></a>
        </div>
        <div class="footer-links-container">
            <p>Links</p>
        </div>
    </div>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</template>


<style scoped>

.fa {
    color: #052e16;
    font-size: 30px;
    padding: 10px;
}

.footer-container{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    background-color: var(--footer-container-background-color);
    width: 100%;
    padding: 10px;
}

</style>