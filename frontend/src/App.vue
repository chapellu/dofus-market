<template>
  <v-app>
    <v-navigation-drawer temporary v-model="drawer" app>
      <v-list v-model:selected="selectedItem">
        <v-list-item v-for="item in menuItems" :key="item.title" :value="item.title" @click="navigate(item.route)">
          <template v-slot:prepend>
            <v-icon>{{ item.icon }}</v-icon>
          </template>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Dofus Market</v-toolbar-title>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>
 
<script lang="ts">
import { debounce } from 'lodash';

export default {
  data: () => ({
    drawer: false,
    selectedItem: null,
    menuItems: [
      { title: 'Equipements', icon: 'mdi-shield', route: '/' },
      { title: 'Runes', icon: 'mdi-diamond-stone', route: '/runes' },
      { title: 'Ingredients', icon: 'mdi-flask', route: '/ingredients' },
    ]
  }),

  methods: {
    navigate(route: string) {
      // Debounce the navigation with a delay of 200ms
      const debouncedNavigate = debounce(() => {
        this.$router.push(route);
      }, 200);
      debouncedNavigate(); // Execute the debounced function
    }
  }
};
</script>
 