<template>
    <div style="padding: 20px;">
        <v-text-field v-model="name" label="Search" prepend-inner-icon="mdi-magnify" variant="outlined" hide-details
            single-line @change="updateSearch()"></v-text-field>
        <v-data-table-server mobile :items="items" :items-length="totalItems" :search="search" density="compact"
            @update:options="loadItems" :loading="loading" disable-sort hide-default-header item-value="name">
            <template v-slot:item="{ item }">
                <div>
                    <v-row class="align-center">
                        <v-col cols="8">
                            <v-list-subheader>{{ item.name }}</v-list-subheader>
                        </v-col>

                        <v-col cols="4">
                            <v-text-field v-model="item.price" @change="updatePrice(item)" density="compact"
                                hide-details="auto" suffix="K"></v-text-field>
                        </v-col>
                    </v-row>
                </div>
            </template>
        </v-data-table-server>
    </div>
</template>

<script lang="ts">
import Ingredient from "../Ingredient.vue";
import { backendUrl } from '../../config';

export default {
    components: {
        Ingredient
    },
    data: () => ({
        backendUrl: backendUrl,
        search: '',
        items: [] as Array<any>,
        totalItems: 0,
        loading: false,
        name: '',
        mounted: false,
    }),
    watch: {
        '$route.query': {
            handler() {
                this.getDataFromAPI()
            },
            immediate: true, // Fetch data on component mount
        },

    },
    methods: {
        async getDataFromAPI() {
            const response = await this.axios.get(`${this.backendUrl}/api/ingredients`, {
                params: {
                    page: this.$route.query.page || 1, // Default to page 1 if not present
                    page_size: this.$route.query.itemsPerPage || 10, // Default to 10 items per page
                    search: this.$route.query.search || '',
                },
            })
            this.items = response.data.results
            this.totalItems = response.data.count
        },

        async updatePrice(item: any) {
            console.log(item)
            await this.axios.put(`${this.backendUrl}/api/ingredients/${item.name}`, { "price": item.price })
        },
        async updateURL(page: number, itemsPerPage: number, search: string) {
            let params: Record<string, any> = {
                "page": page,
                "page_size": itemsPerPage
            }
            if (search) {
                params["search"] = search
            }
            await this.$router.push({ path: this.$route.path, query: params });
        },
        async loadItems({ page, itemsPerPage, search }: any) {
            if (this.mounted) {
                this.loading = true
                console.log(page, itemsPerPage, search, this.name)
                await this.updateURL(page, itemsPerPage, this.name)
            }
            else {
                this.mounted = true
            }
        },
        async updateSearch() {
            this.search = String(Date.now())
        }
    },

}
</script>