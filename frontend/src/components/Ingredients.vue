<template>
    <v-data-table-virtual mobile :items="ingredients" :sort-by="sortBy" style="padding-left: 20px;" :expanded="expanded"
        hideDefaultHeader item-value="name">
        <template v-slot:item="{ item }">
            <ingredient :item="item" @click="expandRow(item)"></ingredient>
        </template>
        <template v-slot:expanded-row="{ item }">
            <ingredients :ingredients="item.ingredients" v-if="item.ingredients.length > 0"></ingredients>
        </template>
    </v-data-table-virtual>
</template>

<script lang="ts">
import Ingredient from "./Ingredient.vue";
import { backendUrl } from '../config'

type SortItem = { key: string, order?: boolean | 'asc' | 'desc' }

export default {
    name: "Ingredients",
    props: {
        ingredients: {
            type: Array<any>,
            required: true,
        }
    },
    components: {
        Ingredient,
    },
    data: () => ({
        expanded: [] as Array<any>,
        backendUrl: backendUrl,
        sortBy: [{ key: 'quantity', order: 'desc' }] as Array<SortItem>,
    }),

    methods: {
        getColor(rentabilite: number) {
            if (rentabilite <= 0) return 'red'
            else if (rentabilite < 20) return 'orange'
            else return 'green'
        },
        expandRow(item: any) {
            console.log(item)
            if (this.expanded.includes(item.name)) {
                this.expanded.splice(this.expanded.indexOf(item.name), 1)
            }
            else {
                this.expanded.push(item.name)
            }
        },
    },
}
</script>