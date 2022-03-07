import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'),
    children: [
      {
        path: '/answer/:ques_id',
        name: 'Answer',
        component: () => import('../components/Answer.vue'),
        props: { default: true }
        // redirect: {
        //   name: 'Home'
        // }
      },
      {
        path: '/question',
        name: 'Question',
        component: () => import('../components/AddQuestion.vue')
      }
    ]
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  // {
  //   path: '/question',
  //   name: 'Login',
  //   component: () => import('../views/Question.vue')
  // },
  {
    path: '/:pathMatch(.*)*',
    redirect: to => {
      return { path: '/' }
    }
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router