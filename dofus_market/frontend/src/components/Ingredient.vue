<template>
    <div>
        <v-row class="align-center">
            <v-col cols="8">
                <v-list-subheader>{{ item.name }}</v-list-subheader>
            </v-col>

            <v-col cols="4">
                <v-text-field v-model="item.price" @change="updatePrice" density="compact" hide-details="auto"
                    suffix="K"></v-text-field>
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
            price: Number
        }
    },
    methods: {
        async updatePrice() {
            await this.axios.put(`${this.backendUrl}/api/ingredients/${this.item.name}`, { "price": this.item.price })
        }
    }
}
</script>