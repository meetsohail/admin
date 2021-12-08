<template>
    <div class="container-fluid">
        <!-- Header -->
        <div class="header">
            <div class="header-body">
                <div class="row align-items-center">
                    <div class="col">
    
                        <!-- Pretitle -->
                        <h6 class="header-pretitle">
                            Overview
                        </h6>
    
                        <!-- Title -->
                        <h1 class="header-title text-truncate">
                            User Stats
                        </h1>
    
                    </div>
                  
                </div>
                <!-- / .row -->
            </div>
        </div>
        <div v-if="user != []" class="row align-items-center">
            <div class="col-lg-12 pr-lg-2">
                <div class="card mb-3">
                    <div class="card-header">
                        <h5 class="mb-0">
                            
                            <span v-if="user.email"> {{ user.email }}</span>
                        </h5>
                    </div>
                    <div class="card-body bg-light">
                        <div class="table-responsive">
                            <table class="table table-striped">
                                <tbody>
                                    <tr>
                                        <td style="width:30%;">All-time Calls</td>
                                        <td>{{ user.alltime_calls|toNumber }}</td>
                                    </tr>
                                    <tr>
                                        <td>Monthly Calls</td>
                                        <td>{{ user.monthly_calls|toNumber }}</td>
                                    </tr>
                                    <tr>
                                        <td>Total Bulk Jobs</td>
                                        <!-- <td>{{ user.statistics.jobs.total|toNumber }}</td> -->
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
                <div class="card mb-3">
                    <div class="card-header">
                        <h5 class="mb-0">Add Credits</h5>
                    </div>
                    <div class="card-body bg-light">
                        <div class="row g-3">
                            <div class="col-lg-12">
                                <div class="form-group">
                                    <label class="form-label" for="credit">Credits<span>
                        ({{ user.credit | toNumber }})</span
                      ></label
                    >
                    <input
                      :class="{ 'is-invalid': errors.credit }"
                      class="form-control form-control-lg"
                      v-model="credit"
                      placeholder="Enter credits amount, i.e. 1000"
                      id="credit"
                      type="text"
                    />
                    <div class="invalid-feedback" v-if="errors.credit">
                      {{ errors.credit[0] }}
                    </div>
                  </div>
                </div>
                <div class="col-12 d-flex">
                  <button
                    v-if="!update_user"
                    :disabled="busy"
                    @click="update_user = true"
                    class="btn btn-primary"
                  >
                    Add Credits
                  </button>
                  <button
                    v-if="update_user"
                    :disabled="busy"
                    @click="update_user = false"
                    class="btn btn-success mr-1"
                  >
                    Cancel
                  </button>
                  <button
                    v-if="update_user"
                    :disabled="busy"
                    @click="updateUser()"
                    class="btn btn-danger"
                  >
                    Confirm
                  </button>
                </div>
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
            user: [],
            credit: '',
            saved: false,
            errors: [],
            busy: false,
            update_user: false,
        };
    },
    mounted() {
        this.getUser();
    },
    methods: {
        getUser() {
            let _this = this;
            axios
                .get(`/users/${_this.$route.params.id}/`)
                .then((res) => {
                    _this.user = res.data;
                    console.log(_this.user)
                })
                .catch((err) => {});
        },
        updateUser() {
            let _this = this;
            _this.busy = true;
            let fd = new FormData();
            fd.append("credit", _this.credit);
            fd.append("has_api_access", _this.user.has_api_access);
            fd.append("rate_limiting_value", _this.user.rate_limiting_value);
            if (_this.user.cust_price) {
                fd.append("cust_price", _this.user.cust_price);
            }
            axios
                .post(`/users/${_this.$route.params.id}/update-settings/`, fd)
                .then((res) => {
                    toastr.success("User settings have been updated.");
                    _this.busy = false;
                    _this.credit = 0;
                    _this.update_user = false;
                    _this.getUser();
                    if (_this.user.id == _this.$store.state.user.id) {
                        _this.$store.commit("setUser");
                    }
                })
                .catch((err) => {
                    _this.busy = false;
                    toastr.error("User settings cannot be updated.");
                });
        },
    },
};
</script>
