<script lang="ts">
import Equipement from "../Equipement.vue";
import { EquipementType } from '../types/EquipementType'
type SortItem = { key: string, order?: boolean | 'asc' | 'desc' }

export default {
    components: {
        Equipement
    },
    data: () => ({
        expanded: [],
        backendUrl: "http://127.0.0.1:8000",
        loading: true,
        search: '',
        sortBy: [{ key: 'rentabilite', order: 'desc' }, { key: 'cout_fabrication', order: 'asc' }] as Array<SortItem>,
        headers: [
            { title: 'Nom', key: 'name', sortable: false },
            { title: 'Rentabilité (%)', key: 'rentabilite' },
            { title: 'Gain estimé (K)', key: 'gain_estime' },
            { title: 'Cout de fabrication (K)', key: 'cout_fabrication' },
            { title: "Metier", key: "metier" },
            { title: "Nombre d'ingrédients", key: "nb_objet" }
        ],
        items: [] as Array<EquipementType>,
    }),

    methods: {
        getColor(rentabilite: number) {
            if (rentabilite <= 0) return 'red'
            else if (rentabilite < 20) return 'orange'
            else return 'green'
        },
        async getDataFromAPI() {
            const response = await this.axios.get(`${this.backendUrl}/api/equipements`)
            console.log(response.data)
            this.items = response.data
            this.loading = false
        },
        expandRow(item) {
            console.log(item)
            if (this.expanded.includes(item.name)) {
                this.expanded.splice(this.expanded.indexOf(item.name), 1)
            }
            else {
                this.expanded.push(item.name)
            }
        }
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
    <v-data-table-virtual mobile :items="items" disable-sort :sort-by="sortBy" multi-sort :search="search" density="compact"
        :loading="loading" item-value="name" :expanded="expanded">
        <template v-slot:item="{ item }">
            <equipement :item="item" @click="expandRow(item)"></equipement>
        </template>
        <!-- <template v-slot:item.rentabilite="{ value }">
            <v-chip :color="getColor(value)">
                {{ value }}
            </v-chip>
        </template> -->
        <template v-slot:expanded-row="{ item }">
            <v-data-table :items="item.ingredients"></v-data-table>
        </template>
    </v-data-table-virtual>
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
