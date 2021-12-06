const mix = require('laravel-mix');

mix.js('resources/js/auth.js', 'static/vuejs/assets/js')
    .js('resources/js/portal.js', 'static/vuejs/assets/js');
