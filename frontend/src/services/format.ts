
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

export function formatDuration(duration: string | null | undefined): string {
    if (!duration) return '';

    const [hours, minutes, seconds] = duration.split(':');
    const totalSeconds = Number(seconds);

    const h = Number(hours);
    const m = Number(minutes);
    const s = Math.floor(totalSeconds);

    if (h > 0) {
        return `${h}h ${m}m ${s}s`;
    }

    if (m > 0) {
        return `${m}m ${s}s`;
    }

    return `${s}s`;
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

export function formatPace(
    pace: number | null | undefined,
    activityType: string | null | undefined
): string {
    if (pace == null || !Number.isFinite(pace) || pace <= 0) {
        return '--';
    }

    switch (activityType) {
        case 'running':
        case 'swimming': {
            const totalSeconds = Math.round(pace * 60);
            const minutes = Math.floor(totalSeconds / 60);
            const seconds = totalSeconds % 60;

            const formattedTime =
                `${minutes}:${String(seconds).padStart(2, '0')}`;

            return activityType === 'running'
                ? `${formattedTime} min/km`
                : `${formattedTime} /100m`;
        }

        case 'cycling':
            return `${pace.toFixed(1)} km/h`;

        default:
            return '--';
    }
}