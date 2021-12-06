require('./bootstrap');

window.Vue = require('vue');
window.axios.defaults.baseURL = '/auth/';

import VueRouter from 'vue-router';
Vue.use(VueRouter);

import { routes } from './routes/auth';
const router = new VueRouter({
    mode: 'history',
    routes: routes,
    base: '/auth/'
});

import { store } from './store';

const app = new Vue({
    el: '#app',
    store: store,
    router: router
});
