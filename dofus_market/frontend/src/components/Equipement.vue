<template>
    <div>
        <v-card class="d-flex flex-row" variant="elevated" color="surface-variant">
            <v-col cols="6" class="d-flex align-center justify-center ">
                <div style="font-size: 12px;">{{ item.name }}</div>
            </v-col>
            <v-col cols="6" class="d-flex flex-row">
                <v-col cols="3" class="d-flex flex-column align-center">
                    <font-awesome-icon icon="percent" />
                    <v-chip :color="getColor(item.rentabilite)">
                        {{ item.rentabilite }}
                    </v-chip>
                </v-col>
                <v-col cols="3" class="d-flex flex-column align-center">
                    <font-awesome-icon icon="landmark" />
                    <v-text-field width="100%" readonly density="compact" hide-details="true" v-model="item.gain_estime"
                        placeholder="-"></v-text-field>
                </v-col>
                <v-col cols="3" class="d-flex flex-column align-center">
                    <font-awesome-icon icon="hammer" />
                    <v-text-field width="100%" readonly density="compact" hide-details="true"
                        v-model="computedCraftCost"></v-text-field>
                </v-col>
                <v-col cols="3" class="d-flex flex-column align-center">
                    <font-awesome-icon icon="flask" />
                    <v-text-field width="100%" readonly density="compact" hide-details="true"
                        v-model="item.nb_objet"></v-text-field>
                </v-col>
            </v-col>
        </v-card>
    </div>
</template>

<script lang="ts">
import { EquipementType } from './types/EquipementType'


export default {
    data: () => ({
        backendUrl: "http://127.0.0.1:8000",
        formatter: Intl.NumberFormat('FR', { notation: 'compact' }),
    }),
    props: {
        "item": {
            type: EquipementType,
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
                return this.formatter.format(this.item.cout_fabrication);
            },
            set(newValue) {
                this.item.cout_fabrication = Number(newValue); //TODO this not working
            }
        },
        computedEstimatedGain: {
            get() {
                return this.formatter.format(this.item.gain_estime);
            },
            set(newValue) {
                this.item.gain_estime = Number(newValue); //TODO this not working
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

.v-card {
    margin: 2px;
    padding: 2px
}

.v-col {
    width: 100%;
    padding: 1px;
}

.v-field {
    font-size: 12px;
}

.v-field__field {
    align-items: center;
}

.v-field__input {
    padding-inline: 6px;
    padding-top: 0px;
    padding-bottom: 0px;
    min-height: 0px;
    text-align: center;
}

.v-table .v-table__wrapper>table>thead>tr>th {
    border-bottom: none;
}
</style>