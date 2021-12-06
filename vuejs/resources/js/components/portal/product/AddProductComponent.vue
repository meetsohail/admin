<template>
  <div class="row">
    <div class="col-lg-12 pr-lg-2">
      <div
        v-if="saved && $route.name == 'add_product'"
        class="alert alert-success"
      >
        Billing settings have been Created.
      </div>
      <div
        v-if="saved && $route.name == 'updateproduct'"
        class="alert alert-success"
      >
        Billing settings have been Updated.
      </div>
      <div class="card mb-3">
        <div class="card-header">
          <h5 class="mb-0">Add New Product</h5>
        </div>
        <div class="card-body bg-light">
          <div class="row g-3">
            <div class="col-lg-6">
              <label class="form-label" for="first-name">Product Name</label>
              <input
                :disabled="busy"
                :class="{ 'is-invalid': errors.product_name }"
                class="form-control"
                v-model="product.product_name"
                id="first-name"
                type="text"
              />
              <div class="invalid-feedback" v-if="errors.product_name">
                {{ errors.product_name[0] }}
              </div>
            </div>
            <div class="col-lg-6">
              <label class="form-label" for="email1">Product Price</label>
              <input
                class="form-control"
                id="product_price"
                type="number"
                v-model="product.product_price"
                :disabled="busy"
                :class="{ 'is-invalid': errors.product_price }"
              />
              <div class="invalid-feedback" v-if="errors.product_price">
                {{ errors.product_price[0] }}
              </div>
            </div>
            <div class="col-lg-6">
              <label class="form-label" for="email1">Max Keywords</label>
              <input
                class="form-control"
                id="max_keywords"
                type="number"
                v-model="product.max_keywords"
                :disabled="busy"
                :class="{ 'is-invalid': errors.max_keywords }"
              />
              <div class="invalid-feedback" v-if="errors.max_keywords">
                {{ errors.max_keywords[0] }}
              </div>
            </div>
            <div class="col-lg-6">
              <label class="form-label" for="email1">Max Results</label>
              <input
                class="form-control"
                id="max_results"
                type="number"
                v-model="product.max_results"
                :disabled="busy"
                :class="{ 'is-invalid': errors.max_results }"
              />
              <div class="invalid-feedback" v-if="errors.max_results">
                {{ errors.max_results[0] }}
              </div>
            </div>
            <div class="col-lg-6">
              <label class="form-label" for="email1">Check Interval</label>
              <select
                class="form-control"
                v-model="product.check_interval"
                :disabled="busy"
                :class="{ 'is-invalid': errors.check_interval }"
              >
                <option value="hourly">Hourly</option>
                <option value="daily">Daily</option>
                <option value="weekly">Weekly</option>
                <option value="monthly">Monthly</option>
              </select>

              <div class="invalid-feedback" v-if="errors.check_interval">
                {{ errors.check_interval[0] }}
              </div>
            </div>
            <div class="col-lg-6">
              <label class="form-label" for="email1">Realtim Check</label>
              <input
                class="form-control"
                id="realtime_checks"
                type="number"
                v-model="product.realtime_checks"
                :disabled="busy"
                :class="{ 'is-invalid': errors.realtime_checks }"
              />
              <div class="invalid-feedback" v-if="errors.realtime_checks">
                {{ errors.realtime_checks[0] }}
              </div>
            </div>
            <div class="col-lg-12">
              <label class="form-label" for="last-name"
                >Product Description</label
              >
              <textarea
                :disabled="busy"
                :class="{ 'is-invalid': errors.product_description }"
                class="form-control"
                id="last-name"
                type="text"
                v-model="product.product_description"
              ></textarea>
              <div class="invalid-feedback" v-if="errors.product_description">
                {{ errors.product_description[0] }}
              </div>
            </div>
            <div class="col-lg-6">
              <label class="form-label" for="first-name"
                >Product Stripe ID</label
              >
              <input
                :disabled="busy"
                :class="{ 'is-invalid': errors.product_stripe_id }"
                class="form-control"
                v-model="product.product_stripe_id"
                id="product_stripe_price_id"
                type="text"
              />
              <div class="invalid-feedback" v-if="errors.product_stripe_id">
                {{ errors.product_stripe_id[0] }}
              </div>
            </div>
            <div class="col-lg-6">
              <label class="form-label" for="email1"
                >Product Price Stripe ID</label
              >
              <input
                class="form-control"
                id="product_stripe_price_id"
                type="text"
                v-model="product.product_stripe_price_id"
                :disabled="busy"
                :class="{ 'is-invalid': errors.product_stripe_price_id }"
              />
              <div
                class="invalid-feedback"
                v-if="errors.product_stripe_price_id"
              >
                {{ errors.product_stripe_price_id[0] }}
              </div>
            </div>
            <div class="col-lg-12 mt-0">
              <small class="text-muted"
                >If you already have created product and price in Stripe just
                copy and paste product and price ID. Otherwise it will create by
                own on stripe.</small
              >
            </div>

            <div class="col-lg-12">
              <div class="form-check form-switch">
                <input
                  class="form-check-input"
                  id="flexSwitchCheckDefault"
                  type="checkbox"
                  :disabled="busy"
                  :class="{ 'is-invalid': errors.product_status }"
                  v-model="product.product_status"
                />
                <label class="form-check-label" for="flexSwitchCheckDefault"
                  >Product Status (<span class="ml-1 small">Active/Hold</span
                  >)</label
                >
              </div>

              <!-- <label class="form-label" for="last-name">Product Status (<span class="ml-1 small">Active/Hold</span>)</label> -->

              <!-- <div class="checkbox-inline">
                            <input type="checkbox" :disabled="busy" :class="{'is-invalid': errors.product_status}" class="form-check-input float-left" id="status" v-model="product.product_status" />
                             </div> -->
              <div class="invalid-feedback" v-if="errors.product_status">
                {{ errors.product_status[0] }}
              </div>
            </div>
            <div class="col-lg-12">
              <div class="form-check form-switch">
                <input
                  class="form-check-input"
                  id="productFeatured"
                  type="checkbox"
                  v-model="product.featured"
                />
                <label class="form-check-label" for="productFeatured"
                  >Product Featured
                </label>
                <div class="block invalid-feedback" v-if="errors.featured">
                  {{ errors.featured[0] }}
                </div>
              </div>

              <!-- <label class="form-label" for="last-name">Product Featured </label> -->
              <!-- <div class="checkbox-inline">
                            <input type="checkbox"  :disabled="busy" :class="{'is-invalid': errors.featured}" class="form-check-input float-left" v-model="product.featured" />
                            
                            <div class="block invalid-feedback" v-if="errors.featured">{{ errors.featured[0] }}</div>
                             </div> -->
            </div>
            <div class="col-12 d-flex justify-content-end">
              <button
                v-if="$route.name == 'add_product'"
                :disabled="busy"
                @click="createProduct()"
                class="btn rounded shadow btn-black text-white"
                type="submit"
              >
                Add New
                <div
                  v-if="busy"
                  class="spinner-border text-light spinner-border-sm"
                  role="status"
                ></div>
              </button>
              <button
                v-if="$route.name == 'updateproduct'"
                :disabled="busy"
                @click="updateProduct()"
                class="btn rounded shadow btn-black text-white"
                type="submit"
              >
                Update
                <div
                  v-if="busy"
                  class="spinner-border text-light spinner-border-sm"
                  role="status"
                ></div>
              </button>
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
      product: {
        product_stripe_id: "",
        product_stripe_price_id: "",
        featured: false,
        product_name: "",
        product_price: 0,
        product_status: false,
        product_description: "",
        max_results: 0,
        max_keywords: 0,
        realtime_checks: 0,
        check_interval: "hourly",
      },
      busy: false,
      saved: false,
      errors: {},
      product_id: "",
    };
  },
  mounted() {
    this.product_id = this.$route.params.id;
    if (this.$route.name == "updateproduct") {
      this.getProduct();
    }
  },
  methods: {
    getProduct() {
      let _this = this;
      _this.busy = true;
      _this.saved = false;
      _this.errors = {};

      axios
        .get(`/billing/${_this.product_id}`)
        .then((res) => {
          _this.busy = false;
          console.log(res);
          _this.product = res.data;
        })
        .catch((err) => {
          _this.busy = false;
          _this.errors = err.response.data;
        });
    },
    createProduct() {
      let _this = this;
      _this.busy = true;
      _this.saved = false;
      _this.errors = {};
      console.log(_this.product.featured);
      let fd = new FormData();
      fd.append("product_name", _this.product.product_name);
      fd.append("product_description", _this.product.product_description);
      fd.append("product_price", _this.product.product_price);
      fd.append("product_status", _this.product.product_status);
      fd.append("product_stripe_id", _this.product.product_stripe_id);
      fd.append(
        "product_stripe_price_id",
        _this.product.product_stripe_price_id
      );
      fd.append("featured", _this.product.featured);
      fd.append("max_keywords", _this.product.max_keywords);
      fd.append("max_results", _this.product.max_results);
      fd.append("check_interval", _this.product.check_interval);
      fd.append("realtime_checks", _this.product.realtime_checks);
      fd.append("countries", [1]);

      // axios.put(`/products/${_this.product.id}/`, fd).then((res) => {
      axios
        .post(`/billing/`, fd)
        .then((res) => {
          _this.busy = false;
          // _this.saved = true;
          toastr.success("Product has been added successfully!");
          setTimeout(function () {
            _this.$router.push("/products");
          }, 1500);
        })
        .catch((err) => {
          _this.busy = false;
          // toastr.error(err.response.data);
          _this.errors = err.response.data;
        });
    },
    updateProduct() {
      let _this = this;
      _this.busy = true;
      _this.saved = false;
      _this.errors = {};
      let fd = new FormData();
      fd.append("product_name", _this.product.product_name);
      fd.append("product_description", _this.product.product_description);
      fd.append("product_price", _this.product.product_price);
      fd.append("product_stripe_id", _this.product.product_stripe_id);
      fd.append(
        "product_stripe_price_id",
        _this.product.product_stripe_price_id
      );
      fd.append("featured", _this.product.featured);
      fd.append("credit_rate", _this.product.credit_rate);
      fd.append("max_keywords", _this.product.max_keywords);
      fd.append("max_results", _this.product.max_results);
      fd.append("check_interval", _this.product.check_interval);
      fd.append("realtime_checks", _this.product.realtime_checks);

      if (_this.product.product_status == true) {
        fd.append("product_status", 1);
      } else {
        fd.append("product_status", 0);
      }
      axios
        .put(`/billing/${_this.product.id}/`, fd)
        .then((res) => {
          setTimeout(function () {
            toastr.success("Product has been updated successfully!");
          }, 500);
          _this.busy = false;

          setTimeout(function () {
            _this.$router.push("/products");
          }, 1500);
        })
        .catch((err) => {
          _this.busy = false;
          _this.errors = err.response.data;
        });
    },
  },
};
</script>
<style scoped>
  input:focus, textarea:focus {
    outline: none!important;
    box-shadow: none;
  }
</style>