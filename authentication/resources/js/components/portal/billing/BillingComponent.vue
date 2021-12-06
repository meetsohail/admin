<template>
  <div class="row" v-if="$store.state.user">
    <div class="col-lg-12">
      <div v-if="!$store.state.user.stripe_last4" class="alert text-white alert-danger gradient-danger">
        To top-up your account, you need to set a payment method first.
      </div>
      <div v-if="delmethod" class="alert alert-warning">
        <span class="d-block mb-2"
          >If this payment method is removed, your subscription renewals will fail. To
          keep your subscriptions active, you need to have a valid payment method on file.
          Do you really want to remove your current card?</span
        >
        <button
          :disabled="deleting"
          class="btn btn-sm btn-warning"
          @click="removePaymentMethod()"
        >
          <loading-component
            :busy="deleting"
            nText="Remove"
            bText="Removing"
          ></loading-component>
        </button>
        <button
          :disabled="deleting"
          class="btn btn-sm btn-success"
          @click="delmethod = false"
        >
          Cancel
        </button>
      </div>
      <div class="card mb-3">
        <div class="card-header gradient-dark ">
          <div class="row">
            <div class="col">
              <h5 class="mb-0 text-white">
                <span v-if="!$store.state.user.stripe_last4">Add Card</span>
                <span v-else>Update Card</span>
              </h5>
            </div>
            <div class="col text-right">
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
            </div>
          </div>
        </div>
        <div class="card-body bg-light">
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
                class="btn btn-black rounded text-white"
                type="submit"
              >
                <loading-component :busy="busy"></loading-component>
              </button>
            </div>
          </div>
        </div>
      </div>
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
