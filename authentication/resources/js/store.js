require('./bootstrap');

window.Vue = require('vue');

import Vuex from 'vuex';
Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        user: JSON.parse(localStorage.getItem('user'))
    },
    mutations: {
        setUser(state) {
            axios.defaults.baseURL = '/api/';
            axios.get('/users/user/').then((res) => {
                localStorage.setItem('user', JSON.stringify(res.data));
                state.user = res.data;
            }).catch((err) => {});
        },
        unsetUser(state) {
            localStorage.removeItem('user');
            state.user = null;
        }
    }
});