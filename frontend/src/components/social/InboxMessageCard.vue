<script setup lang="ts">
import type { InboxMessage } from '@/types/notification'
import { verboseDateTime } from '@/services/format.ts'
import { useNotificationStore } from '@/stores/notification'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faTrash } from '@fortawesome/free-solid-svg-icons'
const props = defineProps<{
  message: InboxMessage
}>()

const emit = defineEmits<{
  (e: 'delete', messageId: string): void
}>()

const notificationStore = useNotificationStore()
const markAsRead = () => {
  notificationStore.markAsRead(props.message.id)
  props.message.read = true
}

</script>

<template>
  <div class="inbox-message-card">
    <div class="message-header flex justify-between items-center">
      <span class="message-sender">{{ props.message.sent_by.username }}</span>
      <span class="message-date">{{ verboseDateTime(props.message.created) }}</span>
    </div>
    <p class="message-body">{{ props.message.message }}</p>
    <div class="message-actions flex justify-between">
      <button v-if="!props.message.read" @click="markAsRead" class="mark-as-read">Mark as Read</button>
      <span v-else class="read-message">Read</span>
      <button @click="emit('delete', props.message.id)" class="delete-message">
        <FontAwesomeIcon :icon="faTrash" />
      </button>

    </div>
  </div>
</template>

<style scoped>
.message-body {
  margin-bottom: 10px;
}
.message-header {
  margin-bottom: 5px;
}
.message-sender {
  font-weight: bold;
}
.message-date {
  font-size: 0.9em;
  color: #666;
}
.inbox-message-card {
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
  padding: 10px;
  margin-bottom: 10px;
  width: 100%;
}
.mark-as-read {
  background-color: #8bc34a;
  color: white;
  border: none;
  border-radius: 3px;
  padding: 5px 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
.mark-as-read:hover {
  background-color: #7cb342;
}
.delete-message {
  background-color: #f44336;
  color: white;
  border: none;
  border-radius: 3px;
  padding: 5px 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
.delete-message:hover {
  background-color: #d32f2f;
}
.read-message {
  color: #8bc34a;
  font-weight: bold;
}
</style>