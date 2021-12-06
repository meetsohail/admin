<template>
    <li class="nav-item dropdown dropdown-on-hover">
        <a class="nav-link notification-indicator notification-indicator-primary px-0 icon-indicator"
            id="navbarDropdownNotification" href="#" role="button" data-toggle="dropdown" aria-haspopup="true"
            aria-expanded="false"><span class="fas fa-bell fs-4" data-fa-transform="shrink-6"></span></a>
        <div class="dropdown-menu dropdown-menu-right dropdown-menu-card"
            aria-labelledby="navbarDropdownNotification">
            <div class="card card-notification shadow-none">
                <div class="card-header">
                    <div class="row justify-content-between align-items-center">
                        <div class="col-auto">
                            <h6 class="card-header-title mb-0">Notifications</h6>
                        </div>
                        <div class="col-auto"><a class="card-link font-weight-normal" href="#">Mark
                                all as read</a></div>
                    </div>
                </div>
                <div class="list-group list-group-flush font-weight-normal fs--1">
                    <div class="list-group-title border-bottom">NEW</div>
                    <div class="list-group-item">
                        <a class="notification notification-flush notification-unread" href="#!">
                            <div class="notification-avatar">
                                <div class="avatar avatar-2xl mr-3">
                                    <!-- <img class="rounded-circle" src="/assets/img/team/1-thumb.png" alt="" /> -->
                                </div>
                            </div>
                            <div class="notification-body">
                                <p class="mb-1"><strong>Emma Watson</strong> replied to your comment
                                    : "Hello world 😍"</p>
                                <span class="notification-time"><span class="mr-1" role="img"
                                        aria-label="Emoji">💬</span>Just now</span>

                            </div>
                        </a>
                    </div>
                </div>
                <div class="card-footer text-center border-top"><a class="card-link d-block"
                        href="javascript:void(0)">View all</a></div>
            </div>
        </div>
    </li>
</template>
<script>
export default {
    
}
</script>