<template>
  <div class="container-fluid">
        <div class="row justify-content-center" v-if="$store.state.user">
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

            <!-- Alert -->
            <div class="alert alert-danger">
              <i class="fe fe-info me-1"></i> You are near your API limits.
            </div>

            <div class="row">
              <div class="col-12 col-md-6">

                <!-- Card -->
                <div class="card">
                  <div class="card-body">
                    <div class="row align-items-center">
                      <div class="col">

                        <!-- Title -->
                        <h6 class="text-uppercase text-muted mb-2">
                          Current plan
                        </h6>

                        <!-- Heading -->
                        <span class="h2 mb-0">
                          $29/mo
                        </span>

                      </div>
                      <div class="col-auto">

                        <!-- Icon -->
                        <a class="btn btn-sm btn-primary" href="pricing.html">Upgrade</a>

                      </div>
                    </div> <!-- / .row -->

                  </div>
                </div>

              </div>
              <div class="col-12 col-md-6">

                <!-- Card -->
                <div class="card">
                  <div class="card-body">
                    <div class="row align-items-center">
                      <div class="col">

                        <!-- Title -->
                        <h6 class="text-uppercase text-muted mb-2">
                          API usage <i class="fe fe-info" data-bs-toggle="tooltip" data-title="Your limits renew on May 1, 2020"></i>
                        </h6>

                        <!-- Heading -->
                        <span class="h2 mb-0">
                          7,500 of 10,000
                        </span>

                      </div>
                      <div class="col-auto">

                        <!-- Chart -->
                        <div class="chart chart-sparkline">
                          <canvas class="chart-canvas" id="sparklineChart"></canvas>
                        </div>

                      </div>
                    </div> <!-- / .row -->

                  </div>
                </div>

              </div>
            </div>

            <!-- Card -->
            <div class="card">
              <div class="card-header">
                <div class="row align-items-center">
                  <div class="col">

                    <!-- Title -->
                    <h4 class="card-header-title">
                      <span v-if="!$store.state.user.stripe_last4">Add Card</span>
                      <span v-else>Update Card</span> 
                    </h4>

                  </div>
                  <div class="col-auto">

                    <!-- Button -->
                    <span class="badge badge-primary">
                      <small
                class="text-white border border-light p-1 rounded"
                v-if="
                  $store.state.user.stripe_last4 &&
                  $store.state.user.card_brand &&
                  !delmethod
                "
                ><span class="font-weight-bold font-italic">{{
                  $store.state.user.card_brand.toUpperCase()
                }}</span>
                ****{{ $store.state.user.stripe_last4 }}
                <a
                  @click="delmethod = true"
                  class="text-light px-2"
                  href="javascript:void(0)"
                  ><i class="fas fa-times-circle"></i></a
              ></small>
                    </span>

                  </div>
                </div>
              </div>
              <div class="card-body">
                  <div class="row g-3">
            <div class="col-md-12">
              <card
                ref="card"
                :disabled="busy"
                class="form-control stripe-card"
                :class="{ complete }"
                :stripe="stripePubKey"
                @change="complete = $event.complete"
              />
              
            </div>
          </div>
          
              </div>
              <div class="card-footer">
               <div class="row">
            <div class="col-12 d-flex justify-content-end">
              <button
                :disabled="busy"
                @click="updateBillingInfo()"
                class="btn btn-dark btn-sm rounded text-white"
                type="submit"
              >
                <loading-component :busy="busy"></loading-component>
              </button>
            </div>
          </div>
              </div>
            </div>
            <!-- Card -->
            <div class="card">
              <div class="card-header">

                <!-- Title -->
                <h4 class="card-header-title">
                  Invoices
                </h4>

              </div>
              <div class="table-responsive">
                <table class="table table-sm table-nowrap card-table">
                  <thead>
                    <tr>
                      <th>Invoice ID</th>
                      <th>Date</th>
                      <th>Amount</th>
                      <th>Status</th>
                    </tr>
                  </thead>
                  <tbody class="fs-base">
                    <tr>
                      <td>
                        <a href="invoice.html">Invoice #10395</a>
                      </td>
                      <td>
                        <time datetime="2020-04-24">Apr. 24, 2020</time>
                      </td>
                      <td>
                        $29.00
                      </td>
                      <td>
                        <span class="badge bg-secondary">Outstanding</span>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <a href="invoice.html">Invoice #10244</a>
                      </td>
                      <td>
                        <time datetime="2020-03-24">Mar. 24, 2020</time>
                      </td>
                      <td>
                        $29.00
                      </td>
                      <td>
                        <span class="badge bg-success">Paid</span>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <a href="invoice.html">Invoice #10119</a>
                      </td>
                      <td>
                        <time datetime="2020-02-24">Feb. 24, 2020</time>
                      </td>
                      <td>
                        $29.00
                      </td>
                      <td>
                        <span class="badge bg-success">Paid</span>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <a href="invoice.html">Invoice #10062</a>
                      </td>
                      <td>
                        <time datetime="2020-01-24">Jan. 24, 2020</time>
                      </td>
                      <td>
                        $29.00
                      </td>
                      <td>
                        <span class="badge bg-success">Paid</span>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Text -->
            <p class="text-center">
              <small class="text-muted">Don’t need Dashkit anymore? <a href="#!">Cancel your account</a></small>
            </p>

            <br>

          </div>
        </div> <!-- / .row -->
        <div class="" v-else>
          <h3 class="text-center mt-5">Permission denied!</h3>
        </div>
      </div>
