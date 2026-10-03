interface Profile {
    userID: string,
    display_name: string,
    bio: string,
    goals: Goal[]
}

interface Goal {
    id: string,
    title: string,
    description: string,
    target_date: Date,
    completion_date: Date,
}

export type { Profile, Goal };