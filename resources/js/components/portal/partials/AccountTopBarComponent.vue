<template>
    <div class="row align-items-center">
                  <div class="col">

                    <!-- Nav -->
                    <ul class="nav nav-tabs nav-overflow header-tabs">
                      <li class="nav-item">
                        <router-link :to="{name:'profile'}" class="nav-link" v-bind:class="$route.name == 'profile' ? 'active' : ''">
                          General
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link :to="{name:'billing'}" class="nav-link" v-bind:class="$route.name == 'billing' ? 'active' : ''">
                          Billing
                        </router-link>
                      </li>
                     
                      <li class="nav-item">
                        <a href="account-security.html" class="nav-link">
                          Security
                        </a>
                      </li>
                      <li class="nav-item">
                        <a href="account-notifications.html" class="nav-link">
                          Notifications
                        </a>
                      </li>
                    </ul>

                  </div>
                </div>
</template>
<script>
export default {
    
}
</script>