</template>
<script>
import { Card, handleCardSetup } from "vue-stripe-elements-plus";
export default {
  data() {
    return {
      user: {},
      complete: false,
      autosaving: false,
      busy: false,
      errors: {},
      stripePubKey: stripePubKey,
      failed: false,
      delmethod: false,
      deleting: false
    };
  },
  components: { Card },
  mounted() {
    this.user = this.$store.state.user;
  },
  methods: {
    removePaymentMethod() {
      let _this = this;
      if (_this.deleting) {
        return false;
      }
      _this.deleting = true;
      let fd = new FormData();
      fd.append("payMethodId", _this.$store.state.user.payment_method_id);
      axios
        .post("/billing/remove-card/", fd)
        .then((res) => {
          _this.$store.commit("setUser");
          _this.delmethod = false;
          _this.deleting = false;
          toastr.warning("Your payment method has been deleted.");
        })
        .catch((err) => {
          _this.failed = true;
          _this.deleting = false;
        });
    },
    updateBillingInfo() {
      let _this = this;
      if (_this.busy) {
        return false;
      }
      _this.alertmessage = "";
      _this.busy = true;
      _this.errors = {};
      _this.failed = false;
      let fd = new FormData();
      axios
        .get("/billing/setup-intent/")
        .then((res) => {
          let clientSecret = res.data.client_secret;
          handleCardSetup(clientSecret)
            .then((data) => {
              if (data.setupIntent.status == "succeeded") {
                let paymentMethodId = data.setupIntent.payment_method;
                let fd = new FormData();
                fd.append("payMethodId", paymentMethodId);
                axios
                  .post("/billing/payment-method/", fd)
                  .then((res) => {
                    _this.busy = false;
                    _this.$refs.card.clear();
                    _this.$store.commit("setUser");
                    toastr.success("Your payment method has been saved.");
                  })
                  .catch((err) => {
                    _this.busy = false;
                    _this.failed = true;
                    toastr.error("Payment method cannot be updated.");
                  });
              } else {
                _this.busy = false;
                _this.failed = true;
              }
            })
            .catch((err) => {
              _this.busy = false;
              _this.failed = true;
            });
        })
        .catch((err) => {
          toastr.error("Payment method cannot be updated.");
          _this.busy = false;
        });
    },
  },
};
</script>