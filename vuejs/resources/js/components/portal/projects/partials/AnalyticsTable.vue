<template>
  <div class="row">
    <div class="col-12">
      <div class="card mb-3">
        <div class="card-header bg-light">
          <div class="row align-items-center justify-content-between">
            <div class="col-6 col-sm-auto d-flex align-items-center pr-0">
              <h5 class="fs-0 mb-0 text-nowrap py-2 py-xl-0">
                Last 1,000 Logs<span v-if="stats.count"> ({{ stats.count|toNumber }})</span>
              </h5>
            </div>
          </div>
        </div>
        <div class="card-body px-0 pt-0">
          <div v-if="busy" class="row g-0 p-4 text-center">
            <loading-component
              :busy="busy"
              nText
              bText="Loading stats..."
            ></loading-component>
          </div>
          <div v-else>
            <div v-if="!stats || stats.count == 0" class="row g-0 pt-4 text-center">
              <h3 class="text-center text-muted">No statistics found!</h3>
            </div>
            <div v-else class="row g-0">
              <div class="table-responsive">
                <table class="table">
                  <thead class="bg-secondary text-white">
                    <tr>
                      <th style="width: 50%">
                        <a
                          class="text-decoration-none text-white"
                          @click="orderstatsBy('url')"
                          href="javascript:void(0)"
                        >
                          <i v-if="order_by == 'url'" class="fas fa-arrow-up"></i>
                          <i
                            v-if="order_by == '-url'"
                            class="fas fa-arrow-down"
                          ></i>
                          Request Path
                        </a>
                      </th>
                      <th style="width: 15%">
                        <a
                          class="text-decoration-none text-white"
                          @click="orderstatsBy('status')"
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
                          @click="orderstatsBy('created_at')"
                          href="javascript:void(0)"
                        >
                          <i v-if="order_by == 'created_at'" class="fas fa-arrow-up"></i>
                          <i
                            v-if="order_by == '-created_at'"
                            class="fas fa-arrow-down"
                          ></i>
                          Date & Time
                        </a>
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="stat in stats.results">
                      <td><span class="border border-info px-1 rounded text-info">{{ stat.method }}</span> {{ stat.url }}</td>
                      <td :class="{'font-weight-bold text-success': stat.status == 200, 'font-weight-bold text-warning': stat.status != 200}">{{ stat.status }}</td>
                      <td>{{ stat.created_at }}</td>
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
            @click="(offset = previous_offset), getstats()"
            class="btn btn-falcon-default"
          >
            Previous
          </button>
          <button
            :disabled="next_offset == false"
            @click="(offset = next_offset), getstats()"
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
      stats: {},
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
    _this.getstats();
  },
  methods: {
    getParameterByName(url, name) {
      var match = RegExp("[?&]" + name + "=([^&]*)").exec(url);
      return match && decodeURIComponent(match[1].replace(/\+/g, " "));
    },
    getstats() {
      let _this = this;
      _this.busy = true;
      axios
        .get(
          `/users/analytics/?limit=${_this.limit}&offset=${_this.offset}&order_by=${_this.order_by}&status=${_this.status}`
        )
        .then((res) => {
          _this.stats = res.data;
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
          _this.stats = false;
        });
    },
    orderstatsBy(order_by) {
      let _this = this;
      if (order_by == _this.order_by) {
        _this.order_by = `-${order_by}`;
      } else {
        _this.order_by = order_by;
      }
      _this.offset = "";
      _this.getstats();
    },
  },
  watch: {
    busy(oldVal, newVal) {
      docReady(tooltipInit);
    },
    status(oldVal, newVal) {
      this.getstats();
    },
  },
};
</script>
