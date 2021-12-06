<template>
  <!-- <div class="card h-100">
    <div class="card-header bg-light d-flex flex-between-center py-2">
      <h6 class="mb-0">Bandwidth Saved</h6>
    </div>
     <div class="card-body d-flex flex-center flex-column">  -->
      <!-- chart -->
      <div id="main" :style=" 'width: 100%; height: '+ graphWidth+'px' "></div>
<!--      
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
  </div>  -->
</template>
<script>
export default {
  props: {
    graphWidth: {
      type:Number,
      default:150
    },
    score: {
      type: Number,
      default: 99
    },
    outerCircleRadius:{
      type: Number,
      default: 60
    },
    innerCircleRadius:{
      type: Number,
      default: 50
    },
    fontSize:{
      type: Number,
      default: 30
    },
     fontWeight:{
      type: Number,
      default: 300
    },
  },
  data() {
    return{
      animationDuration: 2000,

    }
  },
  mounted() {
var _panelImageURL = 'https://echarts.apache.org/examples/data/asset/img/custom-gauge-panel.png';
let _this = this;
var chartDom = document.getElementById('main');
var myChart = echarts.init(chartDom);
var option;

var _panelImageURL = _panelImageURL;
var _animationDuration = this.animationDuration;
var _animationDurationUpdate = 1000;
var _animationEasingUpdate = 'quarticInOut';
var _valOnRadianMax = 200;
var _outerRadius = this.outerCircleRadius;
var _innerRadius = 50;
var _pointerInnerRadius = 40;
var _insidePanelRadius = this.innerCircleRadius;
var _currentDataIndex = 0;
function renderItem(params, api) {
  var valOnRadian = api.value(1);
  var coords = api.coord([api.value(0), valOnRadian]);
  var polarEndRadian = coords[3];
  var imageStyle = {
    image: _panelImageURL,
    x: params.coordSys.cx - _outerRadius,
    y: params.coordSys.cy - _outerRadius,
    width: _outerRadius * 2,
    height: _outerRadius * 2
  };
  return {
 
    type: 'group',
    children: [
      {
        type: 'image',
        style: imageStyle,
        clipPath: {
          type: 'sector',
          shape: {
            cx: params.coordSys.cx,
            cy: params.coordSys.cy,
            r: _outerRadius,
            r0: _innerRadius,
            startAngle: 0,
            endAngle: -polarEndRadian,
            transition: 'endAngle',
            enterFrom: { endAngle: 0 }
          }
        }
      },
      {
        type: 'image',
        style: imageStyle,
        clipPath: {
          type: 'polygon',
          shape: {
            points: makePionterPoints(params, polarEndRadian)
          },
          extra: {
            polarEndRadian: polarEndRadian,
            transition: 'polarEndRadian',
            enterFrom: { polarEndRadian: 0 }
          },
          during: function (apiDuring) {
            apiDuring.setShape(
              'points',
              makePionterPoints(params, apiDuring.getExtra('polarEndRadian'))
            );
          }
        }
      },
      {
        type: 'circle',
        shape: {
          cx: params.coordSys.cx,
          cy: params.coordSys.cy,
          r: _insidePanelRadius
        },
        style: {
          fill: '#fff',
          shadowBlur: 25,
          shadowOffsetX: 0,
          shadowOffsetY: 0,
          shadowColor: 'rgba(76,107,167,0.4)'
        }
      },
      {
        type: 'text',
        extra: {
          valOnRadian: valOnRadian,
          transition: 'valOnRadian',
          enterFrom: { valOnRadian: 0 }
        },
        style: {
          text: makeText(valOnRadian),
          fontSize: _this.fontSize,
          fontWeight: _this.fontWeight,
          x: params.coordSys.cx,
          y: params.coordSys.cy,
          fill: 'rgb(0,50,190)',
          align: 'center',
          verticalAlign: 'middle',
          enterFrom: { opacity: 0 }
        },
        during: function (apiDuring) {
          apiDuring.setStyle(
            'text',
            makeText(apiDuring.getExtra('valOnRadian'))
          );
        }
      }
    ]
  };
}
function convertToPolarPoint(renderItemParams, radius, radian) {
  return [
    Math.cos(radian) * radius + renderItemParams.coordSys.cx,
    -Math.sin(radian) * radius + renderItemParams.coordSys.cy
  ];
}
function makePionterPoints(renderItemParams, polarEndRadian) {
  return [
    convertToPolarPoint(renderItemParams, _outerRadius, polarEndRadian),
    convertToPolarPoint(
      renderItemParams,
      _outerRadius,
      polarEndRadian + Math.PI * 0.03
    ),
    convertToPolarPoint(renderItemParams, _pointerInnerRadius, polarEndRadian)
  ];
}
function makeText(valOnRadian) {
  // Validate additive animation calc.
  if (valOnRadian < -10) {
    alert('illegal during val: ' + valOnRadian);
  }
  return ((valOnRadian / _valOnRadianMax) * 100).toFixed(0) + '%';
}
option = {
  animationEasing: _animationEasingUpdate,
  animationDuration: _animationDuration,
  animationDurationUpdate: _animationDurationUpdate,
  animationEasingUpdate: _animationEasingUpdate,
  dataset: {
    source: [[1, this.score * 2]]
  },
  tooltip: {},
  angleAxis: {
    type: 'value',
    startAngle: 0,
    show: false,
    min: 0,
    max: _valOnRadianMax
  },
  radiusAxis: {
    type: 'value',
    show: false
  },
  polar: {},
  series: [
    {
      type: 'custom',
      coordinateSystem: 'polar',
      renderItem: renderItem
    }
  ]
};
// setInterval(function () {
//   var nextSource = [[1, Math.round(Math.random() * _valOnRadianMax)]];
//   console.log(_panelImageURL);

//   myChart.setOption({
//     dataset: {
//       source: nextSource
//     }
//   });
// }, 3000);

option && myChart.setOption(option);

  },
};
</script>

