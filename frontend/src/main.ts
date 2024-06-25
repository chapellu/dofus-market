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

/* import the fontawesome core */
import { library } from "@fortawesome/fontawesome-svg-core";
/* import font awesome icon component */
import {
  faLandmark,
  faPercent,
  faCoins,
  faFlask,
  faHammer,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import "@mdi/font/css/materialdesignicons.css";

library.add(faLandmark, faPercent, faCoins, faFlask, faHammer);

const routes: Array<RouteRecordRaw> = [
  { path: "/", component: Equipements },
  { path: "/ingredients", component: Ingredients },
  { path: "/runes", component: Runes },
];

const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: "dark",
  },
});

const router = createRouter({
  history: createWebHistory(),
  routes,
});

createApp(App)
  .component("font-awesome-icon", FontAwesomeIcon)
  .use(vuetify)
  .use(VueAxios, axios)
  .use(router)
  .mount("#app");
