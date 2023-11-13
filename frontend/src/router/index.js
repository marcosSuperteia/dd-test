import { createRouter, createWebHistory } from "vue-router";
import BaseLayout from "@/layout/BaseLayout.vue";
import AuthLayout from "@/layout/AuthLayout.vue";
const routes = [
  {
    path: "/",
    component: BaseLayout,
    redirect: "loading",
    meta: {
      authRequired: true,
      hidden: true,
    },
    children: [
      {
        path: "/home",
        name: "home",
        component: () => import("../views/home/Home.vue"),
        meta: { transition: 'slide-right' },
      },
      {
        path: "/",
        name: "loading",
        component: () => import("../views/transition/index.vue"),
        meta: { transition: 'slide-right' },
      },
    ],
  },
  {
    path: "/login",
    component: AuthLayout,
    redirect: "login",
    children: [
      {
        path: "/login",
        name: "login",
        component: () => import("../views/auth/Login.vue"),
        meta: { transition: "slide-right" },
      },
      {
        path: "/register",
        name: "register",
        component: () => import("../views/auth/Register.vue"),
        meta: { transition: "slide-right" },
      },
      {
        path: "/confirm",
        name: "confirm",
        component: () => import("../views/auth/Confirm.vue"),
        meta: { transition: "slide-right" },
      },
      {
        path: "/reset-password",
        name: "reset",
        component: () => import("../views/auth/ResetPassword.vue"),
        meta: { transition: "slide-right" },
      },
      {
        path: "/password-recovery",
        name: "forgot",
        component: () => import("../views/auth/Forgot.vue"),
        meta: { transition: "slide-right" },
      },
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record)) {
    next();
  } else {
    next();
  }
});

export default router;
