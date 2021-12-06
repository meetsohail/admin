<template>
    <div>
        <logo-component/>
        <div class="card">
            <div class="card-body p-4 p-sm-5">
                <div class="row text-left justify-content-between align-items-center mb-2">
                    <div class="col-auto">
                        <h5>Set a new password</h5>
                    </div>
                    <div class="col-auto">
                        <p class="fs--1 text-600 mb-0">or <router-link :to="{name: 'login'}">Sign in</router-link>
                        </p>
                    </div>
                </div>
                <div class="mb-3">
                    <input class="form-control" autocomplete="new-password" :class="{'is-invalid': errors.new_password1}" :disabled="busy" v-model="password" type="password" placeholder="Password" />
                    <div v-if="errors.new_password1" class="invalid-feedback">
                        {{ errors.new_password1[0] }}
                    </div>
                </div>
                <div class="mb-3">
                    <input class="form-control" :class="{'is-invalid': errors.new_password2}" :disabled="busy" v-model="confirm_password" type="password" placeholder="Confirm password" />
                    <div v-if="errors.new_password2" class="invalid-feedback">
                        {{ errors.new_password2[0] }}
                    </div>
                </div>
                <div class="mb-3">
                    <button @click="setPassword()" :disabled="busy" class="btn btn-primary btn-block mt-3">
                        <span v-if="busy">Resetting password...</span>
                        <span v-else>Set new password</span>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import LogoComponent from './partials/LogoComponent';
export default {
    components: {
        LogoComponent
    },
    data() {
        return {
            email: '',
            token: '',
            password: '',
            confirm_password: '',
            busy: false,
            errors: false
        }
    },
    mounted() {
        this.email = this.$route.query.email;
        this.token = this.$route.query.token;
    },
    methods: {
        setPassword() {
            let _this = this;
            _this.busy = true;
            _this.errors = false;
            let fd = new FormData();
            fd.append('new_password1', _this.password);
            fd.append('new_password2', _this.confirm_password);
            fd.append('email', _this.email);
            fd.append('token', _this.token);
            axios.post('/do-update-password/', fd).then((res) => {
                _this.busy = false;
                window.location = '';
            }).catch((err) => {
                _this.errors = err.response.data.errors;
                _this.busy = false;
            });
        }
    }
}
</script>