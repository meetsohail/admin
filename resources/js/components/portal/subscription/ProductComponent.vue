<template>
    <div>
        <!-- HEADER -->
        <div class="pt-7 pb-8 bg-dark bg-ellipses">
            <div class="container-fluid">
                <div class="row justify-content-center">
                    <div class="col-md-10 col-lg-8 col-xl-6">
                        <h1 class="display-3 text-center text-white">
                            Plans & Pricing
                        </h1>
                        <p class="lead text-center text-muted">
                            We have plans and prices that fit your business perfectly. Make your client site a success with our products.
                        </p>
    
                    </div>
                </div>
            </div>
        </div>
        <div class="container-fluid">
            <div class="row mt-n7" v-if="!$store.state.user.payment_method_id">
                <div class="col-12 col-lg-23">
                    <div class="card">
                        <div class="card-body">
                            <div class="alert alert-warning">Please update your payment method first to subscribe!
                                <router-link :to="{name: 'billing'}" class="btn btn-info btn-sm">
                                    <i class="fas fa-credit-card"></i> Billing Settings
                                </router-link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row mt-n7" v-else>
                <div class="col-12 mb-3">
                    <div v-if="successmsg" class="alert alert-success" role="alert">{{message}}</div>
                    <div v-if="errormsg" class="alert alert-danger" role="alert">{{message}}</div>
                </div>
                <div class="col-12 col-lg-4" v-if="products" v-for="product in products" :key="product.id">
                    <div class="card">
                        <div class="card-body">
                            <h6 class="text-uppercase text-center text-muted my-4">
                                {{product.product_name}}
                            </h6>
                            <div class="row g-0 align-items-center justify-content-center">
                                <div class="col-auto">
                                    <div class="h2 mb-0">$</div>
                                </div>
                                <div class="col-auto">
                                    <div class="display-2 mb-0">{{product.product_price}}</div>
                                </div>
                            </div>
                            <div class="h6 text-uppercase text-center text-muted mb-5">
                                / month
                            </div>
                            <div class="mb-3">
                                <ul class="list-group list-group-flush">
                                    <li class="list-group-item d-flex align-items-center justify-content-between px-0">
                                        <small v-html="product.product_description">Unlimited activity</small> <i class="fe fe-check-circle text-success"></i>
                                    </li>
                                    <li class="list-group-item d-flex align-items-center justify-content-between px-0">
                                        <small>Direct messaging</small> <i class="fe fe-check-circle text-success"></i>
                                    </li>
                                    <li class="list-group-item d-flex align-items-center justify-content-between px-0">
                                        <small>Members</small> <small>10 members</small>
                                    </li>
                                    <li class="list-group-item d-flex align-items-center justify-content-between px-0">
                                        <small>Admins</small> <small>No access</small>
                                    </li>
                                </ul>
                            </div>
                       
                            <div v-if="$store.state.user.payment_method_id">
                                <button v-if="!subs_id" :disabled="!$store.state.user.payment_method_id || subs_id==product.id || busy" class="btn w-100 btn-light" @click="subscribe(product.id)">
                                                    <span v-if="subs_id == product.id">
                                                      Subscribed
                                                    </span>
                                                    <span v-else>
                                                      Subscribe
                                                    </span>
                                                    <div v-if="subscribing == product.product_id" class="spinner-border text-light spinner-border-sm" role="status"></div>
                                                  </button>
                                <button v-else :disabled="!$store.state.user.payment_method_id || subs_id==product.id || busy" class="btn w-100 btn-light" @click="ConfirmSwitch(product.id)">
                                                   Subscribed
                                                   </button>
                                <br>
                                <div class="text-center">
                                  <small v-if="switching && switching_prod==product.id" class="text-warning">Do you want to switch your current package to this one?</small><br>
                                  <span v-if="switching && switching_prod==product.id" @click="subscribe(product.id)" class="badge bg-danger small">Confirm?</span>
                                  <span href="#" v-if="switching && switching_prod==product.id" @click="cancelSubscribe()" class="badge bg-success small">Cancel?</span>
                                </div>
                            </div>
                            <div class="text-center">
                            <span href="#!" class="small sm text-center text-weight-light text-muted" v-if="subs_id == product.id" @click="unsubscribe(product.id)">Unsubscribe</span>
                            </div>
                            <br>
    
                            <a href="#" v-if="unsubbtn && pid==product.id" @click="unsubscribeCofirm(product.id)" class="badge badge-soft-danger small mt-3">Confirm?</a>
                            <a href="#" v-if="unsubbtn && pid==product.id" @click="unsubscribeCancel()" class="badge badge-soft-info small">Cancel?</a>
                        </div>
                    </div>
    
                </div>
    
            </div>
            <!-- / .row -->
            <div class="row">
                <div class="col-12 col-md-6">
    
                    <!-- Card -->
                    <div class="card card-inactive">
                        <div class="card-body">
    
                            <!-- Title -->
                            <h3 class="text-center">
                                Need some help deciding?
                            </h3>
    
                            <!-- Text -->
                            <p class="text-muted text-center">
                                We can help you decide what’s the best for your company based on a lot of factors and other cool stuff that I’m going to write about.
                            </p>
    
                            <!-- Button -->
                            <div class="text-center">
                                <a href="#!" class="btn btn-outline-secondary">
                                Contact us
                              </a>
                            </div>
    
                        </div>
                    </div>
    
                </div>
                <div class="col-12 col-md-6">
    
                    <!-- Card -->
                    <div class="card card-inactive">
                        <div class="card-body">
    
                            <!-- Title -->
                            <h3 class="text-center">
                                Want a custom plan?
                            </h3>
    
                            <!-- Text -->
                            <p class="text-muted text-center">
                                We can help you decide what’s the best for your company based on a lot of factors and other cool stuff that I’m going to write about.
                            </p>
    
                            <!-- Button -->
                            <div class="text-center">
                                <a href="#!" class="btn btn-outline-secondary">
                                Build it
                              </a>
                            </div>
    
                        </div>
                    </div>
    
                </div>
            </div>
            <!-- / .row -->
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            products: {},
            busy: false,
            status: true,
            message: '',
            subs_id: false,
            errors: {},
            unsubbtn: false,
            pid: '',
            successmsg: false,
            errormsg: false,
            subscribing: false,
            endPoint: '',
            switching: false,
            switching_prod: ''
        };
    },
    mounted() {
        let _this = this;
        _this.getProducts();
        _this.getSubscription();

    },
    methods: {
        ConfirmSwitch(product_id) {
            let _this = this;
            _this.switching = true;
            _this.switching_prod = product_id;
        },
        cancelSubscribe() {
            let _this = this;
            _this.switching = false;
            _this.switching_prod = '';
        },
        unsubscribe(prod_id) {
            let _this = this;
            _this.unsubbtn = true;
            _this.pid = prod_id;
        },
        unsubscribeCancel() {
            let _this = this;
            _this.unsubbtn = false;
        },
        unsubscribeCofirm(product_id) {
            let _this = this;
            _this.busy = true;
            let fd = new FormData();
            fd.append('product_id', product_id);
            axios
                .post(
                    `/billing/unsubscribe/`, fd)
                .then((res) => {
                    // _this.successmsg = true;
                    // _this.message = res.data.message;
                    _this.busy = false;
                    _this.getProducts();
                    _this.getSubscription();
                    _this.subscribing = false;
                    _this.subs_id = false;
                    _this.unsubbtn = false;
                    toastr.success(res.data.message);
                })
                .catch((err) => {
                    console.log(err.status)
                    // _this.errormsg = true;
                    // _this.message = err.response.data.message;
                    _this.busy = false;
                    toastr.success(err.response.data.message);
                });
        },
        getSubscription() {
            let _this = this;
            axios
                .get(
                    `/billing/get_subscribe/`)
                .then((res) => {
                    if (res.data.product_id) {
                        _this.subs_id = res.data.product_id;
                    }
                    console.log(_this.subs_id)
                })
                .catch((err) => {
                    _this.subs_id = false;
                });
        },
        subscribe(product_id) {
            let _this = this;
            _this.busy = true;
            _this.subscribing = product_id;

            if (_this.subs_id == false) {
                _this.endPoint = '/billing/subscribe/';

            } else {
                _this.endPoint = '/billing/switch/';
            }
            let fd = new FormData();
            fd.append('product_id', product_id);
            axios
                .post(`${_this.endPoint}`, fd)
                .then((res) => {
                    // _this.successmsg = true;
                    // _this.message = res.data.message;
                    _this.busy = false;
                    _this.getProducts();
                    _this.getSubscription();
                    toastr.success(res.data.message);
                })
                .catch((err) => {
                    console.log(err.status)
                    // _this.errormsg = true;
                    _this.message = err.response.data.message;
                    _this.busy = false;
                    toastr.error(err.response.data.message);
                });
            _this.switching = false;
            _this.switching_prod = '';
        },
        getParameterByName(url, name) {
            var match = RegExp("[?&]" + name + "=([^&]*)").exec(url);
            return match && decodeURIComponent(match[1].replace(/\+/g, " "));
        },
        getProducts() {
            let _this = this;
            _this.busy = true;
            axios
                .get(
                    `/billing/?status=true`
                )
                .then((res) => {
                    _this.products = res.data;
                    if (res.data.next) {
                        _this.next_offset = _this.getParameterByName(res.data.next, "offset");
                    } else {
                        _this.next_offset = false;
                    }
                    if (res.data.previous) {
                        let prev_offset = _this.getParameterByName(res.data.previous, "offset");
                        if (!prev_offset) {
                            prev_offset = "0";
                        }
                        _this.previous_offset = prev_offset;
                    } else {
                        _this.previous_offset = false;
                    }
                    _this.busy = false;
                })
                .catch((err) => {
                    _this.busy = false;
                    _this.products = false;
                });
        },
        orderProductsBy(order_by) {
            let _this = this;
            if (order_by == _this.order_by) {
                _this.order_by = `-${order_by}`;
            } else {
                _this.order_by = order_by;
            }
            _this.offset = "";
            _this.getProducts();
        },
    },
    watch: {
        busy(oldVal, newVal) {
            // docReady(tooltipInit);
        },
    },
};
</script>
