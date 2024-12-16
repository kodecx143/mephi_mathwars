import { createRouter, createWebHistory } from 'vue-router';
import GameView from '../views/GameView.vue';
import Home from '../views/HomeView.vue'; // Создадим эту страницу для главного меню

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/game',
    name: 'Game',
    component: GameView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
