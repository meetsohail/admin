<template>
    <div class="container-fluid">
        <div class="row justify-content-center">
          <div class="col-12 col-lg-10 col-xl-8">

            <!-- Header -->
            <div class="header mt-md-5">
              <div class="header-body">
                <div class="row align-items-center">
                  <div class="col">

                    <!-- Pretitle -->
                    <h6 class="header-pretitle">
                      Overview
                    </h6>

                    <!-- Title -->
                    <h1 class="header-title">
                      Account
                    </h1>

                  </div>
                </div> <!-- / .row -->
              <accounts-topbar></accounts-topbar>
              </div>
            </div>

            <!-- Form -->
            <form>

              <div class="row justify-content-between align-items-center">
                <div class="col">
                  <div class="row align-items-center">
                    <div class="col-auto">

                      <!-- Avatar -->
                      <div class="avatar">
                        <img class="avatar-img rounded-circle" :src="user.avatar_url" alt="...">
                      </div>

                    </div>
                    <div class="col ms-n2">

                      <!-- Heading -->
                      <h4 class="mb-1">
                        Your avatar
                      </h4>

                      <!-- Text -->
                      <small class="text-muted">
                        You can change your profile from gravatar againt the provided email
                      </small>

                    </div>
                  </div> <!-- / .row -->
                </div>
                <div class="col-auto">

                

                </div>
              </div> <!-- / .row -->

              <!-- Divider -->
              <hr class="my-5">

              <div class="row">
                <div class="col-12 col-md-6">

                  <!-- First name -->
                  <div class="form-group">

                    <!-- Label -->
                    <label class="form-label">
                      First name
                    </label>

                    <!-- Input -->
                   <input :disabled="busy" :class="{'is-invalid': errors.first_name}" class="form-control" v-model="user.first_name" id="first-name" type="text"/>
                   <div class="invalid-feedback" v-if="errors.first_name">{{ errors.first_name[0] }}</div>

                  </div>

                </div>
                <div class="col-12 col-md-6">

                  <!-- Last name -->
                  <div class="form-group">

                    <!-- Label -->
                    <label class="form-label">
                      Last name
                    </label>

                    <!-- Input -->
                   <input :disabled="busy" :class="{'is-invalid': errors.last_name}" class="form-control" id="last-name" type="text" v-model="user.last_name" />
                            <div class="invalid-feedback" v-if="errors.last_name">{{ errors.last_name[0] }}</div>

                  </div>

                </div>
                <div class="col-6">

                  <!-- Email address -->
                  <div class="form-group">

                    <!-- Label -->
                    <label class="mb-1">
                      Email address
                    </label>

                

                    <!-- Input -->
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

                </div>
                <div class="col-6 col-md-6">

                  <!-- Phone -->
                  <div class="form-group">

                    <!-- Label -->
                    <label class="form-label">
                      Password
                    </label>

                    <!-- Input -->
                    <input :disabled="busy" :class="{'is-invalid': errors.password}" class="form-control" placeholder="Leave blank if you don't want to change." id="password" type="password" autocomplete="new-password" v-model="password" />
                            <div class="invalid-feedback" v-if="errors.password">{{ errors.password[0] }}</div>

                  </div>

                </div>
                
              </div> <!-- / .row -->

              <!-- Button -->
              <button :disabled="busy" @click="updateProfile()" class="btn btn-primary">
                Save changes
              </button>

              <!-- Divider -->
              <hr class="my-5">

            </form>

            <br><br>

          </div>
        </div> <!-- / .row -->
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