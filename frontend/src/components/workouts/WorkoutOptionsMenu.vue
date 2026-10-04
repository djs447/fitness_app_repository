<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faEllipsis, faPen, faTrash } from '@fortawesome/free-solid-svg-icons'

const emit = defineEmits<{
    edit: []
    delete: []
}>()

const isOpen = ref(false)

const toggleMenu = () => {
    isOpen.value = !isOpen.value
}

const editWorkout = () => {
    isOpen.value = false
    emit('edit')
}

const deleteWorkout = () => {
    isOpen.value = false
    emit('delete')
}

const menuRef = ref<HTMLElement | null>(null)

const handleClickOutside = (event: MouseEvent) => {
    if (
        menuRef.value &&
        !menuRef.value.contains(event.target as Node)
    ) {
        isOpen.value = false
    }
}

onMounted(() => {
    document.addEventListener('click', handleClickOutside)
})

onBeforeUnmount(() => {
    document.removeEventListener('click', handleClickOutside)
})

</script>

<template>
    <div class="relative">
        <!-- Meatballs -->
        <button
            type="button"
            class="text-gray-500 hover:text-blue-300 p-1"
            @click.stop="toggleMenu"
        >
            <FontAwesomeIcon :icon="faEllipsis" />
        </button>

        <!-- Dropdown -->
        <div
            v-if="isOpen"
            ref="menuRef"
            class="absolute right-0 mt-1 w-32 bg-white border border-gray-200 rounded shadow-lg z-10"
        >
            <button
                type="button"
                class="w-full text-left px-4 py-2 hover:bg-gray-100"
                @click="editWorkout"
            >
                <FontAwesomeIcon :icon="faPen" class="mr-2" />
                Edit
            </button>

            <button
                type="button"
                class="w-full text-left px-4 py-2 hover:bg-gray-100 text-red-600"
                @click="deleteWorkout"
            >
                <FontAwesomeIcon :icon="faTrash" class="mr-2" />
                Delete
            </button>
        </div>
    </div>
</template>