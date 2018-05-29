import Vue from 'vue'
import Router from 'vue-router'
// import VueCookie from 'vue-cookie'
import Login from '@/components/Login'
import Home from '@/components/Home'
import Course from '@/components/Course'
import User from '@/components/User'
import Semester from '@/components/Semester'

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
          path: 'user',
          name: 'User',
          components: {
            body: User
          }
        },
        {
          path: 'semester',
          name: 'Semester',
          components: {
            body: Semester
          }
        }
      ]
    }
  ]
})

// router.beforeEach((to, from, next) => {
//   if (!VueCookie.get('id')) {
//     if (to.path === '/login') {
//       next()
//     } else {
//       next('/login')
//     }
//   } else {
//     if (to.path === '/login') {
//       next('/')
//     } else {
//       next()
//     }
//   }
// })

export default router
