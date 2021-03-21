import Vue from 'vue'
import VueRouter from 'vue-router'
import aituBridge from '@btsd/aitu-bridge'
import axios from 'axios'
import store from '../store/index';


Vue.use(VueRouter)


const routes = [
  {
    path: '/',
    beforeEnter: ((to, from, next) => {
      next('/me')
    })
  },
  {
    path: '/me',
    name: 'Me',
    beforeEnter: ( (to, from, next) => {
      store.dispatch('sendProfile')
      next()
    }),
    component: () => import('../nav/mainNavigation.vue'),
    children: [
      {
        path: '/',
        name: 'Profile',
        component: () => import('../views/Profile.vue')
      },
      {
        path: 'profile',
        name: 'Profile_',
        component: () => import('../views/Profile.vue')
      },
      {
        path: 'search',
        name: 'Search',
        component: () => import('../views/Search.vue')
      },
      {
        path: 'map',
        name: 'Map',
        component: () => import('../views/Map.vue')
      }
      /*{
        path: 'meeting',
        name: 'Search',
        component: () => import('../views/Search.vue')
      }*/
    ]

  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
