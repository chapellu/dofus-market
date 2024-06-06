<script lang="ts">
// import HelloWorld from './components/HelloWorld.vue'
export default {
  data: () => ({
    backendUrl: "http://127.0.0.1:8000",
    search: '',
    sortBy: [{ key: 'rentabilite', order: 'desc' }, { key: 'cout_fabrication', order: 'asc' }],
    headers: [
      { title: 'Nom', key: 'name', sortable: false },
      { title: 'Rentabilité (%)', key: 'rentabilite' },
      { title: 'Gain estimé (K)', key: 'gain_estime' },
      { title: 'Cout de fabrication (K)', key: 'cout_fabrication' },
      { title: "Metier", key: "metier" },
      { title: "Nombre d'ingrédients", key: "nb_objet" }
    ],
    items: []
    // items: [
    //   {
    //     nom: 'Bottines du Mulou',
    //     rentabilité: 10,
    //     gain_estimé: 1111,
    //     cout_fabrication: 1,
    //     metier: "Cordonnier",
    //     nb_objet: 10,
    //   },
    //   {
    //     nom: 'test2',
    //     rentabilité: 20,
    //     gain_estimé: 2222,
    //     cout_fabrication: 1,
    //     metier: "bucheron",
    //     nb_objet: 5,
    //   },
    //   {
    //     nom: 'test22',
    //     rentabilité: 20,
    //     gain_estimé: 2222,
    //     cout_fabrication: 15,
    //     metier: "alchimiste",
    //     nb_objet: 4,
    //   },
    //   {
    //     nom: 'test3',
    //     rentabilité: 50,
    //     gain_estimé: 333333,
    //     cout_fabrication: 4,
    //     metier: "poissonier",
    //     nb_objet: 3,
    //   },
    //   {
    //     nom: 'test4',
    //     rentabilité: 0,
    //     gain_estimé: 2222,
    //     cout_fabrication: 15,
    //     metier: "alchimiste",
    //     nb_objet: 6,
    //   },
    //   // ... more items
    // ]
    // items: [
    //   {
    //     "name": "Botte du Bouftou",
    //     "level": 10,
    //     "effects": [
    //       {
    //         "name": "Vitalité",
    //         "min": 100,
    //         "max": 150,
    //         "rune": {
    //           "id": 1,
    //           "name": "Vi",
    //           "prix_ra": 1000,
    //           "prix_pa": 100,
    //           "prix_ba": 10
    //         }
    //       }
    //     ],
    //     "ingredients": [
    //       {
    //         "name": "Bave du Bouftou",
    //         "quantity": 4
    //       },
    //       {
    //         "name": "Corne bouftou",
    //         "quantity": 10
    //       }
    //     ],
    //     "cout_fabrication": 248,
    //     "gain_estime": 427,
    //     "rentabilite": 72,
    //     "brisage": [
    //       [
    //         "Vitalité",
    //         0.09,
    //         2.64,
    //         7.39
    //       ]
    //     ],
    //     "nb_objet": 2,
    //     "metier": "cordonnier"
    //   }
    // ]
  }),

  methods: {
    getColor(rentabilite: number) {
      if (rentabilite <= 0) return 'red'
      else if (rentabilite < 20) return 'orange'
      else return 'green'
    },
    async getDataFromAPI() {
      const response = await this.axios.get(`${this.backendUrl}/api/`)
      console.log(response.data)
      this.items = response.data
    },
  },
  async mounted() {
    await this.getDataFromAPI()
  },
}
</script>

<template>
  <div>
    <h1>Dofus Market</h1>
  </div>
  <v-text-field v-model="search" label="Search" prepend-inner-icon="mdi-magnify" variant="outlined" hide-details
    single-line></v-text-field>
  <v-data-table-virtual mobile :items="items" :headers="headers" :sort-by="sortBy" multi-sort :search="search"
    density="compact">
    <template v-slot:item.rentabilite="{ value }">
      <v-chip :color="getColor(value)">
        {{ value }}
      </v-chip>
    </template>
  </v-data-table-virtual>
  <!-- <HelloWorld msg="Vite + Vue" /> -->
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}

.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
