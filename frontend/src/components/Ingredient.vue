<template>
    <div>
        <v-lazy :options="{ 'threshold': 0.5 }" transition="fade-transition">
            <v-card class="d-flex flex-row" variant="elevated" color="surface-variant">
                <v-col cols="6" class="d-flex align-center justify-left ">
                    <div style="font-size: 12px;">{{ item.quantity }} X {{ item.name }}</div>
                </v-col>
                <v-col cols="6" class="d-flex flex-row">
                    <v-col cols="3" class="d-flex flex-column align-center">
                        <div v-if="item.rentabilite > 0" class="d-flex flex-column align-center">
                            <font-awesome-icon icon="percent" />
                            <v-chip :color="getColor(item.rentabilite)">
                                {{ Math.round(item.rentabilite) }}
                            </v-chip>
                        </div>
                    </v-col>
                    <v-col cols="3" class="d-flex flex-column align-center">
                        <font-awesome-icon icon="landmark" />
                        <v-text-field width="100%" density="compact" hide-details v-model.lazy="computedPrice" @click.stop
                            placeholder="-" @change="updatePrice(item)"></v-text-field>
                    </v-col>
                    <v-col cols="3" class="d-flex flex-column align-center" v-if="item.cout_fabrication > 0">
                        <font-awesome-icon icon="hammer" />
                        <v-text-field width="100%" readonly density="compact" hide-details @click.stop
                            v-model="computedCraftCost"></v-text-field>
                    </v-col>
                    <v-col cols="3" class="d-flex flex-column align-center" v-if="item.nb_objet > 0">
                        <font-awesome-icon icon="flask" />
                        <v-text-field width="100%" readonly density="compact" hide-details @click.stop
                            v-model="item.nb_objet"></v-text-field>
                    </v-col>
                </v-col>
            </v-card>
        </v-lazy>
    </div>
</template>

<script lang="ts">
import { backendUrl } from '../config'

export default {
    data: () => ({
        backendUrl: backendUrl,
        formatter: Intl.NumberFormat('FR', { notation: 'compact' }),
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
            console.log(item)
            await this.axios.put(`${this.backendUrl}/api/ingredients/${item.name}`, { "price": item.price })
        }
    },
    computed: {
        computedCraftCost: {
            get() {
                return this.formatter.format(this.item.cout_fabrication);
            },
            set(newValue: any) {
                this.item.cout_fabrication = this.reverseFormatting(newValue)
            }
        },
        computedEstimatedGain: {
            get() {
                return this.formatter.format(this.item.gain_estime);
            },
            set(newValue: any) {
                this.item.gain_estime = this.reverseFormatting(newValue)
            }
        },
        computedPrice: {
            get() {
                return this.formatter.format(this.item.price);
            },
            set(newValue: any) {
                this.item.price = this.reverseFormatting(newValue)
            }
        }
    }
}
</script>