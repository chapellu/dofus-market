<template>
    <v-data-table-virtual mobile :items="ingredients" style="padding-left: 20px;" :expanded="expanded" hideDefaultHeader
        item-value="name">
        <template v-slot:item="{ item }">
            <ingredient data-testid="ingredient" :item="item" @click="expandRow(item)"></ingredient>
        </template>
        <template v-slot:expanded-row="{ item }">
            <ingredients :ingredients="item.ingredients" v-if="item.ingredients.length > 0"></ingredients>
        </template>
    </v-data-table-virtual>
</template>

<script lang="ts">
import { ref, onMounted, defineComponent } from 'vue'
import { createPromiseClient } from "@connectrpc/connect";
import { RuneListRequest } from "@/grpc/grpc_market_pb";
import { transport } from '@/transport'
import Ingredient from "@/components/Ingredient.vue";
import { EquipementController, RuneController } from "@/grpc/grpc_market_connect";
import { EquipementDetailsRequest, EquipementListRequest, RuneRequest } from "@/grpc/grpc_market_pb";

const runeClient = createPromiseClient(RuneController, transport);
const client = createPromiseClient(EquipementController, transport);
type SortItem = { key: string, order?: boolean | 'asc' | 'desc' }

export default defineComponent({
    name: "Ingredients",
    props: {
        ingredients: {
            type: Array,
            required: true
        }
    },
    components: {
        Ingredient
    },
    setup(props) {
        // const sortedIngredients = ref([]);
        const expanded = ref([])
        // const sortIngredients = (sortItem: SortItem) => {
        //     sortedIngredients.value = [...props.ingredients].sort((a, b) => {
        //         const key = sortItem.key;
        //         const order = sortItem.order === 'desc' ? -1 : 1;
        //         if (a[key] < b[key]) return -1 * order;
        //         if (a[key] > b[key]) return 1 * order;
        //         return 0;
        //     });
        // };

        const getEquipmentDetailsFromAPI = async (item) => {
            console.log(`Get ${item.name} details`)
            const response = await client.details(new EquipementDetailsRequest({ name: item.name }))
            console.log(response)
            return response
        }

        const expandRow = async (item: any) => {
            if (expanded.value.includes(item.name)) {
                expanded.value.splice(expanded.value.indexOf(item.name), 1)
            }
            else {
                console.log(item)
                console.log(props.ingredients.indexOf(item))
                // props.ingredients[props.ingredients.indexOf(item)] = await getEquipmentDetailsFromAPI(item)
                expanded.value.push(item.name)
            }
        };

        onMounted(async () => {
            // const request = new RuneListRequest();
            // try {
            //     const response = await runeClient.list(request);
            //     console.log(response);
            // } catch (error) {
            //     console.error('Failed to fetch runes:', error);
            // }
            console.log(props)
        });
        return {
            // sortedIngredients,
            expanded,
            // sortIngredients,
            expandRow,
        };
    }
});
</script>