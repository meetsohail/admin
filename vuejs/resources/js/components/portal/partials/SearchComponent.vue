<template>
    <div class="search-box">
        <input @keyup.enter="doSearch()" v-model="q" class="form-control rounded-pill search-input" type="search" placeholder="Search projects..." aria-label="Search" /><span class="position-absolute fas fa-search text-400 search-box-icon"></span>
    </div>
</template>
<script>
import { bus } from '../../../portal.js';
export default {
    data() {
        return {
            q: ''
        }
    },
    methods: {
        doSearch() {
            if(this.$route.name != 'dashboard') {
                this.$router.push({name: 'dashboard'});
            }
            bus.$emit('searched', this.q);
        }
    }
}
</script>