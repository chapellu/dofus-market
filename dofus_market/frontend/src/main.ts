import { createApp } from "vue";
import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

// Axios
import axios from "axios";
import VueAxios from "vue-axios";

// Components
import App from "./App.vue";
import Equipements from "./components/pages/Equipements.vue";
import Ingredients from "./components/pages/Ingredients.vue";
import Runes from "./components/pages/Runes.vue";

const routes: Array<RouteRecordRaw> = [
  { path: "/", component: Equipements },
  { path: "/ingredients", component: Ingredients },
  { path: "/runes", component: Runes },
];

const vuetify = createVuetify({
  components,
  directives,
});

const router = createRouter({
  history: createWebHistory(),
  routes,
});

createApp(App).use(vuetify).use(VueAxios, axios).use(router).mount("#app");
