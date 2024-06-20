<template>
  <v-app>
    <v-navigation-drawer v-model="drawer" app>
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
      this.$router.push(route);
    }
  }
};
</script>
 