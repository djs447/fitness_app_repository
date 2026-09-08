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
        <h1>Login</h1>
        <form @submit.prevent="handleLogin">
        <div class="form-group">
            <label class="p-6" for="email">Username:</label>
            <input class="bg-white border" type="text" id="username" v-model="username" required />
        </div>
        <div class="form-group">
            <label class="p-6" for="password">Password:</label>
            <input class="bg-white border" type="password" id="password" v-model="password" required />
        </div>
        <p v-if="error">
            {{  error }}
        </p>
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