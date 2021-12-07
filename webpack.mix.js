const mix = require('laravel-mix');

mix.js('resources/js/auth.js', 'static/dashboard/assets/js')
    .js('resources/js/portal.js', 'static/dashboard/assets/js');