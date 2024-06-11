<template>
    <div style="padding: 20px;">
        <v-text-field v-model="search" label="Search" prepend-inner-icon="mdi-magnify" variant="outlined" hide-details
            single-line></v-text-field>
        <v-data-table-virtual mobile :items="items" :search="search" density="compact" disable-sort="true">
            <template v-slot:item="{ item }">
                <ingredient :item="item"></ingredient>
            </template>
        </v-data-table-virtual>
    </div>
</template>

<script lang="ts">
import Ingredient from "../Ingredient.vue";

export default {
    components: {
        Ingredient
    },
    data: () => ({
        backendUrl: "http://127.0.0.1:8000",
        search: '',
        items: []
    }),
    async mounted() {
        await this.getDataFromAPI()
    },
    methods: {
        async getDataFromAPI() {
            const response = await this.axios.get(`${this.backendUrl}/api/ingredients`)
            console.log(response.data)
            this.items = response.data
        },

        async updatePrice(item) {
            console.log(item)
        }
    },

}
</script>