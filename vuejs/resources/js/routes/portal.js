export const routes = [
    {
        path: '/test',
        name: 'bar',
        component: require('../components/portal/widgets/LinechartComponent').default,
        meta: {
            title: 'Bar chart'
        }
    },
    {
        path: '/',
        name: 'dashboard',
        component: require('../components/portal/dashboard/DashboardComponent').default,
        meta: {
            title: 'Dashboard Home'
        }
    },
    {
        path: '/new-project',
        name: 'newproject',
        component: require('../components/portal/projects/NewComponent').default,
        meta: {
            title: 'New Project'
        }
    },
    {
        path: '/project/:id',
        name: 'projdetails',
        component: require('../components/portal/projects/ProjectComponent').default,
        meta: {
            title: 'Project Details'
        }
    },
    {
        path: '/project/keyword/:id',
        name: 'keyworddetails',
        component: require('../components/portal/projects/keyword/KeywordComponent').default,
        meta: {
            title: 'Keyword Details'
        }
    },
    {
        path: '/profile-settings',
        name: 'profile',
        component: require('../components/portal/profile/ProfileComponent').default,
        meta: {
            title: 'Profile Settings'
        }
    },
    {
        path: '/billing-settings',
        name: 'billing',
        component: require('../components/portal/billing/BillingComponent').default,
        meta: {
            title: 'Billing Settings'
        }
    },
    {
        path: '/subscriptions',
        name: 'subscription',
        component: require('../components/portal/subscription/ProductComponent').default,
        meta: {
            title: 'Subscriptions'
        }
    },
    {
        path: '/api-keys',
        name: 'apikeys',
        component: require('../components/portal/profile/KeysComponent').default,
        meta: {
            title: 'API Keys'
        }
    },
    {
        path: '/my-invoices',
        name: 'invoices',
        component: require('../components/portal/billing/InvoicesComponent').default,
        meta: {
            title: 'My Invoices'
        }
    },
    {
        path: '/manage-users',
        name: 'users',
        component: require('../components/portal/users/UsersComponent').default,
        meta: {
            title: 'Manage Users'
        }
    },
    {
        path: '/update-user/:id',
        name: 'updateuser',
        component: require('../components/portal/users/SettingsComponent').default,
        meta: {
            title: 'Update User'
        }
    }
]