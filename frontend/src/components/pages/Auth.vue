<template>
    <v-container grid-list-md>
        <v-layout row wrap align-center justify-center fill-height>
            <v-flex xs12 sm8 lg4 md5>
                <v-card class="login-card">
                    <v-card-title>
                        <span class="headline">Login to Movies</span>
                    </v-card-title>

                    <v-spacer />

                    <v-card-text>

                        <v-layout row fill-height justify-center align-center v-if="loading">
                            <v-progress-circular :size="50" color="primary" indeterminate />
                        </v-layout>


                        <v-form v-else ref="form" v-model="valid" lazy-validation>
                            <v-container>

                                <v-text-field v-model="credentials.username" :counter="70" label="email address"
                                    maxlength="70" required />

                                <v-text-field type="password" v-model="credentials.password" :counter="20" label="password"
                                    maxlength="20" required />

                            </v-container>
                            <v-btn class="pink white--text" :disabled="!valid" @click="login">Login</v-btn>

                        </v-form>


                    </v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
export default {
    name: 'Auth',
    data: () => ({
        credentials: {},
        valid: true,
        loading: false
    }),
    methods: {
        login() {

        }
    }
}
</script>