<template>
    <div>
        <logo-component/>
        <div class="card">
            <div class="card-body p-4 p-sm-5">
                <div class="row text-left justify-content-between align-items-center mb-2">
                    <div class="col-auto">
                        <h5>Reset password</h5>
                    </div>
                    <div class="col-auto">
                        <p class="fs--1 text-600 mb-0">or <router-link :to="{name: 'login'}">Back to login</router-link>
                        </p>
                    </div>
                </div>
                <div v-if="sent" class="alert alert-success">
                    A password reset link has been sent!
                </div>
                <div class="mb-3">
                    <input class="form-control" :class="{'is-invalid': errors.email}" :disabled="busy" v-model="email" type="email" placeholder="Email address" />
                    <div v-if="errors.email" class="invalid-feedback">
                        {{ errors.email[0] }}
                    </div>
                </div>
                <div class="mb-3">
                    <button @click="resetPassword()" :disabled="busy" class="btn btn-primary btn-block mt-3">
                        <span v-if="busy">Sending email...</span>
                        <span v-else>Reset password</span>
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
            busy: false,
            errors: false,
            sent: false
        }
    },
    methods: {
        resetPassword() {
            let _this = this;
            _this.busy = true;
            _this.errors = false;
            _this.sent = false;
            let fd = new FormData();
            fd.append('email', _this.email);
            axios.post('/do-reset-password/', fd).then((res) => {
                _this.busy = false;
                _this.email = '';
                _this.sent = true;
            }).catch((err) => {
                _this.errors = err.response.data.errors;
                _this.busy = false;
            });
        }
    }
}
</script>