require('./bootstrap');

window.Vue = require('vue');
window.axios.defaults.baseURL = '/api/';

export const bus = new Vue();

import VueRouter from 'vue-router';
Vue.use(VueRouter);

import vSelect from 'vue-select';
Vue.component('v-select', vSelect);

Vue.filter('toCurrency', function(value) {
    value = parseFloat(value);
    var formatter = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 2
    });
    return formatter.format(value);
});

Vue.filter('toNumber', function(value) {
    if (typeof value !== "number") {
        return value;
    }
    var formatter = new Intl.NumberFormat('en-US');
    return formatter.format(value);
});

import { routes } from './routes/portal';
const router = new VueRouter({
    mode: 'history',
    routes: routes,
    base: '/dashboard/'
});

import { store } from './store';

Vue.component('search-component', require('./components/portal/partials/SearchComponent').default);
Vue.component('notifications-component', require('./components/portal/partials/NotificationsComponent').default);
Vue.component('loading-component', require('./components/global/LoadingComponent').default);
Vue.component('chart-component', require('./components/global/ChartComponent').default);
Vue.component('alert-component', require('./components/global/AlertComponent').default);
Vue.component('billing-credit', require('./components/global/BillingCreditComponent').default);
Vue.component('progressbar-widget', require('./components/portal/widgets/ProgressbarComponent.vue').default);
Vue.component('line-widget', require('./components/portal/widgets/LinechartComponent.vue').default);
Vue.component('health-widget', require('./components/portal/widgets/HealthchartComponent.vue').default);
Vue.component('pie-widget', require('./components/portal/widgets/PiechartComponent.vue').default);
Vue.component('accounts-topbar', require('./components/portal/partials/AccountTopBarComponent.vue').default);
Vue.component('invoices', require('./components/portal/billing/InvoicesComponent.vue').default);

Vue.mixin({
    data() {
        return {
            alertclass: '',
            alertmessage: ''
        }
    },
    methods: {
        getPercentage(numA, numB) {
            return parseFloat(parseFloat(numA) / parseFloat(numB) * 100);
        }
    }
});

const app = new Vue({
    el: '#app',
    store: store,
    router: router,
    mounted() {
        this.$store.commit('setUser');
    },
    methods: {
        signOut() {
            let _this = this;
            axios.defaults.baseURL = '/dashboard/';
            axios.get('/logout/').then((res) => {
                _this.$store.commit('unsetUser');
                window.location = '';
            }).catch((err) => {});
        }
    }
});