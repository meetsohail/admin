<template>
    <div class="echart-line-total-sales h-100" data-echart-responsive="true"></div>
</template>
<script>
export default {
    props: ['types', 'itemstats', 'xdata'],
    mounted() {
        this.initChart();
    },
    methods: {
        initChart() {
            let _this = this;
            var totalSales = function totalSales() {
                var ECHART_LINE_TOTAL_SALES = ".echart-line-total-sales";
                var SELECT_MONTH = ".select-type";
                var $echartsLinetotalSales = document.querySelector(
                    ECHART_LINE_TOTAL_SALES
                );
                var days = _this.types;
                function getFormatter(params) {
                    var _params$ = params[0],
                        name = _params$.name,
                        value = _params$.value;
                    var date = new Date(name);
                    return ""
                        .concat(days[0], " ")
                        .concat(date.getDate(), ", ")
                        .concat(value);
                }

                if ($echartsLinetotalSales) {
                    var userOptions = utils.getData(
                        $echartsLinetotalSales,
                        "options"
                    );
                    var chart = window.echarts.init($echartsLinetotalSales);
                    var itemstats = _this.itemstats;
                    var defaultOptions = {
                        color: utils.grays.white,
                        tooltip: {
                            trigger: "axis",
                            padding: [7, 10],
                            backgroundColor: utils.grays.white,
                            borderColor: utils.grays["300"],
                            borderWidth: 1,
                            textStyle: {
                                color: utils.colors.dark,
                            },
                            formatter: function formatter(params) {
                                return getFormatter(params);
                            },
                            transitionDuration: 0,
                            position: function position(
                                pos,
                                params,
                                dom,
                                rect,
                                size
                            ) {
                                return getPosition(
                                    pos,
                                    params,
                                    dom,
                                    rect,
                                    size
                                );
                            },
                        },
                        xAxis: {
                            type: "category",
                            data: _this.xdata,
                            boundaryGap: false,
                            axisPointer: {
                                lineStyle: {
                                    color: utils.grays["300"],
                                    type: "dashed",
                                },
                            },
                            splitLine: {
                                show: false,
                            },
                            axisLine: {
                                lineStyle: {
                                    color: utils.rgbaColor("#000", 0.01),
                                    type: "dashed",
                                },
                            },
                            axisTick: {
                                show: false,
                            },
                            axisLabel: {
                                color: utils.grays["400"],
                                formatter: function formatter(value) {
                                    var date = new Date(value);
                                    return ""
                                        .concat(days[date.getMonth()], " ")
                                        .concat(date.getDate());
                                },
                                margin: 15,
                            },
                        },
                        yAxis: {
                            type: "value",
                            axisPointer: {
                                show: false,
                            },
                            splitLine: {
                                lineStyle: {
                                    color: utils.grays["300"],
                                    type: "dashed",
                                },
                            },
                            boundaryGap: false,
                            axisLabel: {
                                show: true,
                                color: utils.grays["400"],
                                margin: 15,
                            },
                            axisTick: {
                                show: false,
                            },
                            axisLine: {
                                show: false,
                            },
                        },
                        series: [
                            {
                                type: "line",
                                data: itemstats[0],
                                lineStyle: {
                                    color: utils.colors.primary,
                                },
                                itemStyle: {
                                    borderColor: utils.colors.primary,
                                    borderWidth: 2,
                                },
                                symbol: "circle",
                                symbolSize: 10,
                                smooth: false,
                                hoverAnimation: true,
                                areaStyle: {
                                    color: {
                                        type: "linear",
                                        x: 0,
                                        y: 0,
                                        x2: 0,
                                        y2: 1,
                                        colorStops: [
                                            {
                                                offset: 0,
                                                color: utils.rgbaColor(
                                                    utils.colors.primary,
                                                    0.2
                                                ),
                                            },
                                            {
                                                offset: 1,
                                                color: utils.rgbaColor(
                                                    utils.colors.primary,
                                                    0
                                                ),
                                            },
                                        ],
                                    },
                                },
                            },
                        ],
                        grid: {
                            right: "28px",
                            left: "40px",
                            bottom: "15%",
                            top: "5%",
                        },
                    };
                    var options = window._.merge(defaultOptions, userOptions);
                    chart.setOption(options);
                }
            };
            docReady(totalSales);
        }
    }
}
</script>