<template>
  <projects-table :pagination="true"></projects-table>
</template>
<script>
import ProjectsTable from './partials/ProjectsTable.vue';
export default {
  components: {
    ProjectsTable,
  }
};
</script>
