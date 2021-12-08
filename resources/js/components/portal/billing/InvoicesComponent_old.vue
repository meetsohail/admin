<template>
    <div class="row">
    <div class="col-12">
      <div class="card mb-3">
        <div class="card-header gradient-dark text-white">
          <div class="row align-items-center justify-content-between">
            <div class="col-6 col-sm-auto d-flex align-items-center pr-0">
              <h5 class="text-white mb-0 text-nowrap py-2 py-xl-0">
                Invoices<span v-if="invoices.count"> ({{ invoices.count|toNumber }})</span>
              </h5>
            </div>
          </div>
        </div>
        <div class="card-body px-0 pt-0">
          <div v-if="busy" class="row g-0 p-4 text-center">
            <loading-component
              :busy="busy"
              nText
              bText="Loading invoices..."
            ></loading-component>
          </div>
          <div v-else>
            <div v-if="!invoices || invoices.count == 0" class="row g-0 pt-4 text-center">
              <h5 class="text-center text-muted my-5">No invoices found!</h5>
            </div>
            <div v-else class="row g-0">
              <div class="table-responsive">
                <table class="table">
                  <thead class="bg-secondary text-white">
                    <tr>
                      <th style="width:10%;">
                        <a
                          class="text-decoration-none text-white"
                          @click="orderinvoicesBy('pk')"
                          href="javascript:void(0)"
                        >
                          <i v-if="order_by == 'pk'" class="fas fa-arrow-up"></i>
                          <i
                            v-if="order_by == '-pk'"
                            class="fas fa-arrow-down"
                          ></i>
                          ID
                        </a>
                      </th>
                      <th style="width: 20%">
                        <a
                          class="text-decoration-none text-white"
                          @click="orderinvoicesBy('cost')"
                          href="javascript:void(0)"
                        >
                          <i v-if="order_by == 'cost'" class="fas fa-arrow-up"></i>
                          <i
                            v-if="order_by == '-cost'"
                            class="fas fa-arrow-down"
                          ></i>
                          Amount
                        </a>
                      </th>
                      <th style="width: 20%">
                        <a
                          class="text-decoration-none text-white"
                          @click="orderinvoicesBy('status')"
                          href="javascript:void(0)"
                        >
                          <i v-if="order_by == 'status'" class="fas fa-arrow-up"></i>
                          <i
                            v-if="order_by == '-status'"
                            class="fas fa-arrow-down"
                          ></i>
                          Status
                        </a>
                      </th>
                      <th colspan="2">
                        <a
                          class="text-decoration-none text-white"
                          @click="orderinvoicesBy('date')"
                          href="javascript:void(0)"
                        >
                          <i v-if="order_by == 'date'" class="fas fa-arrow-up"></i>
                          <i
                            v-if="order_by == '-date'"
                            class="fas fa-arrow-down"
                          ></i>
                          Invoice Date
                        </a>
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="invoice in invoices.results" :key="invoice.id">
                      <td>#{{ invoice.id }}</td>
                      <td>{{ invoice.cost|toCurrency }}</td>
                      <td>
                        <span style="width:80px;" v-if="invoice.status=='paid'" class="badge badge rounded-capsule badge-soft-primary">Paid <span class="ml-1 fas fa-check-circle" data-fa-transform="shrink-2"></span></span>
                        <span style="width:80px;" v-else-if="['open', 'draft'].includes(invoice.status)" class="badge badge rounded-capsule badge-soft-warning">Pending <span class="ml-1 fas fa-stream" data-fa-transform="shrink-2"></span></span>
                        <span style="width:80px;" v-else-if="invoice.status=='void'" class="badge badge rounded-capsule badge-soft-danger">Void <span class="ml-1 fas fa-times-circle" data-fa-transform="shrink-2"></span></span>
                        <span style="width:80px;" v-else-if="invoice.status=='uncollectible'" class="badge badge rounded-capsule badge-soft-danger">Invalid <span class="ml-1 fas fa-info-circle" data-fa-transform="shrink-2"></span></span>
                        <span style="width:80px;" v-else class="badge badge rounded-capsule badge-soft-danger">Unknown <span class="ml-1 fas fa-info-circle" data-fa-transform="shrink-2"></span></span>
                      </td>
                      <td>{{ invoice.date }}</td>
                      <td class="text-right">
                        <a target="_blank" :class="{'disabled': !invoice.url}" :href="invoice.url" class="btn btn-sm btn-primary">View</a>
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
            @click="(offset = previous_offset), getinvoices()"
            class="btn btn-falcon-default"
          >
            Previous
          </button>
          <button
            :disabled="next_offset == false"
            @click="(offset = next_offset), getinvoices()"
            class="btn btn-falcon-default"
          >
            Next
          </button>
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
      invoices: {},
      busy: false,
      next_offset: false,
      previous_offset: false,
      offset: "",
      limit: 10,
      order_by: "-pk",
      status: ""
    };
  },
  mounted() {
    docReady(tooltipInit);
    let _this = this;
    _this.getinvoices();
  },
  methods: {
    getParameterByName(url, name) {
      var match = RegExp("[?&]" + name + "=([^&]*)").exec(url);
      return match && decodeURIComponent(match[1].replace(/\+/g, " "));
    },
    getinvoices() {
      let _this = this;
      _this.busy = true;
      axios
        .get(
          `/users/invoices/?limit=${_this.limit}&offset=${_this.offset}&order_by=${_this.order_by}&status=${_this.status}`
        )
        .then((res) => {
          _this.invoices = res.data;
          if (res.data.next) {
            _this.next_offset = _this.getParameterByName(res.data.next, "offset");
          } else {
            _this.next_offset = false;
          }
          if (res.data.previous) {
            let prev_offset = _this.getParameterByName(res.data.previous, "offset");
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
          _this.invoices = false;
        });
    },
    orderinvoicesBy(order_by) {
      let _this = this;
      if (order_by == _this.order_by) {
        _this.order_by = `-${order_by}`;
      } else {
        _this.order_by = order_by;
      }
      _this.offset = "";
      _this.getinvoices();
    },
  },
  watch: {
    busy(oldVal, newVal) {
      docReady(tooltipInit);
    },
    status(oldVal, newVal) {
      this.getinvoices();
    },
  },
};
</script>
