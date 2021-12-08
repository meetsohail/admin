<template>
    <div>
        <!-- HEADER -->
        <div class="pt-7 pb-8 bg-dark bg-ellipses">
            <div class="container-fluid">
                <div class="row justify-content-center">
                    <div class="col-md-10 col-lg-8 col-xl-6">
    
                        <!-- Title -->
                        <h1 class="display-3 text-center text-white">
                            Plans & Pricing
                        </h1>
    
                        <!-- Text -->
                        <p class="lead text-center text-muted">
                            We have plans and prices that fit your business perfectly. Make your client site a success with our products.
                        </p>
    
                    </div>
                </div>
                <!-- / .row -->
            </div>
        </div>
    
        <!-- CONTENT -->
        <div class="container-fluid">
            <div class="row mt-n7" v-if="!$store.state.user.payment_method_id">
                <div class="col-12 col-lg-23">
    
                    <!-- Card -->
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
                <div class="col-12 col-lg-4" v-if="products" v-for="product in products.results" :key="product.id" >
    
                    <!-- Card -->
                    <div class="card">
                        <div class="card-body">
    
                            <!-- Title -->
                            <h6 class="text-uppercase text-center text-muted my-4">
                                {{product.product_name}}
                            </h6>
    
                            <!-- Price -->
                            <div class="row g-0 align-items-center justify-content-center">
                                <div class="col-auto">
                                    <div class="h2 mb-0">$</div>
                                </div>
                                <div class="col-auto">
                                    <div class="display-2 mb-0">{{product.product_price}}</div>
                                </div>
                            </div>
                            <!-- / .row -->
    
                            <!-- Period -->
                            <div class="h6 text-uppercase text-center text-muted mb-5">
                                / month
                            </div>
    
                            <!-- Features -->
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
    
                            <!-- Button -->
                            <a href="#!" class="btn w-100 btn-light">
                          Start with Basic
                        </a>
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

</script>