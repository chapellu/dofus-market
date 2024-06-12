<template>
    <div style="padding: 20px;">
        <v-text-field v-model="search" label="Search" prepend-inner-icon="mdi-magnify" variant="outlined" hide-details
            single-line></v-text-field>
        <v-data-table-virtual mobile :items="items" :search="search" density="compact">
            <template v-slot:item="{ item }">
                <rune :item="item"></rune>
            </template>
        </v-data-table-virtual>
    </div>
</template>

<script lang="ts">
import Rune from "../Rune.vue";
import { RuneType } from '../types/RuneType'


export default {
    components: {
        Rune
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
            const response = await this.axios.get(`${this.backendUrl}/api/runes`)
            console.log(response.data)
            this.items = response.data
        },

        async updatePrice(item: RuneType) {
            console.log(item)
        }
    },

}
</script>