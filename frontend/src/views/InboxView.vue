<script setup lang="ts">
import InboxMessageCard from '@/components/social/InboxMessageCard.vue'
import { useNotificationStore } from '@/stores/notification'
import { ref, onMounted } from 'vue'
import type { InboxMessage } from '@/types/notification'

const notificationStore = useNotificationStore()
const messages: InboxMessage[] = notificationStore.messages

onMounted(async () => {
  // Fetch messages from your API or store
  await notificationStore.fetchMessages()
})

async function deleteMessage(messageId: string) {
  // Update the local messages array
  const index = messages.findIndex(m => m.id === messageId)
  if (index !== -1) {
    messages.splice(index, 1)
  }
  await notificationStore.deleteMessage(messageId)
}

</script>

<template>
  <div class="inbox-container">
    <h1 class="inbox-header">Inbox</h1>
    <InboxMessageCard v-for="message in messages" :key="message.id" :message="message" @delete="deleteMessage(message.id)"/>
  </div>
</template>

<style scoped>
.inbox-container {
  width: 35vw;
  padding: 20px;
}
.inbox-header {
  margin-bottom: 20px;
  font-size: 24px;
  font-weight: bold;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  margin-bottom: 20px;
  border-bottom: 1px solid #ccc;
  padding-bottom: 10px;
  background-color: #f9f9f9;
  border-radius: 5px;
  padding: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
  margin-top: 20px;
}
.inbox-header:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
</style>