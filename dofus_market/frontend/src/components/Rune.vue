<template>
    <div>
        <v-row class="align-center">
            <v-col cols="12">
                <v-list-subheader>{{ item.name }}</v-list-subheader>
            </v-col>
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

export default {
    data: () => ({
        backendUrl: "http://127.0.0.1:8000",
    }),
    props: {
        item: {
            name: String,
            prix_ra: Number,
            prix_pa: Number,
            prix_ba: Number
        }
    },
    methods: {
        async updatePrice() {
            await this.axios.put(`${this.backendUrl}/api/runes/${this.item.name}`, { "prix_ra": this.item.prix_ra, "prix_pa": this.item.prix_pa, "prix_ba": this.item.prix_ba })
        }
    }
}
</script>