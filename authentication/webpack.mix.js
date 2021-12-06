const mix = require('laravel-mix');

mix.js('resources/js/auth.js', 'static/falcon/assets/js')
    .js('resources/js/portal.js', 'static/falcon/assets/js')
    .sass('resources/sass/theme.scss', 'static/falcon/assets/css');
