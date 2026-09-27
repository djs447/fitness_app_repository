<script setup lang="ts">

import { ref } from 'vue';
import { useRouter } from 'vue-router';

import { useAuthStore } from '@/stores/auth';

const username = ref('')
const password = ref('')
const error = ref('')

const authStore = useAuthStore()
const router = useRouter()

async function handleLogin() {
    error.value = ''

    try {
        await authStore.login(
            username.value,
            password.value,
        )

        await router.push('/app')
    } catch (err) {
        console.error('Login err', err)
        error.value = 'Invalid username or password.'
    }
}

</script>

<template>
    <div class="login-container">
        <form @submit.prevent="handleLogin">
        <div class="form-group">
            <label class="p-6 text-black" for="email">Username:</label>
            <input class="bg-white border" type="text" id="username" v-model="username" required />
        </div>
        <div class="form-group">
            <label class="p-6 text-black" for="password">Password:</label>
            <input class="bg-white border" type="password" id="password" v-model="password" required />
        </div>
        <p v-if="error">
            {{  error }}
        </p>
        <div class="button-container">
            <button class="bg-green-950 text-white p-2 rounded" type="submit">Login</button>
        </div>
        </form>
    </div>
</template>

<style scoped>

button{
    border: 2px solid black;
}

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
    background-color: var(--public-container-color)
}

.button-container{
    display: flex;
    flex-direction: column;
    margin: auto auto;
    width: 20%;
}

</style>