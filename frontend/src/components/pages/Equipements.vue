<template>
    <v-text-field v-model="name" label="Search" prepend-inner-icon="mdi-magnify" variant="outlined" hide-details single-line
        @change="updateSearch()"></v-text-field>
    <v-select label="Metier" :items="metiers" v-model:model-value="metier" @update:modelValue="updateSearch()"
        clearable></v-select>
    <v-data-table-server mobile :items="items" :items-length="totalItems" disable-sort hide-default-header
        :loading="loading" item-value="name" :expanded="expanded" @update:options="loadItems"
        v-model:items-per-page="itemsPerPage" :search="search">
        <template v-slot:loading>
            <div class="text-center py-5">
                <v-progress-circular indeterminate color="primary" />
                <p class="mt-3">Loading data...</p>
            </div>
        </template>
        <template v-slot:item="{ item }">
            <equipement :item="item" @click="expandRow(item)"></equipement>
        </template>
        <template v-slot:expanded-row="{ item }">
            <v-card>
                <v-tabs v-model="tab" align-tabs="center" stacked>
                    <v-tab value="tab-1">
                        <v-icon icon="mdi-flask"></v-icon>
                    </v-tab>

                    <v-tab value="tab-2">
                        <v-icon icon="mdi-diamond-stone"></v-icon>
                    </v-tab>

                    <v-tab value="tab-3">
                        <v-icon icon="mdi-hammer"></v-icon>
                    </v-tab>
                </v-tabs>

                <v-tabs-window v-model="tab">
                    <v-tabs-window-item :value="'tab-1'">
                        <v-card>
                            <Ingredients :ingredients="item.ingredients"></Ingredients>
                        </v-card>
                    </v-tabs-window-item>
                    <v-tabs-window-item :value="'tab-2'">
                        <v-card>
                            <v-data-table-virtual mobile :items="item.brisage" :headers="rune_headers">
                                <template v-slot:item.prix_ra="{ item }">
                                    <v-text-field label="Prix Ra" v-model.number="(item as any).prix_ra"
                                        @change="updatePrice(item)" density="compact" hide-details="auto" suffix="K"
                                        v-if="(item as any).prix_ra != -1"></v-text-field>
                                </template>
                                <template v-slot:item.total_ra="{ item }">
                                    {{ Number((item as any).prix_ra * (item as any).quantity_ra).toFixed(0) }}
                                </template>
                                <template v-slot:item.prix_pa="{ item }">
                                    <v-text-field label="Prix Pa" v-model.number="(item as any).prix_pa"
                                        @change="updatePrice(item)" density="compact" hide-details="auto" suffix="K"
                                        v-if="(item as any).prix_pa != -1"></v-text-field>
                                </template>
                                <template v-slot:item.total_pa="{ item }">
                                    {{ Number((item as any).prix_pa * (item as any).quantity_pa).toFixed(0) }}
                                </template>
                                <template v-slot:item.prix_ba="{ item }">
                                    <v-text-field label="Prix Ba" v-model.number="(item as any).prix_ba"
                                        @change="updatePrice(item)" density="compact" hide-details="auto" suffix="K"
                                        v-if="(item as any).prix_ba != -1"></v-text-field>
                                </template>
                                <template v-slot:item.total_ba="{ item }">
                                    {{ Number((item as any).prix_ba * (item as any).quantity_ba).toFixed(0) }}
                                </template>
                                <template v-slot:item.total="{ item }">
                                    {{ Number((item as any).prix_ra * (item as any).quantity_ra + (item as any).prix_pa *
                                        (item as any).quantity_pa +
                                        (item as any).prix_ba * (item as any).quantity_ba).toFixed(0) }}
                                </template>
                            </v-data-table-virtual>
                        </v-card>
                    </v-tabs-window-item>
                    <v-tabs-window-item :value="'tab-3'">
                        <v-card>
                            To be defined
                        </v-card>
                    </v-tabs-window-item>
                </v-tabs-window>
            </v-card>
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

        rune_headers: [
            { title: 'Rune', key: 'rune' },
            { title: 'Quantity RA', key: 'quantity_ra' },
            { title: 'Prix RA', key: 'prix_ra' },
            { title: 'Total Ra', key: 'total_ra' },
            { title: 'Quantity PA', key: 'quantity_pa' },
            { title: 'Prix PA', key: 'prix_pa' },
            { title: 'Total Pa', key: 'total_pa' },
            { title: 'Quantity BA', key: 'quantity_ba' },
            { title: 'Prix BA', key: 'prix_ba' },
            { title: 'Total Ba', key: 'total_ba' },
            { title: 'Total', key: 'total' },
        ],
        items: [] as Array<any>,
        metiers: [] as Array<any>,
        metier: '',
        itemsPerPage: 10,
        totalItems: 0,
        loading: true,
        name: '',
        tab: 'tab-1',
        mounted: false
    }),
    watch: {
        '$route.query': {
            handler() {
                this.metier = this.$route.query.metier as string || ''
                this.name = this.$route.query.search as string || ''
                this.getDataFromAPI()
            },
            immediate: true, // Fetch data on component mount
        },
    },
    methods: {
        async getDataFromAPI() {
            let params: Record<string, any> = {
                page: this.$route.query.page || 1, // Default to page 1 if not present
                page_size: this.$route.query.itemsPerPage || 10, // Default to 10 items per page
            }
            if (this.$route.query.search) {
                params.search = this.$route.query.search
            }
            if (this.$route.query.metier) {
                params.metier = this.$route.query.metier
            }
            const response = await this.axios.get(`${this.backendUrl}/api/equipements`, {
                params: params,
            })
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
                this.expanded.push(item.name)
            }
        },
        async updateURL(page: number, itemsPerPage: number, search: string, metier: string) {
            let params: Record<string, any> = {
                "page": page,
                "page_size": itemsPerPage
            }
            if (search) {
                params["search"] = search
            }
            if (metier) {
                params["metier"] = this.metier
            }
            await this.$router.push({ path: this.$route.path, query: params });
        },
        async loadItems({ page, itemsPerPage, search }: any) {
            if (this.mounted) {
                this.loading = true
                console.log(page, itemsPerPage, search, this.name, this.metier)
                await this.updateURL(page, itemsPerPage, this.name, this.metier)
            }
            else {
                this.mounted = true
            }
        },
        async updateSearch() {
            this.search = String(Date.now())
        },
        async updatePrice(rune: any) {
            await this.axios.put(`${this.backendUrl}/api/runes/${rune.rune}`, { "prix_ra": rune.prix_ra, "prix_pa": rune.prix_pa, "prix_ba": rune.prix_ba })
        }
    },
    async mounted() {
        let response = await this.axios.get(`${this.backendUrl}/api/metiers`)
        this.metiers = response.data.map((profession: { name: any; }) => profession.name);
        console.log(this.metiers)
    },
}
</script>

<style scoped></style>