<template>
    <div class="row">
        <div class="col-12">
            <div class="card mb-3">
                    <!-- <div class="bg-holder bg-card" style="background-image:url(https://prium.github.io/falcon/v3.5.0/assets/img/icons/spot-illustrations/corner-2.png);"></div> -->

                <div class="bg-primary gradient-dark card-header">
                    <h5 class="text-white">Add Project</h5>
                </div>
                <div class="card-body">
                    <div class="row mt-3">
                        <div class="col-md-8">
                            <div class="form-group">
                                <label for="projectTitle">Project Title</label>
                                <input
                                    :class="{ 'is-invalid': errors.title }"
                                    type="text"
                                    v-model="title"
                                    class="form-control"
                                    id="projectTitle"
                                    placeholder="Set a title for your project"
                                />
                                <p v-if="errors.title" class="invalid-feedback">
                                    {{ errors.title[0] }}
                                </p>
                            </div>
                            <div class="form-group mt-3">
                                <label for="projectUrl"
                                    >Project URL
                                    <small class="text-info">(e.g https://domain.com)</small></label
                                >
                                <input
                                    :class="{ 'is-invalid': errors.url }"
                                    type="text"
                                    v-model="url"
                                    class="form-control"
                                    id="projectTitle"
                                    placeholder="Provide the Domain to track"
                                />
                                <p v-if="errors.url" class="invalid-feedback">
                                    {{ errors.url[0] }}
                                </p>
                            </div>
                            <!-- countries -->
                            <div class="form-group mt-3">
                                <label for="projectUrl">Select Countries</label>
                                <v-select
                                    multiple
                                    v-model="selected"
                                    :options="geos"
                                    @search="onSearch"
                                    placeholder="Select countries"
                                    :class="{'border rounded-lg border-danger': errors.countries}"
                                />
                                <small v-if="errors.countries" class="text-danger">
                                    {{ errors.countries[0] }}
                                </small>
                            </div>
                            <!-- /countries -->
                            <!-- Devices -->
                            <div class="form-group mt-3">
                                <label for="projectUrl">Select Device</label>
                                <select
                                    v-model="selected_devices"
                                    placeholder="Select Devices"
                                    class="form-control"
                                    :class="{'border rounded-lg border-danger': errors.device}"
                                >
                                <option value="desktop">Desktop</option>
                                <option value="mobile">Mobile</option>
                                <option value="both">Both</option>
                                </select>
                                <small v-if="errors.device" class="text-danger">
                                    {{ errors.device[0] }}
                                </small>
                            </div>
                            <!-- /Devices -->
                        </div>
                    </div>
                    <div class="row mt-3">
                        <div class="col-md-8">
                            <div class="form-group" >
                                <button
                                    @click="addProject()"
                                    :disabled="adding"
                                    class="btn btn-black text-white rounded"
                                   
                                >
                                    Save
                                </button>
                                <router-link
                                    :to="{ name: 'dashboard' }"
                                    class="btn btn-orange text-white rounded"
                                   
                                >
                                    Cancel
                                </router-link>
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
            adding: false,
            errors: {},
            geography: "US",
            title: "",
            url: "",
            selected: [],
            geos: [],
            no_of_countries: 5,
            selected_devices:'desktop',
        };
    },
    mounted() {
        // get countries
        axios
            .get(`/data/countries/`)
            .then((response) => {
                this.geos = response.data.results;
                console.log(this.geos);
            })
            .catch((error) => console.log(error));
    },
    methods: {
        addProject() {
            let _this = this;
            if (_this.adding) {
                return;
            }
            _this.errors = {};
            _this.adding = true;
            var countries = [];
            for(var i = 0; i < _this.selected.length; i++) {
                countries.push(_this.selected[i].id);
            }
            let fd = {
                title: _this.title,
                user: _this.$store.state.user.id,
                url: _this.url,
                countries: countries,
                device: _this.selected_devices
            };
            axios
                .post("/data/projects/", fd)
                .then((res) => {
                    _this.$router.push({ name: "dashboard" });
                    toastr.success("Your project has been added.");
                    _this.$store.commit("setUser");
                    _this.adding = false;
                })
                .catch((err) => {
                    _this.adding = false;
                    if (err.response && err.response.data) {
                        _this.errors = err.response.data;
                        if (_this.errors.detail) {
                            toastr.error(_this.errors.detail);
                        }
                        if (_this.errors.non_field_errors) {
                            for (
                                var i = 0;
                                i < _this.errors.non_field_errors.length;
                                i++
                            ) {
                                toastr.error(_this.errors.non_field_errors[i]);
                            }
                        }
                    } else {
                        toastr.error("Something went wrong. Please try again.");
                    }
                });
        },

        onSearch(search, loading) {
            let _this = this;
            if (search.length) {
                loading(true);
                this.search(loading, search, _this);
            }
        },

        search: _.debounce((loading, search, vm) => {
            fetch(`/api/data/countries/?q=${escape(search)}`).then((res) => {
                res.json().then((json) => {
                    if (json.results.length > 0) {
                        vm.geos = json.results;
                    }
                });
                loading(false);
            });
        }, 1000),
    },
    watch: {
        selected(oldval, newval) {
            console.log(newval);
        }
    }
};
</script>
