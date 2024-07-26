<template>
    <div style="padding: 20px;">
        <v-text-field v-model="search" label="Search" prepend-inner-icon="mdi-magnify" variant="outlined" hide-details
            single-line></v-text-field>
        <v-data-table-virtual mobile :items="items" :search="search" density="compact">
            <template v-slot:item="{ item }">
                <rune :rune="item"></rune>
            </template>
        </v-data-table-virtual>
    </div>
</template>

<script lang="ts" setup>
import Rune from "@/components/Rune.vue";
import { RuneType } from '@/types/RuneType'
import { backendUrl } from '@/config'
import { ref, onMounted, defineComponent } from 'vue'
import { createPromiseClient } from "@connectrpc/connect";
import { createGrpcWebTransport } from "@connectrpc/connect-web";
import { RuneController } from "@/grpc/grpc_market_connect";
import { RuneListRequest } from "@/grpc/grpc_market_pb";

const transport = createGrpcWebTransport({
    baseUrl: "http://localhost:9001",
});

// Here we make the client itself, combining the service
// definition with the transport.
// See https://connectrpc.com/docs/web/using-clients
const client = createPromiseClient(RuneController, transport);


const search = ref('');
const items = ref([]);

const getDataFromAPI = async () => {
    const response = await client.list(new RuneListRequest())
    const data = await response;
    console.log(data);
    items.value = data.results as unknown as any[];
};


onMounted(async () => {
    await getDataFromAPI();
});

</script>