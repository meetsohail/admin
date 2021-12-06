<template>
    <div class="row">
        <div class="col-lg-12 pr-lg-2">
            <div v-if="saved" class="alert alert-success">API key has been regenerated.</div>
            <div v-if="reset_key" class="alert alert-warning">Once reset, the current API key will stop working and your applications may break until you will update your new API key there. Are you sure that you want to reset it?</div>
            <div class="card mb-3">
                <div class="card-header">
                    <h5 class="mb-0">API Keys</h5>
                </div>
                <div class="card-body bg-light">
                    <div class="row g-3">
                        <div class="col-lg-12">
                            <label class="form-label" for="api-key">API Key</label>
                            <input :class="{'is-invalid': errors.api_key}" readonly class="form-control form-control-lg" v-model="api_key" id="api-key" type="text"/>
                            <div class="invalid-feedback" v-if="errors.api_key">{{ errors.api_key[0] }}</div>
                        </div>
                        <div class="col-12 d-flex">
                            <button v-if="!reset_key" :disabled="busy" @click="reset_key=true" class="btn btn-primary">Reset API Key</button>
                            <button v-if="reset_key" :disabled="busy" @click="reset_key=false" class="btn btn-success mr-1">Cancel</button>
                            <button v-if="reset_key" :disabled="busy" @click="resetApiKey()" class="btn btn-danger">Confirm</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            api_key: '',
            saved: false,
            errors: [],
            busy: false,
            reset_key: false
        }
    },
    mounted() {
        this.getApiKey();
    },
    methods: {
        getApiKey() {
            let _this = this;
            axios.get('/users/api-key/').then((res) => {
                _this.api_key = res.data.api_key;
            }).catch((err) => {

            });
        },
        resetApiKey() {
            let _this = this;
            _this.busy = true;
            axios.post('/users/reset-api-key/').then((res) => {
                _this.api_key = res.data.api_key;
                toastr.success('Your API key has been reset.');
                _this.busy = false;
                _this.reset_key = false;
            }).catch((err) => {
                _this.busy = false;
                toastr.error('API token cannot be reset.');
            });
        }
    }
}
</script>
