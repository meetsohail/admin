<template>
    <div>

            <!-- HEADER -->
            <div class="header">

                <div class="container-fluid">

                    <!-- Body -->
                    <div class="header-body">
                        <div class="row align-items-end">
                            <div class="col">

                                <!-- Pretitle -->
                                <h6 class="header-pretitle">
                                    Overview
                                </h6>

                                <!-- Title -->
                                <h1 class="header-title">
                                    Dashboard
                                </h1>

                            </div>
                            <div class="col-auto">

                                <!-- Button -->
                                <a href="#!" class="btn btn-primary lift">
                  Create Report
                </a>

                            </div>
                        </div>
                        <!-- / .row -->
                    </div>
                    <!-- / .header-body -->

                </div>
            </div>
            <!-- / .header -->

            <!-- CARDS -->
            <div class="container-fluid">
        <div class="row">
            <div class="col-12 col-lg-6 col-xl">
                <!-- Value  -->
                <div class="card">
                    <div class="card-body">
                        <div class="row align-items-center gx-0">
                            <div class="col">
    
                                <!-- Title -->
                                <h6 class="text-uppercase text-muted mb-2">
                                    Value
                                </h6>
    
                                <!-- Heading -->
                                <span class="h2 mb-0">
                          $24,500
                        </span>
    
                                <!-- Badge -->
                                <span class="badge bg-success-soft mt-n1">
                          +3.5%
                        </span>
                            </div>
                            <div class="col-auto">
    
                                <!-- Icon -->
                                <span class="h2 fe fe-dollar-sign text-muted mb-0"></span>
    
                            </div>
                        </div>
                        <!-- / .row -->
                    </div>
                </div>
            </div>
            <div class="col-12 col-lg-6 col-xl">
    
                <!-- Hours -->
                <div class="card">
                    <div class="card-body">
                        <div class="row align-items-center gx-0">
                            <div class="col">
    
                                <!-- Title -->
                                <h6 class="text-uppercase text-muted mb-2">
                                    Total hours
                                </h6>
    
                                <!-- Heading -->
                                <span class="h2 mb-0">
                          763.5
                        </span>
    
                            </div>
                            <div class="col-auto">
    
                                <!-- Icon -->
                                <span class="h2 fe fe-briefcase text-muted mb-0"></span>
    
                            </div>
                        </div>
                        <!-- / .row -->
                    </div>
                </div>
    
            </div>
            <div class="col-12 col-lg-6 col-xl">
    
                <!-- Exit -->
                <div class="card">
                    <div class="card-body">
                        <div class="row align-items-center gx-0">
                            <div class="col">
    
                                <!-- Title -->
                                <h6 class="text-uppercase text-muted mb-2">
                                    Exit %
                                </h6>
    
                                <!-- Heading -->
                                <span class="h2 mb-0">
                          35.5%
                        </span>
    
                            </div>
                            <div class="col-auto">
    
                                <!-- Chart -->
                                <div class="chart chart-sparkline">
                                    <canvas class="chart-canvas" id="sparklineChart"></canvas>
                                </div>
    
                            </div>
                        </div>
                        <!-- / .row -->
                    </div>
                </div>
    
            </div>
            <div class="col-12 col-lg-6 col-xl">
    
                <!-- Time -->
                <div class="card">
                    <div class="card-body">
                        <div class="row align-items-center gx-0">
                            <div class="col">
    
                                <!-- Title -->
                                <h6 class="text-uppercase text-muted mb-2">
                                    Avg. Time
                                </h6>
    
                                <!-- Heading -->
                                <span class="h2 mb-0">
                          2:37
                        </span>
    
                            </div>
                            <div class="col-auto">
    
                                <!-- Icon -->
                                <span class="h2 fe fe-clock text-muted mb-0"></span>
    
                            </div>
                        </div>
                        <!-- / .row -->
                    </div>
                </div>
    
            </div>
        </div>
    
        <!-- / .row -->
        <div class="row">
            <div class="col-12">
    
                <!-- Goals -->
                <div class="card">
                    <div class="card-header">
                        <div class="row align-items-center">
                            <div class="col">
    
                                <!-- Title -->
                                <h4 class="card-header-title">
                                    Goals
                                </h4>
    
                            </div>
                            <div class="col-auto">
    
                                <!-- Button -->
                                <a href="#!" class="btn btn-sm btn-white">
                          Export
                        </a>
    
                            </div>
                        </div>
                        <!-- / .row -->
                    </div>
                    <div class="table-responsive mb-0" data-list="{&quot;valueNames&quot;: [&quot;goal-project&quot;, &quot;goal-status&quot;, &quot;goal-progress&quot;, &quot;goal-date&quot;]}">
                        <table class="table table-sm table-nowrap card-table">
                            <thead>
                                <tr>
                                    <th>
                                        <a href="#" class="text-muted list-sort" data-sort="goal-project">
                              Goal
                            </a>
                                    </th>
                                    <th>
                                        <a href="#" class="text-muted list-sort" data-sort="goal-status">
                              Status
                            </a>
                                    </th>
                                    <th>
                                        <a href="#" class="text-muted list-sort" data-sort="goal-progress">
                              Progress
                            </a>
                                    </th>
                                    <th>
                                        <a href="#" class="text-muted list-sort" data-sort="goal-date">
                              Due date
                            </a>
                                    </th>
                                    <th class="text-end">
                                        Team
                                    </th>
                                    <th></th>
                                </tr>
                            </thead>
                            <tbody class="list">
                                <tr>
                                    <td class="goal-project">
                                        Update the API
                                    </td>
                                    <td class="goal-status">
                                        <span class="text-warning">●</span> In progress
                                    </td>
                                    <td class="goal-progress">
                                        55%
                                    </td>
                                    <td class="goal-date">
                                        <time datetime="2018-10-24">07/24/18</time>
                                    </td>
                                    <td class="text-end">
                                        <div class="avatar-group">
                                            <a href="profile-posts.html" class="avatar avatar-xs" data-bs-toggle="tooltip" title="Dianna Smiley">
                                <img src="/static/dashboard/assets/img/avatars/profiles/avatar-1.jpg" class="avatar-img rounded-circle" alt="...">
                              </a>
                                            <a href="profile-posts.html" class="avatar avatar-xs" data-bs-toggle="tooltip" title="Ab Hadley">
                                <img src="/static/dashboard/assets/img/avatars/profiles/avatar-2.jpg" class="avatar-img rounded-circle" alt="...">
                              </a>
                                            <a href="profile-posts.html" class="avatar avatar-xs" data-bs-toggle="tooltip" title="Adolfo Hess">
                                <img src="/static/dashboard/assets/img/avatars/profiles/avatar-3.jpg" class="avatar-img rounded-circle" alt="...">
                              </a>
                                            <a href="profile-posts.html" class="avatar avatar-xs" data-bs-toggle="tooltip" title="Daniela Dewitt">
                                <img src="/static/dashboard/assets/img/avatars/profiles/avatar-4.jpg" class="avatar-img rounded-circle" alt="...">
                              </a>
                                        </div>
                                    </td>
                                    <td class="text-end">
                                        <div class="dropdown">
                                            <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <i class="fe fe-more-vertical"></i>
                              </a>
                                            <div class="dropdown-menu dropdown-menu-end">
                                                <a href="#!" class="dropdown-item">
                                  Action
                                </a>
                                                <a href="#!" class="dropdown-item">
                                  Another action
                                </a>
                                                <a href="#!" class="dropdown-item">
                                  Something else here
                                </a>
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td class="goal-project">
                                        Release v1.2-Beta
                                    </td>
                                    <td class="goal-status">
                                        <span class="text-warning">●</span> In progress
                                    </td>
                                    <td class="goal-progress">
                                        25%
                                    </td>
                                    <td class="goal-date">
                                        <time datetime="2018-10-24">08/26/18</time>
                                    </td>
                                    <td class="text-end">
                                        <div class="avatar-group justify-content-end">
                                            <a href="#!" class="avatar avatar-xs" data-bs-toggle="tooltip" title="Dianna Smiley">
                                <img src="/static/dashboard/assets/img/avatars/profiles/avatar-1.jpg" class="avatar-img rounded-circle" alt="...">
                              </a>
                                            <a href="#!" class="avatar avatar-xs" data-bs-toggle="tooltip" title="Ab Hadley">
                                <img src="/static/dashboard/assets/img/avatars/profiles/avatar-2.jpg" class="avatar-img rounded-circle" alt="...">
                              </a>
                                            <a href="#!" class="avatar avatar-xs" data-bs-toggle="tooltip" title="Adolfo Hess">
                                <img src="/static/dashboard/assets/img/avatars/profiles/avatar-3.jpg" class="avatar-img rounded-circle" alt="...">
                              </a>
                                        </div>
                                    </td>
                                    <td class="text-end">
                                        <div class="dropdown">
                                            <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <i class="fe fe-more-vertical"></i>
                              </a>
                                            <div class="dropdown-menu dropdown-menu-end">
                                                <a href="#!" class="dropdown-item">
                                  Action
                                </a>
                                                <a href="#!" class="dropdown-item">
                                  Another action
                                </a>
                                                <a href="#!" class="dropdown-item">
                                  Something else here
                                </a>
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td class="goal-project">
                                        GDPR Compliance
                                    </td>
                                    <td class="goal-status">
                                        <span class="text-success">●</span> Completed
                                    </td>
                                    <td class="goal-progress">
                                        100%
                                    </td>
                                    <td class="goal-date">
                                        <time datetime="2018-10-24">06/19/18</time>
                                    </td>
                                    <td class="text-end">
                                        <div class="avatar-group justify-content-end">
                                            <a href="#!" class="avatar avatar-xs" data-bs-toggle="tooltip" title="Dianna Smiley">
                                <img src="/static/dashboard/assets/img/avatars/profiles/avatar-1.jpg" class="avatar-img rounded-circle" alt="...">
                              </a>
                                            <a href="#!" class="avatar avatar-xs" data-bs-toggle="tooltip" title="Ab Hadley">
                                <img src="/static/dashboard/assets/img/avatars/profiles/avatar-2.jpg" class="avatar-img rounded-circle" alt="...">
                              </a>
                                            <a href="#!" class="avatar avatar-xs" data-bs-toggle="tooltip" title="Adolfo Hess">
                                <img src="/static/dashboard/assets/img/avatars/profiles/avatar-3.jpg" class="avatar-img rounded-circle" alt="...">
                              </a>
                                        </div>
                                    </td>
                                    <td class="text-end">
                                        <div class="dropdown">
                                            <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <i class="fe fe-more-vertical"></i>
                              </a>
                                            <div class="dropdown-menu dropdown-menu-end">
                                                <a href="#!" class="dropdown-item">
                                  Action
                                </a>
                                                <a href="#!" class="dropdown-item">
                                  Another action
                                </a>
                                                <a href="#!" class="dropdown-item">
                                  Something else here
                                </a>
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td class="goal-project">
                                        v1.2 Documentation
                                    </td>
                                    <td class="goal-status">
                                        <span class="text-danger">●</span> Cancelled
                                    </td>
                                    <td class="goal-progress">
                                        0%
                                    </td>
                                    <td class="goal-date">
                                        <time datetime="2018-10-24">06/25/18</time>
                                    </td>
                                    <td class="text-end">
                                        <div class="avatar-group justify-content-end">
                                            <a href="#!" class="avatar avatar-xs" data-bs-toggle="tooltip" title="Dianna Smiley">
                                <img src="/static/dashboard/assets/img/avatars/profiles/avatar-1.jpg" class="avatar-img rounded-circle" alt="...">
                              </a>
                                            <a href="#!" class="avatar avatar-xs" data-bs-toggle="tooltip" title="Ab Hadley">
                                <img src="/static/dashboard/assets/img/avatars/profiles/avatar-2.jpg" class="avatar-img rounded-circle" alt="...">
                              </a>
                                        </div>
                                    </td>
                                    <td class="text-end">
                                        <div class="dropdown">
                                            <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <span class="fe fe-more-vertical"></span>
                              </a>
                                            <div class="dropdown-menu dropdown-menu-end">
                                                <a href="#!" class="dropdown-item">
                                  Action
                                </a>
                                                <a href="#!" class="dropdown-item">
                                  Another action
                                </a>
                                                <a href="#!" class="dropdown-item">
                                  Something else here
                                </a>
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td class="goal-project">
                                        Plan design offsite
                                    </td>
                                    <td class="goal-status">
                                        <span class="text-success">●</span> Completed
                                    </td>
                                    <td class="goal-progress">
                                        100%
                                    </td>
                                    <td class="goal-date">
                                        <time datetime="2018-10-24">06/30/18</time>
                                    </td>
                                    <td class="text-end">
                                        <div class="avatar-group justify-content-end">
                                            <a href="#!" class="avatar avatar-xs" data-bs-toggle="tooltip" title="Dianna Smiley">
                                <img src="/static/dashboard/assets/img/avatars/profiles/avatar-1.jpg" class="avatar-img rounded-circle" alt="...">
                              </a>
                                            <a href="#!" class="avatar avatar-xs" data-bs-toggle="tooltip" title="Ab Hadley">
                                <img src="/static/dashboard/assets/img/avatars/profiles/avatar-2.jpg" class="avatar-img rounded-circle" alt="...">
                              </a>
                                            <a href="#!" class="avatar avatar-xs" data-bs-toggle="tooltip" title="Adolfo Hess">
                                <img src="/static/dashboard/assets/img/avatars/profiles/avatar-3.jpg" class="avatar-img rounded-circle" alt="...">
                              </a>
                                            <a href="#!" class="avatar avatar-xs" data-bs-toggle="tooltip" title="Daniela Dewitt">
                                <img src="/static/dashboard/assets/img/avatars/profiles/avatar-4.jpg" class="avatar-img rounded-circle" alt="...">
                              </a>
                                        </div>
                                    </td>
                                    <td class="text-end">
                                        <div class="dropdown">
                                            <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <i class="fe fe-more-vertical"></i>
                              </a>
                                            <div class="dropdown-menu dropdown-menu-end">
                                                <a href="#!" class="dropdown-item">
                                  Action
                                </a>
                                                <a href="#!" class="dropdown-item">
                                  Another action
                                </a>
                                                <a href="#!" class="dropdown-item">
                                  Something else here
                                </a>
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
    
            </div>
        </div>
        <!-- / .row -->
        <div class="row">
            <div class="col-12 col-xl-5">
    
                <!-- Activity -->
                <div class="card card-fill">
                    <div class="card-header">
    
                        <!-- Title -->
                        <h4 class="card-header-title">
                            Recent Activity
                        </h4>
    
                        <!-- Button -->
                        <a class="small" href="#!">View all</a>
    
                    </div>
                    <div class="card-body">
    
                        <!-- List group -->
                        <div class="list-group list-group-flush list-group-activity my-n3">
                            <div class="list-group-item">
                                <div class="row">
                                    <div class="col-auto">
    
                                        <!-- Avatar -->
                                        <div class="avatar avatar-sm avatar-online">
                                            <img class="avatar-img rounded-circle" src="/static/dashboard/assets/img/avatars/profiles/avatar-1.jpg" alt="..." />
                                        </div>
    
                                    </div>
                                    <div class="col ms-n2">
    
                                        <!-- Heading -->
                                        <h5 class="mb-1">
                                            Dianna Smiley
                                        </h5>
    
                                        <!-- Text -->
                                        <p class="small text-gray-700 mb-0">
                                            Uploaded the files "Launchday Logo" and "New Design".
                                        </p>
    
                                        <!-- Time -->
                                        <small class="text-muted">
                              2m ago
                            </small>
    
                                    </div>
                                </div>
                                <!-- / .row -->
                            </div>
                            <div class="list-group-item">
                                <div class="row">
                                    <div class="col-auto">
    
                                        <!-- Avatar -->
                                        <div class="avatar avatar-sm avatar-online">
                                            <img class="avatar-img rounded-circle" src="/static/dashboard/assets/img/avatars/profiles/avatar-2.jpg" alt="..." />
                                        </div>
    
                                    </div>
                                    <div class="col ms-n2">
    
                                        <!-- Heading -->
                                        <h5 class="mb-1">
                                            Ab Hadley
                                        </h5>
    
                                        <!-- Text -->
                                        <p class="small text-gray-700 mb-0">
                                            Shared the "Why Dashkit?" post with 124 subscribers.
                                        </p>
    
                                        <!-- Time -->
                                        <small class="text-muted">
                              1h ago
                            </small>
    
                                    </div>
                                </div>
                                <!-- / .row -->
                            </div>
                            <div class="list-group-item">
                                <div class="row">
                                    <div class="col-auto">
    
                                        <!-- Avatar -->
                                        <div class="avatar avatar-sm avatar-offline">
                                            <img class="avatar-img rounded-circle" src="/static/dashboard/assets/img/avatars/profiles/avatar-3.jpg" alt="..." />
                                        </div>
    
                                    </div>
                                    <div class="col ms-n2">
    
                                        <!-- Heading -->
                                        <h5 class="mb-1">
                                            Adolfo Hess
                                        </h5>
    
                                        <!-- Text -->
                                        <p class="small text-gray-700 mb-0">
                                            Exported sales data from Launchday's subscriber data.
                                        </p>
    
                                        <!-- Time -->
                                        <small class="text-muted">
                              3h ago
                            </small>
    
                                    </div>
                                </div>
                                <!-- / .row -->
                            </div>
                        </div>
    
                    </div>
                </div>
    
            </div>
            <div class="col-12 col-xl-7">
    
                <!-- Checklist -->
                <div class="card">
                    <div class="card-header">
    
                        <!-- Title -->
                        <h4 class="card-header-title">
                            Scratchpad Checklist
                        </h4>
    
                        <!-- Badge -->
                        <span class="badge bg-secondary-soft">
                      23 Archived
                    </span>
    
                    </div>
                    <div class="card-body">
    
                        <!-- Checklist -->
                        <div class="checklist">
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="checklistOne">
                                <label class="form-check-label">Delete the old mess in functions files.</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="checklistTwo">
                                <label class="form-check-label">Refactor the core social sharing modules.</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="checklistThree">
                                <label class="form-check-label">Create the release notes for the new pages so customers get psyched.</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="checklistFour">
                                <label class="form-check-label">Send Dianna those meeting notes.</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="checklistFive">
                                <label class="form-check-label">Share the documentation for the new unified API.</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="checklistSix" checked>
                                <label class="form-check-label">Clean up the Figma file with all of the avatars, buttons, and other
                          components.</label>
                            </div>
                        </div>
    
                    </div>
                    <div class="card-footer">
                        <div class="row align-items-center">
                            <div class="col">
    
                                <!-- Input -->
                                <textarea class="form-control form-control-flush form-control-auto" data-autosize rows="1" placeholder="Create a task"></textarea>
    
                            </div>
                            <div class="col-auto">
    
                                <!-- Button -->
                                <button class="btn btn-sm btn-primary">
                          Add
                        </button>
    
                            </div>
                        </div>
                        <!-- / .row -->
                    </div>
                </div>
    
            </div>
        </div>
        <!-- / .row -->
    </div>
    </div>
</template>

<script>
// import ProjectsTable from '../projects/partials/ProjectsTable';
export default {

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

    }
};
</script>