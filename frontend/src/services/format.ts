
export const formatDateTimeLocal = (dateString: string) => {
    const date = new Date(dateString)

    const year = date.getFullYear()
    const month = String(date.getMonth() + 1).padStart(2, '0')
    const day = String(date.getDate()).padStart(2, '0')
    const hours = String(date.getHours()).padStart(2, '0')
    const minutes = String(date.getMinutes()).padStart(2, '0')
    return `${year}-${month}-${day}T${hours}:${minutes}`
}

export const verboseDateTime = (dateString: string) => {
    const date = new Date(dateString)
    
    const options: Intl.DateTimeFormatOptions = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    }
    return date.toLocaleString('en-US', options)
}

export const parseDurationToForm = (duration:string) => {
    const [hours, minutes, seconds] = duration.split(':').map(Number)
    return { hours, minutes, seconds }
}

export const formatCommentDateTimeLocal = (dateString: string) => {
    const date = new Date(dateString)
    return date.toLocaleString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    })
}