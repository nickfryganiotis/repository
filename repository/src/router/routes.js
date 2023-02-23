const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: "",
        component: () => import("pages/HomePage.vue"),
      },
      {
        path: "/search_activity",
        component: () => import("pages/SearchActivity.vue"),
      },
      {
        path: "/create_activity",
        component: () => import("pages/CreateActivity.vue"),
      },
      {
        path: "/activity_description",
        component: () => import("pages/ActivityDescription.vue"),
      },
      {
        path: "/contact_page",
        component: () => import("pages/ContactPage.vue"),
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
