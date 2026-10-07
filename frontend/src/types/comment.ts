interface Comment {
    id: number;
    created: string;
    modified: string;
    username: string;
    content: string;
    workoutId: string;
}

interface CommentData {
    workout: string;
    content: string;
}

export type { Comment, CommentData };