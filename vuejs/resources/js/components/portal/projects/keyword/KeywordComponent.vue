<template>
    <div v-if="keyword" class="row">
        <div class="col-12">
            <!-- custom code  -->
            <div class="col-md-12">
                <div class="card">
                    <div class="card-header" style="border-radius: 10px">
                        <div class="row flex-between-center">
                            <div class="col-auto my-2">
                                <h5 class="mb-0 fs-1 my-1">
                                    Keyword: <small>{{ keyword.keyword }}</small>
                                </h5>
                            </div>
                            <div class="col-auto">
                                <!-- <select
                                    class="form-select form-select-sm select-month me-2 mx-1"
                                    @change="getKeywordData()"
                                    v-model="report_id"
                                >
                                    <option v-for="report in keyword.reports" :key="report.id" :value="report.id">{{ report.label }}</option>
                                </select> -->
                                <div class="row">
                                    <div class="col-md-4 col-sm-12 my-1">
                                        <v-select  class="style-chooser" style="width:200px; font-size:12px !important;" :reduce="(report) => report.id" v-model="report_id" :options="keyword.reports"></v-select>
                                    </div>
                                
                                    <div class="col-md-4 col-sm-12 my-1">
                                        <!-- <select
                                            class="form-select form-select-sm select-month me-2 mx-1"
                                            @change="getKeywordData()"
                                            v-model="country_id"
                                        >
                                            <option
                                                v-for="country in keyword.countries"
                                                :key="country.id"
                                                :value="country.id"
                                            >
                                                {{ country.label }}
                                            </option>
                                        </select> -->
                        <v-select style="width:200px;" :reduce="(options) => options.id" v-model="country_id" @change="getKeywordData()" :options="keyword.countries"></v-select>

                                    </div>
                                        <div class="col-md-4 col-sm-12 my-1">
                                        <select
                                            class="form-select select-month me-2"
                                            @change="getKeywordData()"
                                            v-model="device"
                                        >
                                            <option value="desktop">Desktop</option>
                                            <option value="mobile">Mobile</option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- /custom code -->

            <div class="my-3">
                <div class="">
                    <div class="row">
                        <div class="col-md-3 mb-3">
                            <div class="card h-md-100 p-1">
                                <div
                                    class="bg-holder bg-card"
                                    style="
                                        background-image: url(https://prium.github.io/falcon/v3.5.0/assets/img/icons/spot-illustrations/corner-1.png);
                                    "
                                ></div>

                                <div class="card-header pb-0">
                                    <h6 class="mb-0 mt-2">Current Position</h6>
                                </div>
                                <div class="card-body pt-0">
                                    <div class="row h-50 pt-3">
                                        <div class="col align-self-end">
                                            <div
                                                class="fs-2 font-weight-normal font-sans-serif text-700 lh-1 mb-1"
                                            >
                                                <span
                                                    v-if="keyword.stats.current_position"
                                                    >{{
                                                        keyword.stats.current_position
                                                    }}</span
                                                >
                                                <span v-else>N/A</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3 col-xxl-3 mb-3 pl-md-2 pr-xxl-2">
                            <div class="card h-md-100 p-1">
                                <div
                                    class="bg-holder bg-card"
                                    style="
                                        background-image: url(https://prium.github.io/falcon/v3.5.0/assets/img/icons/spot-illustrations/corner-2.png);
                                    "
                                ></div>

                                <div class="card-header pb-0">
                                    <h6 class="mb-0 mt-2">Best Position</h6>
                                </div>
                                <div class="card-body pt-0">
                                    <div class="row h-50 pt-3">
                                        <div class="col align-self-end">
                                            <div
                                                class="fs-2 font-weight-normal font-sans-serif text-700 lh-1 mb-1"
                                            >
                                                <span
                                                    v-if="keyword.stats.best_position"
                                                    >{{
                                                        keyword.stats.best_position
                                                    }}</span
                                                >
                                                <span v-else>N/A</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3 col-xxl-3 mb-3 pl-md-2 pr-xxl-2">
                            <div class="card h-md-100 p-1">
                                <div
                                    class="bg-holder bg-card"
                                    style="
                                        background-image: url(https://prium.github.io/falcon/v3.5.0/assets/img/icons/spot-illustrations/corner-3.png);
                                    "
                                ></div>

                                <div class="card-header pb-0">
                                    <h6 class="mb-0 mt-2">Last Position</h6>
                                </div>
                                <div class="card-body pt-0">
                                    <div class="row h-50 pt-3">
                                        <div class="col align-self-end">
                                            <div
                                                class="fs-2 font-weight-normal font-sans-serif text-700 lh-1 mb-1"
                                            >
                                                <span
                                                    v-if="keyword.stats.last_position"
                                                    >{{
                                                        keyword.stats.last_position
                                                    }}</span
                                                >
                                                <span v-else>N/A</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3 col-xxl-3 mb-3 pl-md-2 pr-xxl-2">
                            <div class="card h-md-100 p-1">
                                <div
                                    class="bg-holder bg-card"
                                    style="
                                        background-image: url(https://prium.github.io/falcon/v3.5.0/assets/img/icons/spot-illustrations/corner-1.png);
                                    "
                                ></div>

                                <div class="card-header pb-0">
                                    <h6 class="mb-0 mt-2">Average Position</h6>
                                </div>
                                <div class="card-body pt-0">
                                    <div class="row h-50 pt-3">
                                        <div class="col align-self-end">
                                            <div
                                                class="fs-2 font-weight-normal font-sans-serif text-700 lh-1 mb-1"
                                            >
                                                <span v-if="keyword.stats.avg_position">{{
                                                    keyword.stats.avg_position
                                                }}</span>
                                                <span v-else>N/A</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="card">
                <div class="card-body px-4 pt-0">
                    <div class="row g-0"></div>
                    <div v-if="busy" class="row g-0 p-4 text-center">
                        <loading-component
                            :busy="busy"
                            bText="Loading project data..."
                        ></loading-component>
                    </div>
                    <div v-else class="col-md-12">
                        <div v-if="historical_data.xaxis" class="row g-0">
                            <div class="col-md-12">
                                <line-widget
                                    v-if="!busy"
                                    :xAxis="historical_data.xaxis"
                                    :yAxis="historical_data.yaxis"
                                ></line-widget>
                            </div>
                        </div>
                        <div class="py-5 my-5 text-center" v-else>
                            <h4 class="text-muted">Chart data not available yet.</h4>
                        </div>

                    </div>
                </div>
            </div>
            <div class="card mt-3">
                <div class="card-header bg-light">
                    <h5 class="text-primary fs-1">Ranked URLs</h5>
                </div>
                <div v-if="keyword.rankings.length" class="card-body px-0 pt-0">
                    <div class="table-responsive">
                        <table
                            class="table table-dashboard mb-0 table-striped table-hover border-200"
                        >
                            <thead class="bg-primary gradient-dark text-white">
                                <tr>
                                    <th>Position</th>
                                    <th>URL</th>
                                    <th>Country</th>
                                    <th>Device</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="ranking in keyword.rankings" :key="ranking.id">
                                    <td>{{ ranking.position }}</td>
                                    <td>
                                        <h6
                                            :class="{
                                                'font-weight-bold':
                                                    ranking.is_own
                                            }"
                                            class="mb-0 pb-0 text-dark"
                                        >
                                            {{ ranking.title }}
                                        </h6>
                                        <small class="text-dark">{{ ranking.url }}</small>
                                    </td>
                                    <td class="font-weight-bold">
                                        {{ ranking.country }}
                                    </td>
                                    <td class="text-center">
                                        <i
                                            v-if="ranking.device == 'desktop'"
                                            class="fas fa-desktop"
                                        ></i>
                                        <i v-else class="fas fa-mobile-alt"></i>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <div v-else class="card-body py5 my-5">
                    <h3 class="text-muted text-center">No data available.</h3>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            busy: true,
            keyword: false,
            report_id: "",
            country_id: "",
            device: "desktop",
            historical_data: false,
        };
    },
    mounted() {
        this.getKeywordData();
    },
 
    methods: {
        getKeywordData() {
            let _this = this;
            _this.busy = true;
            axios
                .get(
                    `/data/keyword-data/?keyword_id=${_this.$route.params.id}&country_id=${_this.country_id}&report_id=${_this.report_id}&device_id=${_this.device}`
                )
                .then((res) => {
                    _this.keyword = res.data;
                    _this.report_id = res.data.current_report.value;
                    _this.country_id = res.data.current_country;
                    _this.historical_data = res.data.historical_data;
                    _this.busy = false;
                })
                .catch((err) => {
                    _this.busy = false;
                });
              
        },
    },
    watch: {
        report_id(newval, old) {
            if(newval) {
                this.getKeywordData();
            }
        },
        country_id(newval, old) {
            if(newval) {
                this.getKeywordData();
            }
        }
    }
};
</script>


