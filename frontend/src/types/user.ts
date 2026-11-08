interface User {
  id: number;
  user: string;
  email: string;
  display_name: string;
  first_name: string;
  last_name: string;
  profile: string;
  username: string;
}

interface LikeUser {
  id: number;
  username: string;
}

interface LikeWorkout {
  id: number;
  title: string;
}

interface Like {
  user: LikeUser;
  workout: LikeWorkout;
}

export type { User, Like, LikeUser, LikeWorkout };
