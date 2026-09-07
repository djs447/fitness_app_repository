<script setup lang="ts">

import { ref } from 'vue';

const name = ref('');
const email = ref('');
const password = ref('');

const handleRegister = () => {
    // Handle registration logic here
    console.log('Registering user:', name.value, email.value, password.value);
};

</script>

<template>
    <div class="register-container">
        <h1>Register</h1>
        <form @submit.prevent="handleRegister">
            <div class="form-group">
                <label class="p-6" for="name">Name:</label>
                <input class="bg-white border" type="text" id="name" v-model="name" required />
            </div>
            <div class="form-group">
                <label class="p-6" for="email">Email:</label>
                <input class="bg-white border" type="email" id="email" v-model="email" required />
            </div>
            <div class="form-group">
                <label class="p-6" for="password">Password:</label>
                <input class="bg-white border" type="password" id="password" v-model="password" required />
            </div>
            <button class="bg-blue-500 text-white p-2 rounded" type="submit">Register</button>
        </form>
    </div>
</template>

<style scoped>
.form-group {
    margin: 1rem;
}

.register-container{
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