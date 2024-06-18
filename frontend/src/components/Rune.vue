<template>
    <div>
        <v-row>
            <v-list-subheader>Rune {{ item.name }}</v-list-subheader>
        </v-row>
        <v-row class="align-center">
            <v-col cols="4">
                <v-text-field label="Prix Ra" v-model="item.prix_ra" @change="updatePrice" density="compact"
                    hide-details="auto" suffix="K"></v-text-field>
            </v-col>
            <v-col cols="4">
                <v-text-field label="Prix Pa" v-model="item.prix_pa" @change="updatePrice" density="compact"
                    hide-details="auto" suffix="K"></v-text-field>
            </v-col>
            <v-col cols="4">
                <v-text-field label="Prix Ba" v-model="item.prix_ba" @change="updatePrice" density="compact"
                    hide-details="auto" suffix="K"></v-text-field>
            </v-col>
        </v-row>
    </div>
</template>

<script lang="ts">

import { RuneType } from './types/RuneType'
import { backendUrl } from '../config'

export default {
    data: () => ({
        backendUrl: backendUrl,
    }),
    props: {
        item: {
            type: RuneType,
            required: true
        }
    },
    methods: {
        async updatePrice() {
            await this.axios.put(`${this.backendUrl}/api/runes/${this.item.name}`, { "prix_ra": this.item.prix_ra, "prix_pa": this.item.prix_pa, "prix_ba": this.item.prix_ba })
        }
    }
}
</script>

<style>
.v-row {
    margin: 0px
}
</style>