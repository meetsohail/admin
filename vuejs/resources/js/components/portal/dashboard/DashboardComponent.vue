<template>
    <div>
        <projects-table :pagination="true"></projects-table>
    </div>
</template>
<script>
import ProjectsTable from '../projects/partials/ProjectsTable';
export default {
    components: {
      ProjectsTable
    },
    data() {
        return {
            statistics: {
                complete: 0,
                queued: 0,
                inprogress: 0
            },
            stats_gen: false
        }
    },
    mounted() {
        this.$store.commit('setUser');
        if(this.$store.state.user && this.$store.state.user.statistics) {
            let _stats = this.$store.state.user.statistics;
            this.stats_gen = _stats;
            if(typeof(_stats.jobs) != 'undefined') {
                let _ps = _stats.jobs;
                if(_ps) {
                    this.statistics = {
                        queued: parseFloat(this.getPercentage(_ps.queued, _ps.total)),
                        inprogress: parseFloat(this.getPercentage(_ps.inprogress, _ps.total)),
                        complete: parseFloat(this.getPercentage(_ps.complete, _ps.total)),
                        failed: parseFloat(this.getPercentage(_ps.failed, _ps.total)),
                    }
                }
            }
        }
    }
};
</script>