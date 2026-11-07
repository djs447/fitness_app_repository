import { computed, ref } from 'vue';
import type { InboxMessage } from '@/types/notification';
import { defineStore } from 'pinia';

import type { Workout, WorkoutForm, PaginatedWorkouts } from '@/types/workout'
import type { Like } from '@/types/user';
import * as notificationService from '@/services/notificationService'

export const useNotificationStore = defineStore('notification', () => {
    const messages = ref<InboxMessage[]>([]);

    async function fetchMessages() {
        messages.value = await notificationService.fetchMessages();
    }

    async function markAsRead(messageId: string) {
        await notificationService.markAsRead(messageId);
        const message = messages.value.find(m => m.id === messageId);
        if (message) {
            message.read = true;
        }
    }

    async function deleteMessage(messageId: string) {
        messages.value = messages.value.filter(m => m.id !== messageId);
        await notificationService.deleteMessage(messageId);
    }

    return {
        messages,
        fetchMessages,
        markAsRead,
        deleteMessage,
    };
});