import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'),
    children: [
      {
        path: '/answer/:que_id',
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
        component: () => import('../components/Question.vue')
      }
    ],
    redirect: to => {
      return { path: '/question' }
    }
  },

  {
    path: '/overview',
    name: 'Overview',
    component: () => import('../views/Overview.vue')
  },
  // {
  //   path: '/:pathMatch(.*)*',
  //   redirect: to => {
  //     return { path: '/' }
  //   }
  // }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
