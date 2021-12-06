<template>
  <div class="card h-lg-100">
    <div class="card-body d-flex align-items-center">
      <div class="w-100">
        <h6 class="mb-3 text-800">
          {{ title }}
        </h6>
        <p>{{ text }}</p>
        <div
          class="progress mb-3 rounded-3"
          :style="'height: ' + height + 'px'"
        >
          <div
            v-for="value in values"
            :key="value.width"
            :class="
              'progress-bar ' +
              value.color +
              ' border-end border-white border-2'
            "
            role="progressbar"
            :style="'width:' + value.width + '%'"
            :aria-valuenow="value.width"
            aria-valuemin="0"
            aria-valuemax="100"
          ></div>
        </div>
        <div class="row fs--1 fw-semi-bold text-500 g-0">
          <div
            v-for="value in values"
            :key="value.width"
            class="col-auto d-flex align-items-center pe-3 px-1"
          >
            <span :class="' dot ' + value.color + ''"></span
            ><span>{{ value.name }}</span
            ><span class="d-none d-md-inline-block d-lg-none d-xxl-inline-block"
              >(895MB)</span
            >
          </div>
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
      default: "the main title",
    },
    text: {
      type: String,
      default: "some text",
    },
    height: {
      type: Number,
      default: 10,
    },
    values: {
      type: Array,
      default: () => [
        {
          width: 40,
          name: "Regular",
          color: "bg-primary",
        },
        {
          width: 20,
          name: "System",
          color: "bg-info",
        },
        {
          width: 10,
          name: "Shared",
          color: "bg-success",
        },
        {
          width: 30,
          name: "Shared",
          color: "bg-light",
        },
      ],
    },
  },
  mounted() {},
};
</script>
