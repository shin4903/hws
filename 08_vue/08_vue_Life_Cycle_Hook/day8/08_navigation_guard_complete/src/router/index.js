import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView.vue'
import LoginView from '@/views/LoginView.vue'
import NotFound404 from '@/views/NotFound404.vue'
import DogView from '@/views/DogView.vue'

Vue.use(VueRouter)
const isLoggedIn = true
const routes = [
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  {
    path :'/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인 함')
        next({name : 'home'})
      } else {
        next() // 로그인이 안되어 있다면, 로그인 페이지로 이동
      }
    }
  },
  {
    path: '/dog/:breed',
    name : 'dog',
    component: DogView
  },
  {
    path: '*',
    redirect: '/404',

  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// // router/index.js
// router.beforeEach((to, from, next) => {
//   // CODE HERE
//   // 로그인 여부
//   const isLoggedIn = false

//   // 로그인이 필요한 페이지 지정
//   // const authPages = ['hello', 'home', 'about']
//   //반대
//   const allowAuthPages = ['login']  // 로그인 안해도 되는페이지

//   // 앞으로 이동할 페이지(to)가 로그인이 필요한 페이지인지 확인
//   // const isAuthRequired = authPages.includes(to.name)
//   // 반대
//   const isAuthRequired = !allowAuthPages.includes(to.name)

//   // 로그인이 필요한 페이지인데 로그인이 안되어있다면
//   if (isAuthRequired && !isLoggedIn) {
//     console.log('로그인으로 이동')
//     next({name : 'login'})
//   }
//     // 그렇지 않다면
//    else {
//     console.log('to로 이동')
//     next()
//   }
// })

export default router
