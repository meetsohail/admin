const mix = require('laravel-mix');

mix.js('resources/js/auth.js', 'authentication/static/authentication/assets/js')
    .js('resources/js/portal.js', 'dashboard/static/dashboard/assets/js');