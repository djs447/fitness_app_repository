<script setup lang="ts">

import { ref } from 'vue';

const email = ref('');
const password = ref('');

const handleLogin = () => {
    // Handle login logic here
    console.log('Email:', email.value);
    console.log('Password:', password.value);
    // You can add your authentication logic here, such as making an API call to validate the credentials.
};

</script>

<template>
    <div class="login-container">
        <h1>Login</h1>
        <form @submit.prevent="handleLogin">
        <div class="form-group">
            <label class="p-6" for="email">Email:</label>
            <input class="bg-white border" type="email" id="email" v-model="email" required />
        </div>
        <div class="form-group">
            <label class="p-6" for="password">Password:</label>
            <input class="bg-white border" type="password" id="password" v-model="password" required />
        </div>
        <button class="bg-blue-500 text-white p-2 rounded" type="submit">Login</button>
        </form>
    </div>
</template>

<style scoped>

.form-group {
    margin: 1rem;
}

.login-container{
    max-width: 400px;
    margin: 0 auto;
    padding: 2rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

</style>