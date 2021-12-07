<template>
  <div>
    <div class="row no-gutters">
      <div class="row">
        <div class="col-12">
          <div class="card mb-3">
            <div class="card-header">
              <div class="row justify-content-between">
                <div class="col-md-auto">
                  <h5 class="my-1 mb-md-0">Manage Products</h5>
                </div>
                <div class="col-md-auto d-flex">
                  <router-link
                    class="btn btn-orange btn-secondary text-white rounded shadow"
                    style="width: 100%"
                    :to="{ name: 'add_product' }"
                  >
                    Add Product
                  </router-link>
                </div>

                <!-- <input
                        v-model="search"
                        @keyup.enter="getProducts()"
                        type="text"
                        class="form-control-sm col-md-6 col-sm-12"
                        placeholder="Search products..."
                      /> -->
              </div>
              <!-- <div class="col-md-6 col-sm-6 d-flex align-items-center pr-0">
                <router-link class="btn btn-black text-white mx-2 btn-sm" :to="{name: 'add_product'}"> Add Product</router-link>
              </div> -->
            </div>

            <div class="card-body px-0 pt-0">
              <div v-if="busy" class="row g-0 p-4 text-center">
                <loading-component
                  :busy="busy"
                  nText
                  bText="Loading products..."
                ></loading-component>
              </div>
              <div v-else>
                <div
                  v-if="!products || products.count == 0"
                  class="row g-0 pt-4 text-center"
                >
                  <h3 class="text-center text-muted">No products found!</h3>
                </div>
                <div v-else class="row g-0">
                  <div class="table-responsive">
                    <table class="table">
                      <thead class="text-white gradient-dark shadow">
                        <tr>
                          <th>Product Name</th>

                          <th>Price</th>
                          <th>StripeID</th>
                          <th>Featured</th>
                          <th colspan="2">Status</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr
                          v-for="product in products.results"
                          :key="product.id"
                        >
                          <td>{{ product.product_name }}</td>

                          <td>{{ product.product_price | toCurrency }}</td>
                          <td>{{ product.product_stripe_id }}</td>
                          <td v-if="product.featured == true">
                            <i class="fas fa-check-circle text-primary"></i>
                          </td>
                          <td v-else>
                            <i class="fas fa-times-circle text-danger"></i>
                          </td>
                          <td v-if="product.product_status == true">
                            <i class="fas fa-check-circle text-primary"></i>
                          </td>
                          <td v-else>
                            <i class="fas fa-times-circle text-danger"></i>
                          </td>
                          <!-- /featured -->
                          <!--<td>{{ product.created_at }}</td>-->
                          <td class="text-right">
                            <router-link
                              :to="{
                                name: 'updateproduct',
                                params: { id: product.id },
                              }"
                              class="btn btn-black text-white"
                            >
                              <i class="fas fa-edit small"></i>
                            </router-link>
                            <a
                              href="#"
                              class="btn gradient-danger text-white"
                              @click="deleteProduct(product.id)"
                            >
                              <i class="fas fa-trash small"></i>
                            </a>
                            <br />
                            <a
                              href="#"
                              v-if="delbtn && pid == product.id"
                              @click="deleteCofirm(product.id)"
                              class="badge badge-soft-danger small mt-3"
                              >Confirm?</a
                            >
                            <a
                              href="#"
                              v-if="delbtn && pid == product.id"
                              @click="deleteCancel()"
                              class="badge badge-soft-info small"
                              >Cancel?</a
                            >
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
            <div class="card-footer bg-light text-right">
              <button
                :disabled="!previous_offset"
                @click="(offset = previous_offset), getProducts()"
                class="btn btn-falcon-default"
              >
                Previous
              </button>
              <button
                :disabled="next_offset == false"
                @click="(offset = next_offset), getProducts()"
                class="btn btn-falcon-default"
              >
                Next
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
  props: ["pagination"],
  data() {
    return {
      products: {},
      busy: false,
      next_offset: false,
      previous_offset: false,
      offset: "",
      limit: 10,
      order_by: "-pk",
      search: "",
      delbtn: false,
      pid: "",
    };
  },
  mounted() {
    docReady(tooltipInit);
    let _this = this;
    _this.getProducts();
  },
  methods: {
    deleteProduct(prod_id) {
      let _this = this;
      _this.delbtn = true;
      _this.pid = prod_id;
    },
    deleteCancel() {
      let _this = this;
      _this.delbtn = false;
    },
    deleteCofirm(product_id) {
      let _this = this;
      _this.busy = true;
      axios
        .delete(`/billing/${product_id}`)
        .then((res) => {
          _this.busy = false;
          _this.getProducts();
        })
        .catch((err) => {
          _this.busy = false;
          _this.products = false;
        });
    },
    getParameterByName(url, name) {
      var match = RegExp("[?&]" + name + "=([^&]*)").exec(url);
      return match && decodeURIComponent(match[1].replace(/\+/g, " "));
    },
    getProducts() {
      let _this = this;
      _this.busy = true;
      axios
        .get(
          `/billing/?limit=${_this.limit}&offset=${_this.offset}&order_by=${_this.order_by}&search=${_this.search}`
        )
        .then((res) => {
          _this.products = res.data;
          if (res.data.next) {
            _this.next_offset = _this.getParameterByName(
              res.data.next,
              "offset"
            );
          } else {
            _this.next_offset = false;
          }
          if (res.data.previous) {
            let prev_offset = _this.getParameterByName(
              res.data.previous,
              "offset"
            );
            if (!prev_offset) {
              prev_offset = "0";
            }
            _this.previous_offset = prev_offset;
          } else {
            _this.previous_offset = false;
          }
          _this.busy = false;
        })
        .catch((err) => {
          _this.busy = false;
          _this.products = false;
        });
    },
    orderProductsBy(order_by) {
      let _this = this;
      if (order_by == _this.order_by) {
        _this.order_by = `-${order_by}`;
      } else {
        _this.order_by = order_by;
      }
      _this.offset = "";
      _this.getProducts();
    },
  },
  watch: {
    busy(oldVal, newVal) {
      docReady(tooltipInit);
    },
  },
};
</script>
