<template>
    <div class="row">
        <div class="col-12">
            <div class="card mb-3">
                <div class="card-header bg-light">
                    <div class="row align-items-center justify-content-between">
                        <div class="col-12">
                            <h5 class="float-left pt-1 graphics_font">
                                My Projects
                                <!-- <span v-if="projects && projects.count && pagination" >
                                    ({{ projects.count }})
                                </span> -->
                            </h5>
                            <router-link
                                :to="{ name: 'newproject' }"
                                class="btn right btn-orange float-right text-white rounded"
                            >
                                <span
                                    class="fas fa-plus"
                                    data-fa-transform="shrink-3"
                                ></span>
                                New
                            </router-link>
                        </div>
                    </div>
                </div>
                <div class="card-body px-0 pt-0">
                    <div v-if="busy" class="row g-0 p-4 text-center">
                        <loading-component
                            :busy="busy"
                            bText="Loading projects..."
                        ></loading-component>
                    </div>
                    <div v-else>
                        <div
                            v-if="!projects || projects.count == 0"
                            class="row g-0 pt-4 text-center"
                        >
                            <h3 class="text-center text-muted">No projects found!</h3>
                        </div>
                        <div v-else class="row g-0">
                            <div class="table-responsive scrollbar">
                                <table
                                    class="table table-dashboard mb-0 table-striped table-hover border-200"
                                >
                                    <thead class="bg-primary gradient-dark text-white">
                                        <tr>
                                            <th class="th_weight_500">Title</th>
                                            <th class="th_weight_500">Keywords</th>
                                            <th class="th_weight_500">Health Score</th>
                                            <th class="th_weight_500" colspan="2">
                                                Created
                                            </th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr
                                            v-for="proj in projects.results"
                                            :key="proj.id"
                                            style="cursor:pointer;"
                                            @click="$router.push({name: 'projdetails', params:{id: proj.id}})"
                                        >
                                            <td>{{ proj.title }}</td>
                                            <td>{{ proj.total_keywords }}</td>
                                            <td>
                                                <span v-if="proj.health_score">{{
                                                    proj.health_score
                                                }}</span>
                                                <span v-else class="text-muted">N/A</span>
                                            </td>
                                            <td>{{ proj.created_at }}</td>
                                            <td class="text-right">
                                                <button class="btn btn-sm btn-black text-white rounded">
                                                    Manage
                                                </button>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
                <div v-if="pagination" class="card-footer bg-light text-right">
                    <button
                        :disabled="!previous_offset"
                        @click="(offset = previous_offset), getProjects()"
                        class="btn btn-falcon-default"
                    >
                        Previous
                    </button>
                    <button
                        :disabled="next_offset == false"
                        @click="(offset = next_offset), getProjects()"
                        class="btn btn-falcon-default"
                    >
                        Next
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { bus } from "../../../../portal.js";
export default {
    props: ["pagination"],
    data() {
        return {
            previous_offset: 0,
            offset: 0,
            next_offset: 0,
            projects: false,
            busy: false,
            q: ''
        };
    },
    mounted() {
        this.getProjects();
        let _this = this;
        bus.$on("searched", (q) => {
            _this.q = q;
            _this.offset = "";
            _this.getProjects();
        });
    },
    methods: {
        getProjects() {
            let _this = this;
            if (!_this.busy) {
                _this.busy = true;
                axios
                    .get(`/data/projects?q=${_this.q}`)
                    .then((res) => {
                        _this.busy = false;
                        _this.projects = res.data;
                    })
                    .catch((err) => {
                        _this.busy = false;
                        toastr.error("Projects list cannot be retrieved.");
                    });
            }
        },
    },
};
</script>
