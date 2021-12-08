<template>
    <div class="row">
        <div class="col-lg-12 pr-lg-2">
            <div v-if="saved" class="alert alert-success">Profile settings have been updated.</div>
            <div class="card mb-3">
                <div class="card-header">
                    <h5 class="mb-0">Profile Settings</h5>
                </div>
                <div class="card-body bg-light">
                    <div class="row g-3">
                        <div class="col-lg-6">
                            <label class="form-label" for="first-name">First Name</label>
                            <input :disabled="busy" :class="{'is-invalid': errors.first_name}" class="form-control" v-model="user.first_name" id="first-name" type="text"/>
                            <div class="invalid-feedback" v-if="errors.first_name">{{ errors.first_name[0] }}</div>
                        </div>
                        <div class="col-lg-6">
                            <label class="form-label" for="last-name">Last Name</label>
                            <input :disabled="busy" :class="{'is-invalid': errors.last_name}" class="form-control" id="last-name" type="text" v-model="user.last_name" />
                            <div class="invalid-feedback" v-if="errors.last_name">{{ errors.last_name[0] }}</div>
                        </div>
                        <div class="col-lg-6">
                            <label class="form-label" for="email1">Email</label>
                            <input
                                class="form-control"
                                id="email1"
                                type="text"
                                v-model="user.email"
                                :disabled="busy"
                                :class="{'is-invalid': errors.email}"
                            />
                            <div class="invalid-feedback" v-if="errors.email">{{ errors.email[0] }}</div>
                        </div>
                        <div class="col-lg-6">
                            <label class="form-label" for="password">Password</label>
                            <input :disabled="busy" :class="{'is-invalid': errors.password}" class="form-control" placeholder="Leave blank if you don't want to change." id="password" type="password" autocomplete="new-password" v-model="password" />
                            <div class="invalid-feedback" v-if="errors.password">{{ errors.password[0] }}</div>
                        </div>
                        <div class="col-12 d-flex justify-content-end">
                            <button :disabled="busy" @click="updateProfile()" class="btn btn-black text-white rounded shadow" type="submit">Update</button>
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
            user: {},
            busy: false,
            saved: false,
            errors: {},
            password: ''
        }
    },
    mounted() {
        this.user = this.$store.state.user;
    },
    methods: {
        updateProfile() {
            let _this = this;
            _this.busy = true;
            _this.saved = false;
            _this.errors = {};
            let fd = new FormData();
            fd.append('email', _this.user.email);
            fd.append('first_name', _this.user.first_name);
            fd.append('last_name', _this.user.last_name);
            if(_this.password) {
                fd.append('password', _this.password);
            }
            axios.put(`/users/${_this.user.id}/`, fd).then((res) => {
                _this.busy = false;
                _this.saved = true;
                _this.password = null;
                _this.$store.commit('setUser');
            }).catch((err) => {
                _this.busy = false;
                _this.errors = err.response.data;
            });
        }
    }
};
</script>