import Vue from 'vue'
import Router from 'vue-router'
import VueCookie from 'vue-cookie'
import Login from '@/components/Login'
import Home from '@/components/Home'
import Course from '@/components/Course'
import Grades from '@/components/Grades'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/',
      name: 'Home',
      component: Home,
      children: [
        {
          path: 'course',
          name: 'Course',
          components: {
            body: Course
          }
        },
        {
          path: 'grades',
          name: 'Grades',
          components: {
            body: Grades
          }
        }
      ]
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
