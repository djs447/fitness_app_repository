import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: import('../layouts/PublicLayout.vue'),
      children: [
        {
          path: '',
          name: 'home',
          component: import('../views/PublicHomeView.vue'),
        },
        {
          path: 'login',
          name: 'login',
          component: import('../views/LoginView.vue'),
        },
        {
          path: 'register',
          name: 'register',
          component: import('../views/RegisterView.vue'),
        },
      ],
    },

    // Authenticated routes
    {
      path: '/app',
      component: import('../layouts/AuthenticatedLayout.vue'),
      meta: {
        requiresAuth: true,
      },
      children: [
        {
          path: '',
          component: import('../views/HomeView.vue'),
        },
        {
          path: 'profile/:id',
          name: 'profile',
          component: import('../views/ProfileView.vue'),
        },
        {
          path: 'workouts',
          name: 'workouts',
          component: import('../views/WorkoutsView.vue'),
        },
        {
          path: 'workouts/:id',
          name: 'workout',
          component: import('../views/WorkoutView.vue'),
        }
      ],
    },
  ],
})

router.beforeEach((to) => {
  const authStore = useAuthStore()
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    return '/login'
  }
})

export default router
