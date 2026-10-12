interface Comment {
    id: string;
    created: string;
    modified: string;
    username: string;
    content: string;
    workout: string;
    user: {
        username: string;
        id: number;
    };
}

interface CommentData {
    workout: string;
    content: string;
}

interface EditCommentData {
    id: string;
    content: string;
    workout: string;
}

export type { Comment, CommentData, EditCommentData };