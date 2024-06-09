<template>
    <div>
        <span>{{ item.name }}</span>
        <v-text-field v-model="item._prix" @change="updatePrice"></v-text-field>
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
            _prix: Number
        }
    },
    methods: {
        async updatePrice() {
            console.log(this.item._prix)
            await this.axios.put(`${this.backendUrl}/api/ingredients/${this.item.name}`, { "prix": this.item._prix })
        }
    }
}
</script>