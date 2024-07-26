<template>
    <div>
        <!-- <v-lazy :options="{ 'threshold': 0.5 }" transition="fade-transition"> -->
        <v-card class="d-flex flex-row" variant="elevated" style="width: 100%; padding: 1px;">
            <v-col cols="6" class="d-flex align-center justify-left " style="width: 100%; padding: 1px;">
                <div data-testid="ingredient-quantity-name" style="font-size: 12px;">{{ item.quantity }} X {{
                    item.name }}</div>
            </v-col>
            <v-col cols="6" class="d-flex flex-row" style="width: 100%; padding: 1px;">
                <v-col cols="3" class="d-flex flex-column align-center" style="width: 100%; padding: 1px;">
                        <div data-testid="ingredient-rentability" v-if="item.rentabilite"
                        class="d-flex flex-column align-center">
                        <font-awesome-icon icon="percent" />
                        <v-chip :color="getColor(item.rentabilite)">
                            {{ Math.round(item.rentabilite) }}
                        </v-chip>
                    </div>
                </v-col>
                <v-col cols="3" class="d-flex flex-column align-center" style="width: 100%; padding: 1px;">
                    <font-awesome-icon icon="landmark" />
                    <v-text-field data-testid="ingredient-price" class="small-center-text-field" width="100%"
                        density="compact" hide-details v-model="computedPrice" @click.stop placeholder="-"
                        @change="updatePrice(item)" @update:model-value="updatePriceValue"></v-text-field>
                </v-col>
                    <v-col cols="3" class="d-flex flex-column align-center" v-if="item.coutFabrication > 0"
                    data-testid=ingredient-fabrication-cost style="width: 100%; padding: 1px;">
                    <font-awesome-icon icon="hammer" />
                        <v-text-field class="small-center-text-field" width="100%" readonly density="compact"
                            hide-details @click.stop v-model="computedCraftCost"></v-text-field>
                </v-col>
                    <v-col cols="3" class="d-flex flex-column align-center" v-if="item.nbObjet > 0"
                    data-testid=ingredient-nb-object style="width: 100%; padding: 1px;">
                    <font-awesome-icon icon="flask" />
                        <v-text-field class="small-center-text-field" width="100%" readonly density="compact"
                            hide-details @click.stop v-model="item.nbObjet"></v-text-field>
                </v-col>
            </v-col>
        </v-card>
        <!-- </v-lazy> -->
    </div>
</template>

<script lang="ts">
// import { backendUrl } from '../config'
import { transport } from '@/transport'
import { createPromiseClient } from "@connectrpc/connect";
import { IngredientController } from "@/grpc/grpc_market_connect";
import { IngredientRequest } from "@/grpc/grpc_market_pb";

const ingredientClient = createPromiseClient(IngredientController, transport);

export default {
    data: () => ({
        // backendUrl: backendUrl,
        formatter: Intl.NumberFormat('FR', { notation: 'compact' }),
        internalPrice: 0,
    }),
    props: {
        "item": {
            type: Object,
            required: true
        }
    },
    methods: {
        getColor(rentabilite: number) {
            if (rentabilite <= 0) return 'red'
            else if (rentabilite < 20) return 'orange'
            else return 'green'
        },
        reverseFormatting(formattedValue: string) {
            // Remove any non-numeric characters from the input
            const numericString = formattedValue.replace(/[^0-9.-]/g, '')

            // Parse the numeric string to a number
            let number = parseFloat(numericString)

            // Define the suffixes and their corresponding multipliers
            const suffixes = [
                { suffix: 'k', multiplier: 1000 },
                { suffix: 'M', multiplier: 1000000 },
                { suffix: 'Md', multiplier: 1000000000 },
                { suffix: 'bn', multiplier: 1000000000000 },
            ]

            // Find the matching suffix and apply the corresponding multiplier
            const matchedSuffix = suffixes.find(suffixObj =>
                formattedValue.endsWith(suffixObj.suffix)
            )

            if (matchedSuffix) {
                number *= matchedSuffix.multiplier
            }

            return number
        },
        async updatePrice(item: any) {
            this.item.price = this.internalPrice
            console.log(item)
            // await this.axios.put(`${this.backendUrl}/api/ingredients/${item.name}`, { "price": item.price })
            await ingredientClient.update(new IngredientRequest({ name: item.name, price: item.price }))
        },

        updatePriceValue(value: any) {
            this.internalPrice = value
        },
    },
    computed: {
        computedCraftCost: {
            get() {
                return this.formatter.format(this.item.coutFabrication);
            },
            set(newValue: any) {
                this.item.cout_fabrication = this.reverseFormatting(newValue)
            }
        },
        computedEstimatedGain: {
            get() {
                return this.formatter.format(this.item.gainEstime);
            },
            set(newValue: any) {
                this.item.gain_estime = this.reverseFormatting(newValue)
            }
        },
        computedPrice: {
            get() {
                return this.formatter.format(this.item.price);
            },
            set() {
            }
        }
    }
}
</script>

<style>
.v-chip.v-chip--size-default {
    --v-chip-size: none;
    --v-chip-height: none;
    font-size: 12px;
    padding: 0 12px;
}

.small-center-text-field .v-field__input {
    padding-inline: 6px;
    padding-top: 0px;
    padding-bottom: 0px;
    min-height: 0px;
    text-align: center;
}
</style>