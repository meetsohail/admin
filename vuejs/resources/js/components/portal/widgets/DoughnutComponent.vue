<template>
  <div class="card h-100">
    <div class="card-header bg-light d-flex flex-between-center py-2">
      <h6 class="mb-0">{{ title }}</h6>
    </div>
    <div class="card-body d-flex flex-center flex-column">
      <!-- chart -->
      <div id="main" style="width: 100%; height: 400px"></div>
     
    </div>
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
  </div>
</template>
<script>
export default {
    props: {
        title: {
            type: String,
            default: 'Simple Pie Chart'
        },
        data:{
            type: Array,
            default: () => [
            { value: 1048, name: 'Search Engine' },
            { value: 735, name: 'Direct' },
            { value: 580, name: 'Email' },
            { value: 484, name: 'Union Ads' },
            { value: 300, name: 'Video Ads' }
      ]
        },

    },
    mounted() {
        // import * as echarts from 'echarts';

var chartDom = document.getElementById('main');
var myChart = echarts.init(chartDom);
var option;

option = {
  tooltip: {
    trigger: 'item'
  },
  legend: {
    top: '5%',
    left: 'center'
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
      label: {
        show: 0,
        position: 'center'
      },
      emphasis: {
        label: {
          show: true,
          fontSize: '20',
          fontWeight: 'bold'
        }
      },
      labelLine: {
        show: false
      },
      data: this.data
    }
  ]
};

option && myChart.setOption(option);
    },
}

</script>
