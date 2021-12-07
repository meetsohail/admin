<template>
    <div>
        <logo-component/>
        <div class="card">
            <div class="card-body p-4 p-sm-5">
                <div class="row text-left justify-content-between align-items-center mb-2">
                    <div class="col-auto">
                        <h5>Log in</h5>
                    </div>
                    <div class="col-auto">
                        <p class="fs--1 text-600 mb-0">or <router-link :to="{name: 'register'}">Create an account</router-link>
                        </p>
                    </div>
                </div>
                <div class="mb-3">
                    <input @keyup.enter="signIn()" class="form-control" :class="{'is-invalid': errors.email}" :disabled="busy" v-model="email" type="email" placeholder="Email address" />
                    <div v-if="errors.email" class="invalid-feedback">
                        {{ errors.email[0] }}
                    </div>
                </div>
                <div class="mb-3">
                    <input @keyup.enter="signIn()" class="form-control" :class="{'is-invalid': errors.password}" :disabled="busy" v-model="password" type="password" placeholder="Password" />
                    <div v-if="errors.password" class="invalid-feedback">
                        {{ errors.password[0] }}
                    </div>
                </div>
                <div class="row flex-between-center">
                    <div class="col-auto">
                        <div class="form-check mb-0">
                            <input class="form-check-input" :disabled="busy" type="checkbox" id="remember-me" checked="checked" />
                            <label class="form-check-label" for="remember-me">Remember me</label>
                        </div>
                    </div>
                    <div class="col-auto">
                        <router-link class="fs--1" :to="{name: 'reset'}">
                            Forgot Password?
                        </router-link>
                    </div>
                </div>
                <div class="mb-3">
                    <button @click="signIn()" :disabled="busy" class="btn btn-primary btn-block mt-3">
                        <span v-if="busy">Signing in...</span>
                        <span v-else>Log in</span>
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
            password: '',
            busy: false,
            errors: false
        }
    },
    methods: {
        signIn() {
            let _this = this;
            _this.busy = true;
            _this.errors = false;
            let fd = new FormData();
            fd.append('email', _this.email);
            fd.append('password', _this.password);
            axios.post('/do-login/', fd).then((res) => {
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