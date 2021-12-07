<template>
    <div>
        <div class="row no-gutters" v-if="summary">
            <div class="col-lg-6 col-xl-7 col-xxl-8 mb-3 pr-lg-2 mb-3">
              <div class="card h-lg-100">
                <div class="card-body d-flex align-items-center">
                  <div class="w-100">
                    <h6 class="mb-3 text-800">Requests Status (Last 30 Days)</h6>
                    <div class="progress mb-3 rounded-soft" style="height: 10px;">
                      <div class="progress-bar bg-success border-right border-white border-2x" role="progressbar" :style="'width:' + summary.breakdown.successful +'%'" :aria-valuenow="summary.breakdown.successful" aria-valuemin="0" aria-valuemax="100"></div>
                      <div class="progress-bar bg-warning border-right border-white border-2x" role="progressbar" :style="'width:' + summary.breakdown.failed +'%'" :aria-valuenow="summary.breakdown.failed" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <div class="row fs--1 font-weight-semi-bold text-500">
                      <div class="col-auto d-flex align-items-center pr-2"><span class="dot bg-success"></span><span>200 OK</span><span class="d-none d-md-inline-block d-lg-none d-xxl-inline-block ml-1">({{ summary.breakdown.successful.toFixed(2) }}%)</span></div>
                      <div class="col-auto d-flex align-items-center px-2"><span class="dot bg-warning"></span><span>Non 200</span><span class="d-none d-md-inline-block d-lg-none d-xxl-inline-block ml-1">({{ summary.breakdown.failed.toFixed(2) }}%)</span></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-lg-6 col-xl-5 col-xxl-4 mb-3 pl-lg-2">
              <div class="card h-lg-100">
                  <div class="card-body rounded bg-light text-center position-relative">
                    <span><span class="font-weight-bold">Realtime Stats</span> <a :class="{'text-muted': busy}" @click="getSummary()" href="javascript:void(0)"><i class="fas fa-redo"></i></a></span>
                    <h3 class="text-primary pt-2">
                      {{ req_count|toNumber }} reqs / sec
                    </h3>
                  </div>
              </div>
            </div>
          </div>
          <analytics-table :pagination="false"></analytics-table>
    </div>
</template>
<script>
import AnalyticsTable from '../jobs/partials/AnalyticsTable';
export default {
    components: {
      AnalyticsTable
    },
    data() {
        return {
          summary: false,
          req_count: 0,
          busy: false,
          intervalId: false
        }
    },
    mounted() {
        this.$store.commit('setUser');
        this.getSummary();
    },
    methods: {
      getSummary() {
        let _this = this;
        _this.busy = true;
        axios.get('/users/analytics-summary/').then((res) => {
          _this.summary = res.data.data;
          _this.animateValue(_this.req_count, _this.summary.req_count, 500);
          _this.busy = false;
        }).catch((err) => {
          toastr.error('Analytics summary cannot be retrieved.');
          _this.busy = false;
        });
      },
      animateValue(start, end, duration) {
        let _this = this;
        if (start === end) return;
        var range = end - start;
        var current = start;
        var increment = end > start? 1 : -1;
        var stepTime = Math.abs(Math.floor(duration / range));
        var timer = setInterval(function() {
            current += increment;
            _this.req_count = current;
            if (current == end) {
                clearInterval(timer);
            }
        }, stepTime);
    }
    }
};
</script>