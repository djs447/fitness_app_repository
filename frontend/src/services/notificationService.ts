import api from '@/services/api'
import type { InboxMessage } from '@/types/notification'
    
export async function fetchMessages(): Promise<InboxMessage[]> {
    const response = await api.get('/inbox')
    return response.data
}

export async function markAsRead(messageId: string): Promise<void> {
    await api.post(`/inbox/${messageId}/mark-as-read/`);
}

export async function deleteMessage(messageId: string): Promise<void> {
    await api.delete(`/inbox/${messageId}/delete/`);
}

