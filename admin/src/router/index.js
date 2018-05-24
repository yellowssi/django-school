import Vue from 'vue'
import Router from 'vue-router'
import VueCookie from 'vue-cookie'
import Login from '@/components/Login'
import Home from '@/components/Home'
import Course from '@/components/Course'
import User from '@/components/User'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/course',
      name: 'Course',
      component: Course
    },
    {
      path: '/user',
      name: 'User',
      component: User
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (!VueCookie.get('id')) {
    if (to.path === '/login') {
      next()
    } else {
      next('/login')
    }
  } else {
    if (to.path === '/login') {
      next('/')
    } else {
      next()
    }
  }
})

export default router
