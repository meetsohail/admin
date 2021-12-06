export const routes = [
    {
        path: '/login/',
        name: 'login',
        component: require('../components/auth/LoginComponent').default,
        meta: {
            title: 'Sign in'
        }
    },
    {
        path: '/register/',
        name: 'register',
        component: require('../components/auth/RegisterComponent').default,
        meta: {
            title: 'Create account'
        }
    },
    {
        path: '/reset-password/',
        name: 'reset',
        component: require('../components/auth/ResetComponent').default,
        meta: {
            title: 'Reset account password'
        }
    },
    {
        path: '/new-password/',
        name: 'newpass',
        component: require('../components/auth/NewPassword').default,
        meta: {
            title: 'Set new account password'
        }
    }
]