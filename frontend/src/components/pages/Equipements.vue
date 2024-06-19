<template>
    <v-text-field v-model="search" label="Search" prepend-inner-icon="mdi-magnify" variant="outlined" hide-details
        single-line></v-text-field>
    <v-data-table-server mobile :items="items" :items-length="totalItems" :sort-by="sortBy" multi-sort :search="search"
        :loading="loading" item-value="name" :expanded="expanded" @update:options="loadItems"
        v-model:items-per-page="itemsPerPage">
        <template v-slot:item="{ item }">
            <equipement :item="item" @click="expandRow(item)"></equipement>
        </template>
        <template v-slot:expanded-row="{ item }">
            <Ingredients :ingredients="item.ingredients"></Ingredients>
        </template>
    </v-data-table-server>
</template>

<script lang="ts">
import Equipement from "../Equipement.vue";
import Ingredient from "../Ingredient.vue";
import Ingredients from "../Ingredients.vue";
import { backendUrl } from '../../config';

type SortItem = { key: string, order?: boolean | 'asc' | 'desc' }

export default {
    components: {
        Equipement,
        Ingredient,
        Ingredients
    },
    data: () => ({
        expanded: [] as Array<any>,
        backendUrl: backendUrl,
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
        items: [] as Array<any>,
        itemsPerPage: 15,
        totalItems: 0,
        loading: true,

    }),

    methods: {
        async getDataFromAPI(page: any, itemsPerPage: any) {
            const response = await this.axios.get(`${this.backendUrl}/api/equipements?page=${page}&page_size=${itemsPerPage}`)
            console.log(response.data)
            this.items = response.data.results
            this.totalItems = response.data.count
            this.loading = false
        },
        async getEquipmentDetailsFromAPI(item: any) {
            const response = await this.axios.get(`${this.backendUrl}/api/equipements/${item.name}`)
            return response.data
        },
        async expandRow(item: any) {
            if (this.expanded.includes(item.name)) {
                this.expanded.splice(this.expanded.indexOf(item.name), 1)
            }
            else {
                this.items[this.items.indexOf(item)] = await this.getEquipmentDetailsFromAPI(item)
                console.log(item)
                this.expanded.push(item.name)
            }
        },
        async loadItems({ page, itemsPerPage }: any) {
            this.loading = true
            console.log(page, itemsPerPage)
            await this.getDataFromAPI(page, itemsPerPage)
        },
    },
}
</script>

<style scoped></style>