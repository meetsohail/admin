<template>
    <div class="row">
        <div class="card-body px-0 pt-0">
            <div v-if="is_busy" class="row g-0 p-4 text-center">
                <loading-component
                    :busy="is_busy"
                    bText="Loading project data..."
                ></loading-component>
            </div>
            <div v-else class="col-md-12">
                <div class="col-12">
                    <div class="row g-0">
                        <div class="col-md-4 mb-3 ">
                            <div class="card h-md-100">
                                <div class="bg-holder bg-card" style="background-image:url(https://prium.github.io/falcon/v3.5.0/assets/img/icons/spot-illustrations/corner-1.png);"></div>
                                <div class="card-header pb-0">
                                    <h6 class="mb-0 mt-2 text-warning">Total Keywords </h6>
                                    
                                </div>
                                <div class="card-body pt-0">
                                    <div class="row h-100">
                                        <div class="col align-self-end">
                                            <div
                                                class="fs-4 font-weight-normal font-sans-serif text-700 lh-1 mb-1 "
                                            >
                                                <span class="text-warning">{{ total_keywords }}</span>
                                            </div>
                                        </div>
                                        <div class="col-auto pl-0">
                                            <div
                                                class="echart-line-total-order h-100"
                                                style="
                                                    -webkit-tap-highlight-color: transparent;
                                                    user-select: none;
                                                    position: relative;
                                                "
                                                _echarts_instance_="ec_1638122536006"
                                            >
                                                <div
                                                    style="
                                                        position: relative;
                                                        width: 138px;
                                                        height: 81px;
                                                        padding: 0px;
                                                        margin: 0px;
                                                        border-width: 0px;
                                                        cursor: pointer;
                                                    "
                                                >
                                                    <canvas
                                                        data-zr-dom-id="zr_0"
                                                        width="276"
                                                        height="162"
                                                        style="
                                                            position: absolute;
                                                            left: 0px;
                                                            top: 0px;
                                                            width: 138px;
                                                            height: 81px;
                                                            user-select: none;
                                                            -webkit-tap-highlight-color: rgba(
                                                                0,
                                                                0,
                                                                0,
                                                                0
                                                            );
                                                            padding: 0px;
                                                            margin: 0px;
                                                            border-width: 0px;
                                                        "
                                                    ></canvas>
                                                </div>
                                                <div
                                                    style="
                                                        position: absolute;
                                                        display: none;
                                                        border-style: solid;
                                                        white-space: nowrap;
                                                        z-index: 9999999;
                                                        background-color: rgb(
                                                            255,
                                                            255,
                                                            255
                                                        );
                                                        border-width: 1px;
                                                        border-color: rgb(216, 226, 239);
                                                        border-radius: 4px;
                                                        color: rgb(11, 23, 39);
                                                        font: 14px / 21px sans-serif;
                                                        padding: 7px 10px;
                                                        left: 55px;
                                                        top: -44px;
                                                        pointer-events: none;
                                                    "
                                                >
                                                    Week 5: 130
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-4 mb-3 pl-md-2 pr-xxl-2">
                            <div class="card h-md-100">
                                <div class="bg-holder bg-card" style="background-image:url(https://prium.github.io/falcon/v3.5.0/assets/img/icons/spot-illustrations/corner-2.png);"></div>
                                <div class="card-header pb-0">

                                    <h6 class="mb-0 mt-2 text-info">Average Position </h6>
                                </div>
                                <div class="card-body pt-0">
                                    <div class="row h-100">
                                        <div class="col align-self-end">
                                            <div
                                                class="fs-4 font-weight-normal font-sans-serif text-700 lh-1 mb-1"
                                            >
                                                <span class="text-info">{{ kw_avg_position }}</span>
                                            </div>
                                        </div>
                                        <div class="col-auto pl-0">
                                            <div
                                                class="echart-line-total-order h-100"
                                                style="
                                                    -webkit-tap-highlight-color: transparent;
                                                    user-select: none;
                                                    position: relative;
                                                "
                                                _echarts_instance_="ec_1638122536006"
                                            >
                                                <div
                                                    style="
                                                        position: relative;
                                                        width: 138px;
                                                        height: 81px;
                                                        padding: 0px;
                                                        margin: 0px;
                                                        border-width: 0px;
                                                        cursor: pointer;
                                                    "
                                                >
                                                    <canvas
                                                        data-zr-dom-id="zr_0"
                                                        width="276"
                                                        height="162"
                                                        style="
                                                            position: absolute;
                                                            left: 0px;
                                                            top: 0px;
                                                            width: 138px;
                                                            height: 81px;
                                                            user-select: none;
                                                            -webkit-tap-highlight-color: rgba(
                                                                0,
                                                                0,
                                                                0,
                                                                0
                                                            );
                                                            padding: 0px;
                                                            margin: 0px;
                                                            border-width: 0px;
                                                        "
                                                    ></canvas>
                                                </div>
                                                <div
                                                    style="
                                                        position: absolute;
                                                        display: none;
                                                        border-style: solid;
                                                        white-space: nowrap;
                                                        z-index: 9999999;
                                                        background-color: rgb(
                                                            255,
                                                            255,
                                                            255
                                                        );
                                                        border-width: 1px;
                                                        border-color: rgb(216, 226, 239);
                                                        border-radius: 4px;
                                                        color: rgb(11, 23, 39);
                                                        font: 14px / 21px sans-serif;
                                                        padding: 7px 10px;
                                                        left: 55px;
                                                        top: -44px;
                                                        pointer-events: none;
                                                    "
                                                >
                                                    Week 5: 130
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-4 mb-3 pl-md-2 pr-xxl-2">
                            <div class="card h-md-100">
                                <div class="bg-holder bg-card" style="background-image:url(https://prium.github.io/falcon/v3.5.0/assets/img/icons/spot-illustrations/corner-2.png);"></div>


                                <div class="card-body">
                                    <div class="row h-100 justify-content-between g-0">
                                        <div class="col-5 col-sm-6 pr-2">
                                            <h6 class="mt-1 text-primary">Positions</h6>
                                            <div class="fs--2 mt-3">
                                                <div
                                                    class="d-flex flex-between-center mb-1"
                                                >
                                                    <div
                                                        class="d-flex align-items-center"
                                                    >
                                                        <span
                                                            class="dot bg-success"
                                                        ></span
                                                        ><span
                                                            class="font-weight-semi-bold"
                                                        >
                                                            1 — 10</span
                                                        >
                                                    </div>
                                                    <div>
                                                        {{ positions_data[0].value }}
                                                    </div>
                                                </div>
                                                <div
                                                    class="d-flex flex-between-center mb-1"
                                                >
                                                    <div
                                                        class="d-flex align-items-center"
                                                    >
                                                        <span class="dot bg-info"></span
                                                        ><span
                                                            class="font-weight-semi-bold"
                                                        >
                                                            11 — 20</span
                                                        >
                                                    </div>
                                                    <div>
                                                        {{ positions_data[1].value }}
                                                    </div>
                                                </div>
                                                <div
                                                    class="d-flex flex-between-center mb-1"
                                                >
                                                    <div
                                                        class="d-flex align-items-center"
                                                    >
                                                        <span
                                                            class="dot bg-warning"
                                                        ></span
                                                        ><span
                                                            class="font-weight-semi-bold"
                                                        >
                                                            21 — ∞</span
                                                        >
                                                    </div>
                                                    <div>
                                                        {{ positions_data[2].value }}
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-auto" style="position: relative">
                                            <div class="echart-market-share"></div>
                                            <!-- <div class="fs-2" style="transform: translateX(-50%) translateY(-50%) !important; position:absolute !important; top:50%; left:50%;">26M</div> -->
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="card mb-3">
                    <!-- <div class="bg-holder bg-card" style="background-image:url(https://prium.github.io/falcon/v3.5.0/assets/img/icons/spot-illustrations/corner-2.png);"></div> -->

                        <div class="card-header bg-light">
                            <h5 class="float-left pt-1">
                                Project<span v-if="project">: {{ project.title }}</span>
                                <small>({{ project.url }})</small>
                            </h5>
                        </div>
                        <div class="col-md-12">
                        <div  v-if="chart_data">
                            <line-widget :xAxis="chart_data.xaxis" :yAxis="chart_data.yaxis"></line-widget>
                        </div>
                        <div class="py-5 my-5 text-center" v-else>
                                <h4 class="text-muted">Chart data not available yet.</h4>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="card-body px-0 pt-0">
                    <div v-if="is_busy" class="row g-0 p-4 text-center">
                        <loading-component
                            :busy="is_busy"
                            bText="Loading project data..."
                        ></loading-component>
                    </div>
                    <div v-else class="col-md-12">
                        <div class="row g-0"></div>
                    </div>
                </div>
            </div>
            <div v-if="addkw" class="card mb-3">
                <div class="card-header bg-light">
                    <h5>Add Keyword</h5>
                </div>
                <div class="card-body">
                    <div class="form-group mt-3">
                        <input
                            :class="{ 'is-invalid': errors.keyword }"
                            type="text"
                            v-model="keyword"
                            class="form-control form-control-lg"
                            id="keyword"
                            placeholder="Enter a keyword to track"
                            @keyup.enter="addKeyword()"
                        />
                        <p v-if="errors.keyword" class="invalid-feedback">
                            {{ errors.keyword[0] }}
                        </p>
                    </div>
                </div>
                <div class="card-footer">
                    <button
                        :disabled="adding"
                        @click="addKeyword()"
                        class="btn btn-black text-white"
                    >
                        Save
                    </button>
                    <button
                        :disabled="adding"
                        @click="(addkw = false), (errors = {})"
                        class="btn text-white btn-orange"
                    >
                        Cancel
                    </button>
                </div>
            </div>
            <div v-if="importkws" class="card mb-3">
                <div class="card-header bg-light">
                    <h5>Import Keywords</h5>
                </div>
                <div class="card-body">
                    <div class="form-group mt-3">
                        <label for="csvfile">Select CSV file</label>
                        <input
                            :class="{ 'is-invalid': errors.csvfile }"
                            type="file"
                            id="csvfile"
                            class="form-control form-control-lg mb-3"
                            ref="csvfile"
                        />
                        <p class="invalid-feedback" v-if="errors.csvfile">
                            {{ errors.csvfile[0] }}
                        </p>
                        <label for="filesource">Select Source</label>
                        <select
                            :class="{ 'is-invalid': errors.filesource }"
                            id="filesource"
                            class="form-control form-control-lg"
                            v-model="filesource"
                        >
                            <option value="plain_text">Comma-separated Keywords</option>
                            <option value="google_console">Google Console</option>
                            <option value="ahrefs">Ahrefs</option>
                            <option value="semrush">Semrush</option>
                        </select>
                        <p v-if="errors.filesource" class="invalid-feedback">
                            {{ errors.filesource[0] }}
                        </p>
                    </div>
                </div>
                <div class="card-footer">
                    <button
                        :disabled="importing"
                        @click="importKeywords()"
                        class="btn btn-black text-white"
                    >
                        Import
                    </button>
                    <button
                        :disabled="importing"
                        @click="(importkws = false), (errors = {})"
                        class="btn text-white btn-orange"
                    >
                        Cancel
                    </button>
                </div>
            </div>
            <div class="card">
                    <!-- <div class="bg-holder bg-card" style="background-image:url(https://prium.github.io/falcon/v3.5.0/assets/img/icons/spot-illustrations/corner-1.png);"></div> -->

                <div class="card-header bg-light">
                    <div class="row">
                        <div class="col-md-2">
                            <h5 class="float-left">Keywords</h5>
                        </div>
                        <div class="col-md-6">
                            <input
                                class="form-control float-left rounded"
                                v-model="search"
                                @keyup.enter="getKeywords()"
                                autocomplete="off"
                                type="search"
                                name="search"
                                placeholder="type keyword to search..."
                            />
                        </div>
                        <div class="col-md-4 my-1">
                            <button
                                :disabled="importkws || adding"
                                @click="(addkw = !addkw), (errors = {})"
                                class="btn text-white btn-orange float-right"
                            >
                                <i class="fas fa-plus"></i> Add
                            </button>
                            <button
                                @click="(importkws = !importkws), (errors = {})"
                                :disabled="addkw || importing"
                                class="btn text-white btn-black mr-1 float-right"
                            >
                                <i class="fas fa-file-csv"></i> Bulk Import
                            </button>
                        </div>
                    </div>
                </div>
                <div class="card-body">
                    <!-- {{ keywords }} -->
                    <div v-if="is_busy" class="row g-0 p-4 text-center">
                        <loading-component
                            :busy="is_busy"
                            bText="Loading keyword data..."
                        ></loading-component>
                    </div>
                    <div v-else class="table-responsive">
                        <table class="table table-striped table-hover">
                            <thead>
                                <tr>
                                    <th>Keyword</th>
                                    <th>Position</th>
                                    <th>Avg. Position</th>
                                    <th>Best Position</th>
                                    <th colspan="2">Updated</th>
                                </tr>
                            </thead>
                            <tbody v-if="keywords.count > 0">
                                <tr v-for="keyword in keywords.results" :key="keyword.id">
                                    <td
                                        @click="
                                            $router.push({
                                                name: 'keyworddetails',
                                                params: { id: keyword.id },
                                            })
                                        "
                                        style="cursor: pointer"
                                    >
                                        {{ keyword.keyword }}
                                    </td>
                                    <td
                                        @click="
                                            $router.push({
                                                name: 'keyworddetails',
                                                params: { id: keyword.id },
                                            })
                                        "
                                        style="cursor: pointer"
                                    >
                                        <span v-if="keyword.stats.current_position">{{
                                            keyword.stats.current_position
                                        }}</span>
                                        <span v-else>N/A</span>
                                        <span v-if="keyword.stats.change != null">
                                            <span v-if="keyword.stats.change > 0" class="text-success" style="font-size:12px;">
                                                <i class="fas fa-arrow-up"></i> {{ keyword.stats.change }}
                                            </span>
                                            <span v-if="keyword.stats.change < 0" class="text-danger" style="font-size:12px;">
                                                <i class="fas fa-arrow-down"></i> {{ Math.abs(keyword.stats.change) }}
                                            </span>
                                        </span>
                                    </td>
                                    <td
                                        @click="
                                            $router.push({
                                                name: 'keyworddetails',
                                                params: { id: keyword.id },
                                            })
                                        "
                                        style="cursor: pointer"
                                    >
                                        <span v-if="keyword.stats.avg_position">{{
                                            keyword.stats.avg_position
                                        }}</span>
                                        <span v-else>N/A</span>
                                    </td>
                                    <td
                                        @click="
                                            $router.push({
                                                name: 'keyworddetails',
                                                params: { id: keyword.id },
                                            })
                                        "
                                        style="cursor: pointer"
                                    >
                                        <span v-if="keyword.stats.best_position">{{
                                            keyword.stats.best_position
                                        }}</span>
                                        <span v-else>N/A</span>
                                    </td>
                                    <td
                                        @click="
                                            $router.push({
                                                name: 'keyworddetails',
                                                params: { id: keyword.id },
                                            })
                                        "
                                        style="cursor: pointer"
                                    >
                                        {{ keyword.updated_at }}
                                    </td>
                                    <td class="text-center">
                                    
                                        <a 
                                            href="javascript::void(0)"
                                            class=" p-2 fs-1"
                                            @click="deleteKeyword(keyword.id)"
                                            ><i class="fa fa-trash"></i
                                        ></a>
                                        <span
                                            v-if="
                                                delete_confirm &&
                                                keyword.id == delete_key_id
                                            "
                                            class="d-block my-2 d-flex"
                                        >
                                          
                                            <a
                                                href="javascript::void(0)"
                                                class="text-success btn-sm btn-light"
                                                
                                                
                                                @click="cancelDelete()"
                                                >Cancel</a
                                            >
                                              <a
                                                href="javascript::void(0)"
                                                class=" text-danger btn-sm btn-light ml-2"
                                                
                                                
                                                @click="confirmDelete(keyword.id)"
                                                >Confirm</a
                                            >
                                        </span>
                                    
                                    </td>
                                </tr>
                            </tbody>
                            <tbody v-else>
                                <tr>
                                    <td class="text-center" colspan="4">
                                        Keywords not found!
                                    </td>
                                </tr>
                            </tbody>
                        </table>

                        <div class="card-footer bg-light text-right">
                            <button
                                :disabled="!previous_offset"
                                @click="(offset = previous_offset), getKeywords()"
                                class="btn btn-falcon-default"
                            >
                                Previous
                            </button>
                            <button
                                :disabled="next_offset == false"
                                @click="(offset = next_offset), getKeywords()"
                                class="btn btn-falcon-default"
                            >
                                Next
                            </button>
                        </div>
                    </div>
                </div>
            </div>
            <a
                v-if="!del"
                href="javascript:void(0)"
                @click="del = true"
                style="font-size: 12px"
                class="text-danger"
            >
                <i class="fas fa-trash"></i> Delete project
            </a>
            <div v-else class="card mt-3 btn-red">
                <div class="card-header bg-danger">
                    <h5 class="text-white">Delete Project</h5>
                </div>
                <div class="card-body">
                    This action is irreversible. Once you will delete this project, all
                    associated data including keywords will be permanently deleted. Are
                    you sure that you really want to delete this project?
                </div>
                <div class="card-footer bg-light">
                    <button
                        v-if="delconfirm"
                        :disabled="deleting"
                        @click="deleteProject()"
                        class="btn btn-danger btn-red"
                    >
                        Confirm
                    </button>
                    <button
                        :disabled="deleting"
                        @click="(del = false), (delconfirm = false)"
                        class="btn btn-success btn-green"
                    >
                        Cancel
                    </button>
                    <button
                        v-if="!delconfirm"
                        @click="delconfirm = true"
                        class="btn text-white btn-orange"
                    >
                        Delete
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            del: false,
            delconfirm: false,
            project: {},
            is_busy: false,
            deleting: false,
            keywords: false,
            addkw: false,
            keyword: "",
            errors: {},
            adding: false,
            importkws: false,
            importing: false,
            filesource: "plain_text",
            delete_confirm: false,
            chart_data: false,
            delete_key_id: 0,
            next_offset: false,
            previous_offset: false,
            offset: "",
            limit: 10,
            search: "",
            importkeywords: "",
            key_offset: "",
            key_search: "",
            key_prev_offset: false,
            key_next_offset: false,
          
            

            // keywords widgets
            kw_avg_position: 0,
            total_keywords: 0,
            positions_data: [
                {
                    value: 0,
                    name: "1 — 10",
                },
                {
                    value: 0,
                    name: "11 — 20",
                },
                {
                    value: 0,
                    name: "21 — ∞",
                },
            ],
        };
    },
    mounted() {
        this.getProject(this.$route.params.id);
        // this.getImportKeywords();
        this.projectData();
        // health
        this.InitializeChart();
    },
    methods: {
        projectData(){
            let _this = this;
            axios
                    .get(`/data/project-data/?project_id=${_this.$route.params.id}`)
                    .then((res) => {
                        _this.chart_data = res.data.chart_data;
                    })
                    .catch((err)=>{})
        },
        InitializeChart() {
            var echartMarketShare = document.querySelector(".echart-market-share");

            if (echartMarketShare) {
                var userOptions = utils.getData(echartMarketShare, "options");
                var chart = window.echarts.init(echartMarketShare);
                var defaultOptions = {
                    color: [
                        utils.colors.success,
                        utils.colors.info,
                        utils.colors.warning,
                    ],
                    tooltip: {
                        trigger: "item",
                        padding: [7, 10],
                        backgroundColor: utils.grays.white,
                        textStyle: {
                            color: utils.grays.black,
                        },
                        transitionDuration: 0,
                        borderColor: utils.grays["300"],
                        borderWidth: 1,
                        formatter: function formatter(params) {
                            return "<strong>"
                                .concat(params.data.name, ":</strong> ")
                                .concat(params.percent, "%");
                        },
                    },
                    position: function position(pos, params, dom, rect, size) {
                        return getPosition(pos, params, dom, rect, size);
                    },
                    legend: {
                        show: false,
                    },
                    series: [
                        {
                            type: "pie",
                            radius: ["100%", "87%"],
                            avoidLabelOverlap: false,
                            hoverAnimation: false,
                            itemStyle: {
                                borderWidth: 2,
                                borderColor: utils.grays.white,
                            },
                            label: {
                                normal: {
                                    show: false,
                                    position: "center",
                                    textStyle: {
                                        fontSize: "20",
                                        fontWeight: "500",
                                        color: utils.grays["700"],
                                    },
                                },
                                emphasis: {
                                    show: false,
                                },
                            },
                            labelLine: {
                                normal: {
                                    show: false,
                                },
                            },
                            data: this.positions_data,
                        },
                    ],
                };

                var options = window._.merge(defaultOptions, userOptions);

                chart.setOption(options);
            }
        },
        addKeyword() {
            let _this = this;
            if (!_this.adding) {
                _this.adding = true;
                let fd = new FormData();
                fd.append("keyword", _this.keyword);
                fd.append("project", _this.project.id);
                axios
                    .post(`/data/keywords/`, fd)
                    .then((res) => {
                        _this.adding = false;
                        _this.addkw = false;
                        _this.keyword = "";
                        _this.getProject(_this.$route.params.id);
                        toastr.success("Keyword has been added and will be tracked.");
                        _this.getKeywords();
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
            }
        },
        deleteKeyword(deleteKeyword) {
            let _this = this;
            _this.delete_confirm = true;
            _this.delete_key_id = deleteKeyword;
        },
        confirmDelete(deleteKeyword) {
            let _this = this;
            axios
                .delete(`/data/keywords/${deleteKeyword}`)
                .then((res) => {
                    _this.getKeywords();
                    _this.getProject(_this.$route.params.id);
                    toastr.info("The keyword has been deleted.");
                })
                .catch((err) => {
                    toastr.error("The keyword cannot be deleted.");
                });
        },
        cancelDelete() {
            let _this = this;
            _this.delete_confirm = false;
            _this.delete_key_id = 0;
        
        },
        deleteProject() {
            let _this = this;
            if (!_this.deleting) {
                _this.deleting = true;
                let id = _this.$route.params.id;
                axios
                    .delete(`/data/projects/${id}`)
                    .then((res) => {
                        _this.deleting = false;
                        toastr.info("The project and associated data has been deleted.");
                        _this.$router.push({ name: "dashboard" });
                        _this.delete_confirm = false;
                    })
                    .catch((err) => {
                        _this.deleting = false;
                        toastr.error("The project cannot be deleted.");
                        _this.delete_confirm = false;

                    });
            }
    
        },
        getParameterByName(url, name) {
            var match = RegExp("[?&]" + name + "=([^&]*)").exec(url);
            return match && decodeURIComponent(match[1].replace(/\+/g, " "));
        },
        getKeywords() {
            let _this = this;
            let proj_id = _this.$route.params.id;
            if (_this.search) {
                _this.offset = "";
            }
            axios
                .get(
                    `/data/keywords?project_id=${proj_id}&offset=${_this.offset}&search=${_this.search}`
                )
                .then((res) => {
                    _this.keywords = res.data;
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
                })
                .catch((err) => {
                    toastr.error("Project keywords cannot be retrieved.");
                });
        },
        getImportKeywords() {
            let _this = this;
            let proj_id = _this.$route.params.id;
            if (_this.search) {
                _this.offset = "";
            }
            axios
                .get(
                    `/data/import-keyword?project_id=${proj_id}&offset=${_this.key_offset}&search=${_this.key_search}`
                )
                .then((res) => {
                    _this.importkeywords = res.data;
                    if (res.data.next) {
                        _this.key_next_offset = _this.getParameterByName(
                            res.data.next,
                            "offset"
                        );
                    } else {
                        _this.key_next_offset = false;
                    }
                    if (res.data.previous) {
                        let key_prev_offset = _this.getParameterByName(
                            res.data.previous,
                            "offset"
                        );
                        if (!key_prev_offset) {
                            key_prev_offset = "0";
                        }
                        _this.key_previous_offset = key_prev_offset;
                    } else {
                        _this.key_previous_offset = false;
                    }
                })
                .catch((err) => {
                    toastr.error("Import keywords files cannot be retrieved.");
                });
        },
        getProject(id) {
            let _this = this;
            if (!_this.is_busy) {
              // _this.is_busy=true;
                axios
                    .get(`/data/projects/${id}`)
                    .then((res) => {
                        _this.is_busy = false;
                        _this.project = res.data;
                        _this.total_keywords = _this.project.total_keywords;
                        _this.kw_avg_position = _this.project.avg_position;
                        _this.positions_data[0].value = _this.project.top_10;
                        _this.positions_data[1].value = _this.project.top_20;
                        _this.positions_data[2].value = _this.project.top_50;
                        _this.getKeywords();
                        _this.InitializeChart();
                    })
                    .catch((err) => {
                        _this.is_busy = false;
                        toastr.error("Project details cannot be retrieved.");
                    });
            }
        },
        importKeywords() {
            let _this = this;
            if (!_this.loading) {
                _this.importing = true;
                _this.errors = {};
                let csvfile = _this.$refs.csvfile.files[0];
                let fd = new FormData();
                fd.append("csvfile", csvfile);
                fd.append("project", _this.project.id);
                fd.append("filesource", _this.filesource);
                axios
                    .post(`/data/import-keyword/`, fd)
                    .then((res) => {
                        toastr.success(
                            "File has been imported and will be processed shortly."
                        );
                        _this.importing = false;
                        _this.importkws = false;
                        _this.getProject(_this.project.id);
                        _this.filesource = "plain_text";
                        this.getImportKeywords();
                    })
                    .catch((err) => {
                        _this.importing = false;
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
            }
        },
    },
};
</script>
