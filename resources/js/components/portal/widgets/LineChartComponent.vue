<template>
  <!-- <div class="card h-100">
    <div class="card-header bg-light d-flex flex-between-center py-2">
      <h6 class="mb-0">Bandwidth Saved</h6>
    </div>
    <div class="card-body d-flex flex-center flex-column"> -->
      <!-- chart -->
      <div id="mainline" style="width: 100%; height: 350px"></div>
     
    <!-- </div>
    <div class="card-footer bg-light py-2">
      <div class="row flex-between-center">
        <div class="col-auto">
          <select class="form-select form-select-sm">
            <option>Last 6 Months</option>
            <option>Last Year</option>
            <option>Last 2 Year</option>
          </select>
        </div>
      </div>
    </div>
  </div> -->
</template>
<script>
export default {
  props: {
    xAxis: {
      type: Array,
      default: ()=>['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis:{
      type: Array,
      default: ()=>[300, 389, 250, 560, 100, 600, 400]
    },
    chartType: {
      type: String,
      default: 'line'
    }
  },
  // data() {},
  mounted() {
    
var chartDom = document.getElementById('mainline');
var myChart = echarts.init(chartDom);
var option;

option = {
  xAxis: {
    type: 'category',
    data: this.xAxis
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      data: this.yAxis,
      type: this.chartType,
      smooth: true
    }
  ],
    tooltip: {
    trigger: 'item'
  },
};

option && myChart.setOption(option);

  },
};
</script>

