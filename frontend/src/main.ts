import "./assets/main.css";

import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
import { useAuthStore } from "@/stores/auth";

async function bootstrap() {
  const app = createApp(App);
  const pinia = createPinia();

  app.use(pinia);

  app.use(router);

  app.mount("#app");

  const authStore = useAuthStore(pinia);

  try {
    await authStore.initialize();
  } catch (error) {
    console.error("Authentication initialization failed:", error);
  }
}

bootstrap();
