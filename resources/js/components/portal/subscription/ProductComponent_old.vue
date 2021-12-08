<template>
    <div>
    
        <div class="row no-gutters">
            <div class="row">
                <div class="col-12">
                    <div class="card mb-3">
                        <div class="card-header gradient-dark">
                            <div class="col-sm-auto">
                                <h5 class="d-inline-block text-white">Subscription</h5>
                            </div>
                        </div>
                        <div class="card-body">
                            <div class="row g-0">
                                <div class="col-12 mb-3">
                                    <div class="row justify-content-center justify-content-sm-between">
    
    
                                    </div>
                                </div>
    
                                <div class="col-12 mb-3" v-if="!$store.state.user.payment_method_id">
                                    <div class="alert alert-warning">Please update your payment method first to subscribe!
                                        <router-link :to="{name: 'billing'}" class="btn btn-info btn-sm">
                                            <i class="fas fa-credit-card"></i> Billing Settings
                                        </router-link>
                                    </div>
                                </div>
                                <div class="col-12 mb-3">
                                    <div v-if="successmsg" class="alert alert-success" role="alert">{{message}}</div>
                                    <div v-if="errormsg" class="alert alert-danger" role="alert">{{message}}</div>
                                </div>
    
                                <div v-if="products" v-for="product in products.results" :key="product.id" class="col-lg-4 border-top border-bottom border">
    
    
                                    <div class="h-100">
                                        <div class="text-center p-4">
                                            <h3 class="fw-normal my-0">{{product.product_name}}</h3>
                                            <p class="mt-3 text-left small" v-html="product.product_description"></p>
                                            <h2 class="fw-medium my-4"> 
                                            <sup class="fw-normal fs-2 me-1">&dollar;</sup>{{product.product_price}}<small class="fs--1 text-700">/ Monthly</small>
                                            </h2>
                                            <div v-if="$store.state.user.payment_method_id">
                                                <button v-if="!subs_id" :disabled="!$store.state.user.payment_method_id || subs_id==product.id || busy" class="btn btn-primary" @click="subscribe(product.id)">
                                                <span v-if="subs_id == product.id">
                                                  Subscribed
                                                </span>
                                                <span v-else>
                                                  Subscribe
                                                </span>
                                                <div v-if="subscribing == product.product_id" class="spinner-border text-light spinner-border-sm" role="status"></div>
                                              </button>
                                                <button v-else :disabled="!$store.state.user.payment_method_id || subs_id==product.id || busy" class="btn btn-primary btn-black rounded" @click="ConfirmSwitch(product.id)">
                                               Subscribed
                                               </button>
                                                <br>
                                                <small v-if="switching && switching_prod==product.id" class="text-warning">Do you want to switch your current package to this one?</small><br>
                                                <a href="#" v-if="switching && switching_prod==product.id" @click="subscribe(product.id)" class="badge badge-soft-danger small mt-3">Confirm?</a>
                                                <a href="#" v-if="switching && switching_prod==product.id" @click="cancelSubscribe()" class="badge badge-soft-info small">Cancel?</a>
                                            </div>
                                            <a class="btn-warning btn btn-sm mt-3" v-if="subs_id == product.id" @click="unsubscribe(product.id)">Unsubscribe</a>
                                            <br>
    
                                            <a href="#" v-if="unsubbtn && pid==product.id" @click="unsubscribeCofirm(product.id)" class="badge badge-soft-danger small mt-3">Confirm?</a>
                                            <a href="#" v-if="unsubbtn && pid==product.id" @click="unsubscribeCancel()" class="badge badge-soft-info small">Cancel?</a>
                                        </div>
    
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
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
        docReady(tooltipInit);
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
            docReady(tooltipInit);
        },
    },
};
</script>
