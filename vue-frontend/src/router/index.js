import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path:'/videos',
    name:'videos',
    component: () => import('../views/VideoListView.vue')
  },
  {
    path:'/upload',
    name:'upload',
    component: () => import('../views/UploadView.vue')
  },
  {
    path:'/watch/:id',
    name:'watch',
    component: () => import('../views/VideoView.vue')
  },
  {
    path:'/login',
    name:'login',
    component: () => import('../views/LoginView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
