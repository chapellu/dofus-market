<template>
    <div>
        <v-row>
            <v-list-subheader data-testid="rune-name">Rune {{ rune.name }}</v-list-subheader>
        </v-row>
        <v-row class="align-center">
            <v-col cols="4">
                <v-text-field data-testid="prix-ra" label="Prix Ra" v-model="rune.prixRa" @change="updatePrice"
                    density="compact" hide-details="auto" suffix="K" v-if="rune.prixRa != -1"></v-text-field>
            </v-col>
            <v-col cols="4">
                <v-text-field data-testid="prix-pa" label="Prix Pa" v-model.number="rune.prixPa" @change="updatePrice"
                    density="compact" hide-details="auto" suffix="K" v-if="rune.prixPa != -1"></v-text-field>
            </v-col>
            <v-col cols="4">
                <v-text-field data-testid="prix-ba" label="Prix Ba" v-model.number="rune.prixBa" @change="updatePrice"
                    density="compact" hide-details="auto" suffix="K" v-if="rune.prixBa != -1"></v-text-field>
            </v-col>
        </v-row>
    </div>
</template>

<script lang="ts">
import { createPromiseClient } from "@connectrpc/connect";
import { transport } from '@/transport'
import { RuneType } from '@/types/RuneType';
import { RuneController } from "@/grpc/grpc_market_connect";
import { RuneRequest } from "@/grpc/grpc_market_pb";


const runeClient = createPromiseClient(RuneController, transport);

export default {
    props: {
        rune: {
            type: RuneType,
            required: true
        }
    },
    setup(props) {
        const updatePrice = async () => {
            await runeClient.update(new RuneRequest(props.rune))
        };

        return {
            updatePrice
        };
    }
};
</script>

<style scoped>
.v-row {
    margin: 0px
}
</style>