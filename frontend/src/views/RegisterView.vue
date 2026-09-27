<script setup lang="ts">

import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';

const username = ref('')
const email = ref('')
const password = ref('')
const error = ref('')

const authStore = useAuthStore()
const router = useRouter()

async function handleRegister() {
    // Handle registration logic here

    error.value = ''

    try{
        await authStore.register(
            username.value,
            email.value,
            password.value,
        )

        await router.push('/app')
    } catch (err) {
        console.error('Registration err', err)
        error.value = 'Invalid registration information.'
    }
};

</script>

<template>
    <div class="register-container">
        <form @submit.prevent="handleRegister">
            <div class="form-group">
                <label class="p-6 text-black" for="name">Name:</label>
                <input class="bg-white border" type="text" id="name" v-model="username" required />
            </div>
            <div class="form-group">
                <label class="p-6 text-black" for="email">Email:</label>
                <input class="bg-white border" type="email" id="email" v-model="email" required />
            </div>
            <div class="form-group">
                <label class="p-6 text-black" for="password">Password:</label>
                <input class="bg-white border" type="password" id="password" v-model="password" required />
            </div>
            <div class="button-container">
                <button class="bg-green-950 text-white p-2 rounded" type="submit">Register</button>
            </div>
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
    background-color: var(--public-container-color)
}

.button-container{
    display: flex;
    flex-direction: column;
    margin: auto auto;
    min-width: 20%;
    width: 30%;
}
</style>