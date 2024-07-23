<template>
    <div>
        <v-row class="d-flex flex-row" variant="elevated" style="margin: 2px; padding: 2px">
            <v-col cols="4" class="d-flex align-center justify-center " style="width: 100%; padding: 1px;">
                <div style="font-size: 12px;">{{ item.name }}</div>
            </v-col>
            <v-col cols="6" class="d-flex flex-row" style="width: 100%; padding: 1px;">
                <v-col cols="3" class="d-flex flex-column align-center" style="width: 100%; padding: 1px;">
                    <font-awesome-icon icon="percent" />
                    <v-chip :color="getColor(item.rentabilite)">
                        {{ item.rentabilite }}
                    </v-chip>
                </v-col>
                <v-col cols="3" class="d-flex flex-column align-center" style="width: 100%; padding: 1px;">
                    <font-awesome-icon icon="coins" />
                    <v-text-field class="small-center-text-field" width="100%" readonly density="compact" hide-details
                        v-model="item.gainEstime" placeholder="-"></v-text-field>
                </v-col>
                <v-col cols="3" class="d-flex flex-column align-center" style="width: 100%; padding: 1px;">
                    <font-awesome-icon icon="hammer" />
                    <v-text-field class="small-center-text-field" width="100%" readonly density="compact" hide-details
                        v-model="computedCraftCost"></v-text-field>
                </v-col>
                <v-col cols="3" class="d-flex flex-column align-center" style="width: 100%; padding: 1px;">
                    <font-awesome-icon icon="flask" />
                    <v-text-field class="small-center-text-field" width="100%" readonly density="compact" hide-details
                        v-model="item.nbObjet"></v-text-field>
                </v-col>
            </v-col>
        </v-row>
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
    },
    computed: {
        computedCraftCost: {
            get() {
                return this.formatter.format(this.item.coutFabrication);
            },
            set(newValue: any) {
                this.item.coutFabrication = Number(newValue); //TODO this not working
            }
        },
        computedEstimatedGain: {
            get() {
                return this.formatter.format(this.item.gainEstime);
            },
            set(newValue: any) {
                this.item.gainEstime = Number(newValue); //TODO this not working
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