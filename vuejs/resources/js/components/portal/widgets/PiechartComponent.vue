<template>
  <div class="card h-100">
    <!-- <div class="card-header bg-light d-flex flex-between-center py-2">
      <h6 class="mb-0">Bandwidth Saved</h6>
    </div> -->
    <!-- <div class="card-body d-flex flex-center flex-column"> -->
      <!-- chart -->
      <div id="main" style="width: 100%; height: 400px"></div>
      <div class="text-center mt-3">
        <p v-if="caption != '' " class="fs--1 mb-0">{{ caption }}</p>
      </div>
    <!-- </div> -->
    <!-- <div class="card-footer bg-light py-2">
      <div class="row flex-between-center">
        <div class="col-auto">
          <select  class="form-select form-select-sm" >
            <option value="2 Months">Last 6 Months</option>
            <option value="3 Months">Last Year</option>
            <option value="4 Yonths">Last 2 Year</option>
          </select>
        </div>
      </div>
    </div> -->
  </div>
</template>
<script>
export default {
  props: {
    title: {
      type: String,
      default: "Pie Chart Title edited"
    },
    tooltip:{
      type: String,
      default: "Access From"
    },
    caption:{
      type: String,
      default: "38.44 GB total bandwidth l"
    },
    values:{
      type: Array,
      default: () =>[
            { value: 335, name: "Direct j" },
            { value: 310, name: "Email k" },
            { value: 274, name: "Union Ads l" },
            { value: 235, name: "Video Ads" },
            { value: 400, name: "Search Engine hhhS" },
          ]
    }
  },
  
  mounted() {
    var chartDom = document.getElementById("main");
    var myChart = echarts.init(chartDom);
    var option;

    option = {
      backgroundColor: "#2c343c",
      title: {
        text: this.title,
        left: "center",
        top: 20,
        textStyle: {
          color: "#ccc",
        },
      },
      tooltip: {
        trigger: "item",
      },
      visualMap: {
        show: false,
        min: 80,
        max: 600,
        inRange: {
          colorLightness: [0, 1],
        },
      },
      series: [
        {
          name: this.tooltip,
          type: "pie",
          radius: "55%",
          center: ["50%", "50%"],
          data: this.values.sort(function (a, b) {
            return a.value - b.value;
          }),
          roseType: "radius",
          label: {
            color: "rgba(255, 255, 255, 0.3)",
          },
          labelLine: {
            lineStyle: {
              color: "rgba(255, 255, 255, 0.3)",
            },
            smooth: 0.2,
            length: 10,
            length2: 20,
          },
          itemStyle: {
            color: "#c23531",
            shadowBlur: 200,
            shadowColor: "rgba(0, 0, 0, 0.5)",
          },
          animationType: "scale",
          animationEasing: "elasticOut",
          animationDelay: function (idx) {
            return Math.random() * 200;
          },
        },
      ],
    };

    option && myChart.setOption(option);
  },
};
</script>

