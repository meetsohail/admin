<template>
   <div class="row justify-content-center container-fluid">
          <div class="col-12">

            <!-- Header -->
            <div class="header">
              <div class="header-body">
                <div class="row align-items-center">
                  <div class="col">

                    <!-- Pretitle -->
                    <h6 class="header-pretitle">
                      Overview
                    </h6>

                    <!-- Title -->
                    <h1 class="header-title text-truncate">
                      Users
                    </h1>

                  </div>
                  <div class="col-auto">

                    <!-- Navigation (button group) -->
                    <div class="nav btn-group d-inline-flex" role="tablist">
                      <button class="btn btn-white active" id="contactsListTab" data-bs-toggle="tab" data-bs-target="#contactsListPane" role="tab" aria-controls="contactsListPane" aria-selected="true">
                        <span class="fe fe-list"></span>
                      </button>
                      <button class="btn btn-white" id="contactsCardsTab" data-bs-toggle="tab" data-bs-target="#contactsCardsPane" role="tab" aria-controls="contactsCardsPane" aria-selected="false">
                        <span class="fe fe-grid"></span>
                      </button>
                    </div> <!-- / .nav -->

                    <!-- Buttons -->
                    <a href="#!" class="btn btn-primary ms-2">
                      Add contact
                    </a>

                  </div>
                </div> <!-- / .row -->
                <div class="row align-items-center">
                  <div class="col">

                    <!-- Nav -->
                    <ul class="nav nav-tabs nav-overflow header-tabs">
                      <li class="nav-item">
                        <a href="#!" class="nav-link text-nowrap active">
                          All contacts <span class="badge rounded-pill bg-secondary-soft">{{users.count}}</span>
                        </a>
                      </li>
                     
                    </ul>

                  </div>
                </div>
              </div>
            </div>

            <!-- Tab content -->
            <div class="tab-content">
              <div class="tab-pane fade show active" id="contactsListPane" role="tabpanel" aria-labelledby="contactsListTab">

                <!-- Card -->
                <div class="card" data-list='{"valueNames": ["item-name", "item-title", "item-email", "item-phone", "item-score", "item-company"], "page": 10, "pagination": {"paginationClass": "list-pagination"}}' id="contactsList">
                  <div class="card-header">
                    <div class="row align-items-center">
                      <div class="col">

                        <!-- Form -->
                        <form>
                          <div class="input-group input-group-flush input-group-merge input-group-reverse">
                            <input class="form-control list-search" type="search" placeholder="Search" :disabled="busy">
                            <span class="input-group-text">
                              <i class="fe fe-search"></i>
                            </span>
                          </div>
                        </form>

                      </div>
                      <div class="col-auto me-n3">

                        <!-- Select -->
                        <form>
                          <select class="form-select form-select-sm form-control-flush" data-choices='{"searchEnabled": false}'>
                            <option>5 per page</option>
                            <option selected>10 per page</option>
                            <option>All</option>
                          </select>
                        </form>

                      </div>
                      <div class="col-auto">

                        <!-- Dropdown -->
                        <div class="dropdown">

                          <!-- Toggle -->
                          <button class="btn btn-sm btn-white" type="button" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-haspopup="true" aria-expanded="false">
                            <i class="fe fe-sliders me-1"></i> Filter <span class="badge bg-primary ms-1 d-none">0</span>
                          </button>

                          <!-- Menu -->
                          <form class="dropdown-menu dropdown-menu-end dropdown-menu-card">
                            <div class="card-header">

                              <!-- Title -->
                              <h4 class="card-header-title">
                                Filters
                              </h4>

                              <!-- Link -->
                              <button class="btn btn-sm btn-link text-reset d-none" type="reset">
                                <small>Clear filters</small>
                              </button>

                            </div>
                            <div class="card-body">

                              <!-- List group -->
                              <div class="list-group list-group-flush mt-n4 mb-4">
                                <div class="list-group-item">
                                  <div class="row">
                                    <div class="col">

                                      <!-- Text -->
                                      <small>Title</small>

                                    </div>
                                    <div class="col-auto">

                                      <!-- Select -->
                                      <select class="form-select form-select-sm" name="item-title" data-choices='{"searchEnabled": false}'>
                                        <option value="*" selected>Any</option>
                                        <option value="Designer">Designer</option>
                                        <option value="Developer">Developer</option>
                                        <option value="Owner">Owner</option>
                                        <option value="Founder">Founder</option>
                                      </select>

                                    </div>
                                  </div> <!-- / .row -->
                                </div>
                                <div class="list-group-item">
                                  <div class="row">
                                    <div class="col">

                                      <!-- Text -->
                                      <small>Lead scrore</small>

                                    </div>
                                    <div class="col-auto">

                                      <!-- Select -->
                                      <select class="form-select form-select-sm" name="item-score" data-choices='{"searchEnabled": false}'>
                                        <option value="*" selected>Any</option>
                                        <option value="1/10">1+</option>
                                        <option value="2/10">2+</option>
                                        <option value="3/10">3+</option>
                                        <option value="4/10">4+</option>
                                        <option value="5/10">5+</option>
                                        <option value="6/10">6+</option>
                                        <option value="7/10">7+</option>
                                        <option value="8/10">8+</option>
                                        <option value="9/10">9+</option>
                                        <option value="10/10">10</option>
                                      </select>

                                    </div>
                                  </div> <!-- / .row -->
                                </div>
                              </div>

                              <!-- Button -->
                              <button class="btn w-100 btn-primary" type="submit">
                                Apply filter
                              </button>

                            </div>
                          </form>

                        </div>

                      </div>
                    </div> <!-- / .row -->
                  </div>
                    <div v-if="busy" class="row g-0 p-4 text-center">
                <loading-component
                  :busy="busy"
                  nText
                  bText="Loading users..."
                ></loading-component>
                </div>
                  <div class="table-responsive" v-else>
                 
                    <table class="table table-sm table-hover table-nowrap card-table">
                      <thead>
                        <tr>
                          <th>
                            <!-- Checkbox -->
                            <div class="form-check mb-n2">
                              <input class="form-check-input list-checkbox-all" id="listCheckboxAll" type="checkbox">
                              <label class="form-check-label" for="listCheckboxAll"></label>
                            </div>

                          </th>
                          <th>
                            <a class="list-sort text-muted" data-sort="item-name" href="#">Name</a>
                          </th>
                          <th>
                            <a class="list-sort text-muted" data-sort="item-email" href="#">Email</a>
                          </th>
                          <th>
                            <a class="list-sort text-muted" data-sort="item-phone" href="#">Card 4 Digit</a>
                          </th>
                          <th>
                            <a class="list-sort text-muted" data-sort="item-score" href="#">Card Brand</a>
                          </th>
                          <th colspan="">
                            <a class="list-sort text-muted" data-sort="item-company" href="#">Payment ID</a>
                          </th>
                          <th colspan="2">
                            <a class="list-sort text-muted" data-sort="item-company" href="#">Joined</a>
                          </th>
                        </tr>
                      </thead>
                      <tbody class="list fs-base">
                       <tr v-if="!users || users.count == 0">
                        <td>No User Found!</td>
                        </tr>
                        <tr v-for="user in users" :key="user.id">
                          <td>

                            <!-- Checkbox -->
                            <div class="form-check">
                              <input class="form-check-input list-checkbox" id="listCheckboxOne" type="checkbox">
                              <label class="form-check-label" for="listCheckboxOne"></label>
                            </div>

                          </td>
                           <td>
                            <!-- Avatar -->
                            <div class="avatar avatar-xs align-middle me-2">
                              <img class="avatar-img rounded-circle" v-bind:src="user.avatar_url" alt="...">
                            </div> <a class="item-name text-reset" href="#!">{{ user.first_name }} {{ user.last_name }}</a>

                          </td>
                           <td>

                            <!-- Email -->
                            <a class="item-email text-reset" href="#!">{{user.email}}</a>

                          </td>
                          <td class="">

                            <!-- Text -->
                            <span class="item-title">{{user.stripe_last4}}</span>

                          </td>
                         
                          <td>

                            <!-- Phone -->
                            <a class="item-phone text-reset" href="#!">{{user.card_brand}}</a>

                          </td>
                          <td>

                            <!-- Badge -->
                            <span class="item-score badge bg-success-soft">{{user.payment_method_id}}</span>

                          </td>
                          <td>

                            <!-- Link -->
                            <a class="item-company text-reset" href="#!">{{user.date_joined}}</a>

                          </td>
                            <td>

                            <!-- Link -->
                            <router-link :to="{name: 'updateuser', params:{id: user.id}}" class="btn btn-black btn-sm text-white">
                              <i class="fe fe-edit"></i> 
                            </router-link>

                          </td>
                        </tr>
                       
                      </tbody>
                    </table>
                  </div>
                  <div class="card-footer d-flex justify-content-between">

                    <!-- Pagination (prev) -->
                    <ul class="list-pagination-prev pagination pagination-tabs card-pagination">
                      <li class="page-item">
                        <a class="page-link ps-0 pe-4 border-end" href="#">
                          <i class="fe fe-arrow-left me-1"></i> Prev
                        </a>
                      </li>
                    </ul>

                    <!-- Pagination -->
                    <ul class="list-pagination pagination pagination-tabs card-pagination"></ul>

                    <!-- Pagination (next) -->
                    <ul class="list-pagination-next pagination pagination-tabs card-pagination">
                      <li class="page-item">
                        <a class="page-link ps-4 pe-0 border-start" href="#">
                          Next <i class="fe fe-arrow-right ms-1"></i>
                        </a>
                      </li>
                    </ul>

                    <!-- Alert -->
                    <div class="list-alert alert alert-dark alert-dismissible border fade" role="alert">

                      <!-- Content -->
                      <div class="row align-items-center">
                        <div class="col">

                          <!-- Checkbox -->
                          <div class="form-check">
                            <input class="form-check-input" id="listAlertCheckbox" type="checkbox" checked disabled>
                            <label class="form-check-label text-white" for="listAlertCheckbox">
                              <span class="list-alert-count">0</span> deal(s)
                            </label>
                          </div>

                        </div>
                        <div class="col-auto me-n3">

                          <!-- Button -->
                          <button class="btn btn-sm btn-white-20">
                            Edit
                          </button>

                          <!-- Button -->
                          <button class="btn btn-sm btn-white-20">
                            Delete
                          </button>

                        </div>
                      </div> <!-- / .row -->

                      <!-- Close -->
                      <button type="button" class="list-alert-close btn-close" aria-label="Close"></button>

                    </div>

                  </div>
                </div>

              </div>
              <div class="tab-pane fade" id="contactsCardsPane" role="tabpanel" aria-labelledby="contactsCardsTab">

                <!-- Cards -->
                <div data-list='{"valueNames": ["item-name", "item-title", "item-email", "item-phone", "item-score", "item-company"], "page": 9, "pagination": {"paginationClass": "list-pagination"}}' id="contactsCards">

                  <!-- Header -->
                  <div class="row align-items-center mb-4">
                    <div class="col">

                      <!-- Form -->
                      <form>
                        <div class="input-group input-group-lg input-group-merge input-group-reverse">
                          <input class="form-control list-search" type="search" placeholder="Search">
                          <span class="input-group-text">
                            <i class="fe fe-search"></i>
                          </span>
                        </div>
                      </form>

                    </div>
                    <div class="col-auto me-n3">

                      <!-- Select -->
                      <form>
                        <select class="form-select form-select-sm form-control-flush" data-choices='{"searchEnabled": false}'>
                          <option selected>9 per page</option>
                          <option>All</option>
                        </select>
                      </form>

                    </div>
                    <div class="col-auto">

                      <!-- Dropdown -->
                      <div class="dropdown">

                        <!-- Toggle -->
                        <button class="btn btn-sm btn-white" type="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                          <i class="fe fe-sliders me-1"></i> Filter <span class="badge bg-primary ms-1 d-none">0</span>
                        </button>

                        <!-- Menu -->
                        <form class="dropdown-menu dropdown-menu-end dropdown-menu-card">
                          <div class="card-header">

                            <!-- Title -->
                            <h4 class="card-header-title">
                              Filters
                            </h4>

                            <!-- Link -->
                            <button class="btn btn-sm btn-link text-reset d-none" type="reset">
                              <small>Clear filters</small>
                            </button>

                          </div>
                          <div class="card-body">

                            <!-- List group -->
                            <div class="list-group list-group-flush mt-n4 mb-4">
                              <div class="list-group-item">
                                <div class="row">
                                  <div class="col">

                                    <!-- Text -->
                                    <small>Title</small>

                                  </div>
                                  <div class="col-auto">

                                    <!-- Select -->
                                    <select class="form-select form-select-sm" name="item-title" data-choices='{"searchEnabled": false}'>
                                      <option value="*" selected>Any</option>
                                      <option value="Designer">Designer</option>
                                      <option value="Developer">Developer</option>
                                      <option value="Owner">Owner</option>
                                      <option value="Founder">Founder</option>
                                    </select>

                                  </div>
                                </div> <!-- / .row -->
                              </div>
                              <div class="list-group-item">
                                <div class="row">
                                  <div class="col">

                                    <!-- Text -->
                                    <small>Lead scrore</small>

                                  </div>
                                  <div class="col-auto">

                                    <!-- Select -->
                                    <select class="form-select form-select-sm" name="item-score" data-choices='{"searchEnabled": false}'>
                                      <option value="*" selected>Any</option>
                                      <option value="1/10">1+</option>
                                      <option value="2/10">2+</option>
                                      <option value="3/10">3+</option>
                                      <option value="4/10">4+</option>
                                      <option value="5/10">5+</option>
                                      <option value="6/10">6+</option>
                                      <option value="7/10">7+</option>
                                      <option value="8/10">8+</option>
                                      <option value="9/10">9+</option>
                                      <option value="10/10">10</option>
                                    </select>

                                  </div>
                                </div> <!-- / .row -->
                              </div>
                            </div>

                            <!-- Button -->
                            <button class="btn w-100 btn-primary" type="submit">
                              Apply filter
                            </button>

                          </div>
                        </form>

                      </div>

                    </div>
                  </div> <!-- / .row -->

                  <!-- Body -->
                  <div class="list row">
                    <div class="col-12 col-md-6 col-xl-4">

                      <!-- Card -->
                      <div class="card">
                        <div class="card-body">

                          <!-- Header -->
                          <div class="row align-items-center">
                            <div class="col">

                              <!-- Checkbox -->
                              <div class="form-check form-check-circle">
                                <input class="form-check-input list-checkbox" type="checkbox" id="cardsCheckboxOne">
                                <label class="form-check-label" for="cardsCheckboxOne"></label>
                              </div>

                            </div>
                            <div class="col-auto">

                              <!-- Dropdown -->
                              <div class="dropdown">
                                <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                  <i class="fe fe-more-vertical"></i>
                                </a>
                                <div class="dropdown-menu dropdown-menu-end">
                                  <a href="#!" class="dropdown-item">
                                    Action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Another action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Something else here
                                  </a>
                                </div>
                              </div>

                            </div>
                          </div> <!-- / .row -->

                          <!-- Image -->
                          <a href="profile-posts.html" class="avatar avatar-xl card-avatar">
                            <img src="assets/img/avatars/profiles/avatar-1.jpg" class="avatar-img rounded-circle" alt="...">
                          </a>

                          <!-- Body -->
                          <div class="text-center mb-5">

                            <!-- Heading -->
                            <h2 class="card-title">
                              <a class="item-name" href="profile-posts.html">Dianna Smiley</a>
                            </h2>

                            <!-- Text -->
                            <p class="small text-muted mb-3">
                              <span class="item-title">Designer</span> at <span class="item-company">Twitter</span>
                            </p>

                            <!-- Buttons -->
                            <a class="btn btn-sm btn-white" href="tel:1-123-456-7890">
                              <i class="fe fe-phone me-1"></i> Call
                            </a>
                            <a class="btn btn-sm btn-white" href="mailto:john.doe@company.com">
                              <i class="fe fe-mail me-1"></i> Email
                            </a>

                          </div>

                          <!-- Divider -->
                          <hr class="card-divider mb-0">

                          <!-- List group -->
                          <div class="list-group list-group-flush mb-n3">
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Company</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Text -->
                                  <small>Twitter</small>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Lead Score</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Badge -->
                                  <span class="item-score badge bg-danger-soft">1/10</span>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                          </div>

                        </div>
                      </div>

                    </div>
                    <div class="col-12 col-md-6 col-xl-4">

                      <!-- Card -->
                      <div class="card">
                        <div class="card-body">

                          <!-- Header -->
                          <div class="row align-items-center">
                            <div class="col">

                              <!-- Checkbox -->
                              <div class="form-check form-check-circle">
                                <input class="form-check-input list-checkbox" type="checkbox" id="cardsCheckboxTwo">
                                <label class="form-check-label" for="cardsCheckboxTwo"></label>
                              </div>

                            </div>
                            <div class="col-auto">

                              <!-- Dropdown -->
                              <div class="dropdown">
                                <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                  <i class="fe fe-more-vertical"></i>
                                </a>
                                <div class="dropdown-menu dropdown-menu-end">
                                  <a href="#!" class="dropdown-item">
                                    Action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Another action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Something else here
                                  </a>
                                </div>
                              </div>

                            </div>
                          </div> <!-- / .row -->

                          <!-- Image -->
                          <a href="profile-posts.html" class="avatar avatar-xl card-avatar">
                            <img src="assets/img/avatars/profiles/avatar-2.jpg" class="avatar-img rounded-circle" alt="...">
                          </a>

                          <!-- Body -->
                          <div class="text-center mb-5">

                            <!-- Heading -->
                            <h2 class="card-title">
                              <a class="item-name" href="profile-posts.html">Ab Hadley</a>
                            </h2>

                            <!-- Text -->
                            <p class="small text-muted mb-3">
                              <span class="item-title">Developer</span> at <span class="item-company">Google</span>
                            </p>

                            <!-- Buttons -->
                            <a class="btn btn-sm btn-white" href="tel:1-123-456-7890">
                              <i class="fe fe-phone me-1"></i> Call
                            </a>
                            <a class="btn btn-sm btn-white" href="mailto:john.doe@company.com">
                              <i class="fe fe-mail me-1"></i> Email
                            </a>

                          </div>

                          <!-- Divider -->
                          <hr class="card-divider mb-0">

                          <!-- List group -->
                          <div class="list-group list-group-flush mb-n3">
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Company</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Text -->
                                  <small>Google</small>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Lead Score</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Badge -->
                                  <span class="item-score badge bg-success-soft">8/10</span>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                          </div>

                        </div>
                      </div>

                    </div>
                    <div class="col-12 col-md-6 col-xl-4">

                      <!-- Card -->
                      <div class="card">
                        <div class="card-body">

                          <!-- Header -->
                          <div class="row align-items-center">
                            <div class="col">

                              <!-- Checkbox -->
                              <div class="form-check form-check-circle">
                                <input class="form-check-input list-checkbox" type="checkbox" id="cardsCheckBoxThree">
                                <label class="form-check-label" for="cardsCheckBoxThree"></label>
                              </div>

                            </div>
                            <div class="col-auto">

                              <!-- Dropdown -->
                              <div class="dropdown">
                                <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                  <i class="fe fe-more-vertical"></i>
                                </a>
                                <div class="dropdown-menu dropdown-menu-end">
                                  <a href="#!" class="dropdown-item">
                                    Action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Another action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Something else here
                                  </a>
                                </div>
                              </div>

                            </div>
                          </div> <!-- / .row -->

                          <!-- Image -->
                          <a href="profile-posts.html" class="avatar avatar-xl card-avatar">
                            <img src="assets/img/avatars/profiles/avatar-3.jpg" class="avatar-img rounded-circle" alt="...">
                          </a>

                          <!-- Body -->
                          <div class="text-center mb-5">

                            <!-- Heading -->
                            <h2 class="card-title">
                              <a class="item-name" href="profile-posts.html">Adolfo Hess</a>
                            </h2>

                            <!-- Text -->
                            <p class="small text-muted mb-3">
                              <span class="item-title">Owner</span> at <span class="item-company">Google</span>
                            </p>

                            <!-- Buttons -->
                            <a class="btn btn-sm btn-white" href="tel:1-123-456-7890">
                              <i class="fe fe-phone me-1"></i> Call
                            </a>
                            <a class="btn btn-sm btn-white" href="mailto:john.doe@company.com">
                              <i class="fe fe-mail me-1"></i> Email
                            </a>

                          </div>

                          <!-- Divider -->
                          <hr class="card-divider mb-0">

                          <!-- List group -->
                          <div class="list-group list-group-flush mb-n3">
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Company</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Text -->
                                  <small>Google</small>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Lead Score</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Badge -->
                                  <span class="item-score badge bg-success-soft">7/10</span>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                          </div>

                        </div>
                      </div>

                    </div>
                    <div class="col-12 col-md-6 col-xl-4">

                      <!-- Card -->
                      <div class="card">
                        <div class="card-body">

                          <!-- Header -->
                          <div class="row align-items-center">
                            <div class="col">

                              <!-- Checkbox -->
                              <div class="form-check form-check-circle">
                                <input class="form-check-input list-checkbox" type="checkbox" id="cardsCheckboxFour">
                                <label class="form-check-label" for="cardsCheckboxFour"></label>
                              </div>

                            </div>
                            <div class="col-auto">

                              <!-- Dropdown -->
                              <div class="dropdown">
                                <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                  <i class="fe fe-more-vertical"></i>
                                </a>
                                <div class="dropdown-menu dropdown-menu-end">
                                  <a href="#!" class="dropdown-item">
                                    Action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Another action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Something else here
                                  </a>
                                </div>
                              </div>

                            </div>
                          </div> <!-- / .row -->

                          <!-- Image -->
                          <a href="profile-posts.html" class="avatar avatar-xl card-avatar">
                            <img src="assets/img/avatars/profiles/avatar-4.jpg" class="avatar-img rounded-circle" alt="...">
                          </a>

                          <!-- Body -->
                          <div class="text-center mb-5">

                            <!-- Heading -->
                            <h2 class="card-title">
                              <a class="item-name" href="profile-posts.html">Daniela Dewitt</a>
                            </h2>

                            <!-- Text -->
                            <p class="small text-muted mb-3">
                              <span class="item-title">Designer</span> at <span class="item-position">Twitch</span>
                            </p>

                            <!-- Buttons -->
                            <a class="btn btn-sm btn-white" href="tel:tel:1-123-456-7890">
                              <i class="fe fe-phone me-1"></i> Call
                            </a>
                            <a class="btn btn-sm btn-white" href="mailto:john.doe@company.com">
                              <i class="fe fe-mail me-1"></i> Email
                            </a>

                          </div>

                          <!-- Divider -->
                          <hr class="card-divider mb-0">

                          <!-- List group -->
                          <div class="list-group list-group-flush mb-n3">
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Company</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Text -->
                                  <small>Twitch</small>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Lead Score</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Badge -->
                                  <span class="item-score badge bg-warning-soft">4/10</span>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                          </div>

                        </div>
                      </div>

                    </div>
                    <div class="col-12 col-md-6 col-xl-4">

                      <!-- Card -->
                      <div class="card">
                        <div class="card-body">

                          <!-- Header -->
                          <div class="row align-items-center">
                            <div class="col">

                              <!-- Checkbox -->
                              <div class="form-check form-check-circle">
                                <input class="form-check-input list-checkbox" type="checkbox" id="cardsCheckboxFive">
                                <label class="form-check-label" for="cardsCheckboxFive"></label>
                              </div>

                            </div>
                            <div class="col-auto">

                              <!-- Dropdown -->
                              <div class="dropdown">
                                <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                  <i class="fe fe-more-vertical"></i>
                                </a>
                                <div class="dropdown-menu dropdown-menu-end">
                                  <a href="#!" class="dropdown-item">
                                    Action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Another action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Something else here
                                  </a>
                                </div>
                              </div>

                            </div>
                          </div> <!-- / .row -->

                          <!-- Image -->
                          <a href="profile-posts.html" class="avatar avatar-xl card-avatar">
                            <img src="assets/img/avatars/profiles/avatar-5.jpg" class="avatar-img rounded-circle" alt="...">
                          </a>

                          <!-- Body -->
                          <div class="text-center mb-5">

                            <!-- Heading -->
                            <h2 class="card-title">
                              <a class="item-name" href="profile-posts.html">Miyah Myles</a>
                            </h2>

                            <!-- Text -->
                            <p class="small text-muted mb-3">
                              <span class="item-title">Founder</span> at <span class="item-company">Facebook</span>
                            </p>

                            <!-- Buttons -->
                            <a class="btn btn-sm btn-white" href="tel:1-123-456-7890">
                              <i class="fe fe-phone me-1"></i> Call
                            </a>
                            <a class="btn btn-sm btn-white" href="mailto:john.doe@company.com">
                              <i class="fe fe-mail me-1"></i> Email
                            </a>

                          </div>

                          <!-- Divider -->
                          <hr class="card-divider mb-0">

                          <!-- List group -->
                          <div class="list-group list-group-flush mb-n3">
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Company</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Text -->
                                  <small>Facebook</small>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Lead Score</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Badge -->
                                  <span class="item-score badge bg-danger-soft">3/10</span>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                          </div>

                        </div>
                      </div>

                    </div>
                    <div class="col-12 col-md-6 col-xl-4">

                      <!-- Card -->
                      <div class="card">
                        <div class="card-body">

                          <!-- Header -->
                          <div class="row align-items-center">
                            <div class="col">

                              <!-- Checkbox -->
                              <div class="form-check form-check-circle">
                                <input class="form-check-input list-checkbox" type="checkbox" id="cardsCheckBoxSix">
                                <label class="form-check-label" for="cardsCheckBoxSix"></label>
                              </div>

                            </div>
                            <div class="col-auto">

                              <!-- Dropdown -->
                              <div class="dropdown">
                                <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                  <i class="fe fe-more-vertical"></i>
                                </a>
                                <div class="dropdown-menu dropdown-menu-end">
                                  <a href="#!" class="dropdown-item">
                                    Action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Another action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Something else here
                                  </a>
                                </div>
                              </div>

                            </div>
                          </div> <!-- / .row -->

                          <!-- Image -->
                          <a href="profile-posts.html" class="avatar avatar-xl card-avatar">
                            <img src="assets/img/avatars/profiles/avatar-6.jpg" class="avatar-img rounded-circle" alt="...">
                          </a>

                          <!-- Body -->
                          <div class="text-center mb-5">

                            <!-- Heading -->
                            <h2 class="card-title">
                              <a class="item-name" href="profile-posts.html">Ryu Duke</a>
                            </h2>

                            <!-- Text -->
                            <p class="small text-muted mb-3">
                              <span class="item-title">Owner</span> at <span class="item-company">Netflix</span>
                            </p>

                            <!-- Buttons -->
                            <a class="btn btn-sm btn-white" href="tel:1-123-456-7890">
                              <i class="fe fe-phone me-1"></i> Call
                            </a>
                            <a class="btn btn-sm btn-white" href="mailto:john.doe@company.com">
                              <i class="fe fe-mail me-1"></i> Email
                            </a>

                          </div>

                          <!-- Divider -->
                          <hr class="card-divider mb-0">

                          <!-- List group -->
                          <div class="list-group list-group-flush mb-n3">
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Company</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Text -->
                                  <small>Netflix</small>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Lead Score</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Badge -->
                                  <span class="item-score badge bg-warning-soft">6/10</span>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                          </div>

                        </div>
                      </div>

                    </div>
                    <div class="col-12 col-md-6 col-xl-4">

                      <!-- Card -->
                      <div class="card">
                        <div class="card-body">

                          <!-- Header -->
                          <div class="row align-items-center">
                            <div class="col">

                              <!-- Checkbox -->
                              <div class="form-check form-check-circle">
                                <input class="form-check-input list-checkbox" type="checkbox" id="cardsCheckboxSeven">
                                <label class="form-check-label" for="cardsCheckboxSeven"></label>
                              </div>

                            </div>
                            <div class="col-auto">

                              <!-- Dropdown -->
                              <div class="dropdown">
                                <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                  <i class="fe fe-more-vertical"></i>
                                </a>
                                <div class="dropdown-menu dropdown-menu-end">
                                  <a href="#!" class="dropdown-item">
                                    Action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Another action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Something else here
                                  </a>
                                </div>
                              </div>

                            </div>
                          </div> <!-- / .row -->

                          <!-- Image -->
                          <a href="profile-posts.html" class="avatar avatar-xl card-avatar">
                            <img src="assets/img/avatars/profiles/avatar-7.jpg" class="avatar-img rounded-circle" alt="...">
                          </a>

                          <!-- Body -->
                          <div class="text-center mb-5">

                            <!-- Heading -->
                            <h2 class="card-title">
                              <a class="item-name" href="profile-posts.html">Glen Rouse</a>
                            </h2>

                            <!-- Text -->
                            <p class="small text-muted mb-3">
                              <span class="item-title">Designer</span> at <span class="item-position">Netflix</span>
                            </p>

                            <!-- Buttons -->
                            <a class="btn btn-sm btn-white" href="tel:tel:1-123-456-7890">
                              <i class="fe fe-phone me-1"></i> Call
                            </a>
                            <a class="btn btn-sm btn-white" href="mailto:john.doe@company.com">
                              <i class="fe fe-mail me-1"></i> Email
                            </a>

                          </div>

                          <!-- Divider -->
                          <hr class="card-divider mb-0">

                          <!-- List group -->
                          <div class="list-group list-group-flush mb-n3">
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Company</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Text -->
                                  <small>Netflix</small>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Lead Score</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Badge -->
                                  <span class="item-score badge bg-success-soft">9/10</span>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                          </div>

                        </div>
                      </div>

                    </div>
                    <div class="col-12 col-md-6 col-xl-4">

                      <!-- Card -->
                      <div class="card">
                        <div class="card-body">

                          <!-- Header -->
                          <div class="row align-items-center">
                            <div class="col">

                              <!-- Checkbox -->
                              <div class="form-check form-check-circle">
                                <input class="form-check-input list-checkbox" type="checkbox" id="cardsCheckboxEight">
                                <label class="form-check-label" for="cardsCheckboxEight"></label>
                              </div>

                            </div>
                            <div class="col-auto">

                              <!-- Dropdown -->
                              <div class="dropdown">
                                <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                  <i class="fe fe-more-vertical"></i>
                                </a>
                                <div class="dropdown-menu dropdown-menu-end">
                                  <a href="#!" class="dropdown-item">
                                    Action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Another action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Something else here
                                  </a>
                                </div>
                              </div>

                            </div>
                          </div> <!-- / .row -->

                          <!-- Image -->
                          <a href="profile-posts.html" class="avatar avatar-xl card-avatar">
                            <img src="assets/img/avatars/profiles/avatar-1.jpg" class="avatar-img rounded-circle" alt="...">
                          </a>

                          <!-- Body -->
                          <div class="text-center mb-5">

                            <!-- Heading -->
                            <h2 class="card-title">
                              <a class="item-name" href="profile-posts.html">Miyah Myles</a>
                            </h2>

                            <!-- Text -->
                            <p class="small text-muted mb-3">
                              <span class="item-title">Designer</span> at <span class="item-company">Google</span>
                            </p>

                            <!-- Buttons -->
                            <a class="btn btn-sm btn-white" href="tel:1-123-456-7890">
                              <i class="fe fe-phone me-1"></i> Call
                            </a>
                            <a class="btn btn-sm btn-white" href="mailto:john.doe@company.com">
                              <i class="fe fe-mail me-1"></i> Email
                            </a>

                          </div>

                          <!-- Divider -->
                          <hr class="card-divider mb-0">

                          <!-- List group -->
                          <div class="list-group list-group-flush mb-n3">
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Company</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Text -->
                                  <small>Google</small>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Lead Score</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Badge -->
                                  <span class="item-score badge bg-success-soft">10/10</span>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                          </div>

                        </div>
                      </div>

                    </div>
                    <div class="col-12 col-md-6 col-xl-4">

                      <!-- Card -->
                      <div class="card">
                        <div class="card-body">

                          <!-- Header -->
                          <div class="row align-items-center">
                            <div class="col">

                              <!-- Checkbox -->
                              <div class="form-check form-check-circle">
                                <input class="form-check-input list-checkbox" type="checkbox" id="cardsCheckboxNine">
                                <label class="form-check-label" for="cardsCheckboxNine"></label>
                              </div>

                            </div>
                            <div class="col-auto">

                              <!-- Dropdown -->
                              <div class="dropdown">
                                <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                  <i class="fe fe-more-vertical"></i>
                                </a>
                                <div class="dropdown-menu dropdown-menu-end">
                                  <a href="#!" class="dropdown-item">
                                    Action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Another action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Something else here
                                  </a>
                                </div>
                              </div>

                            </div>
                          </div> <!-- / .row -->

                          <!-- Image -->
                          <a href="profile-posts.html" class="avatar avatar-xl card-avatar">
                            <img src="assets/img/avatars/profiles/avatar-2.jpg" class="avatar-img rounded-circle" alt="...">
                          </a>

                          <!-- Body -->
                          <div class="text-center mb-5">

                            <!-- Heading -->
                            <h2 class="card-title">
                              <a class="item-name" href="profile-posts.html">Ryu Duke</a>
                            </h2>

                            <!-- Text -->
                            <p class="small text-muted mb-3">
                              <span class="item-title">Developer</span> at <span class="item-company">Microsoft</span>
                            </p>

                            <!-- Buttons -->
                            <a class="btn btn-sm btn-white" href="tel:1-123-456-7890">
                              <i class="fe fe-phone me-1"></i> Call
                            </a>
                            <a class="btn btn-sm btn-white" href="mailto:john.doe@company.com">
                              <i class="fe fe-mail me-1"></i> Email
                            </a>

                          </div>

                          <!-- Divider -->
                          <hr class="card-divider mb-0">

                          <!-- List group -->
                          <div class="list-group list-group-flush mb-n3">
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Company</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Text -->
                                  <small>Microsoft</small>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Lead Score</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Badge -->
                                  <span class="item-score badge bg-warning-soft">6/10</span>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                          </div>

                        </div>
                      </div>

                    </div>
                    <div class="col-12 col-md-6 col-xl-4">

                      <!-- Card -->
                      <div class="card">
                        <div class="card-body">

                          <!-- Header -->
                          <div class="row align-items-center">
                            <div class="col">

                              <!-- Checkbox -->
                              <div class="form-check form-check-circle">
                                <input class="form-check-input list-checkbox" type="checkbox" id="cardsCheckBoxTen">
                                <label class="form-check-label" for="cardsCheckBoxTen"></label>
                              </div>

                            </div>
                            <div class="col-auto">

                              <!-- Dropdown -->
                              <div class="dropdown">
                                <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                  <i class="fe fe-more-vertical"></i>
                                </a>
                                <div class="dropdown-menu dropdown-menu-end">
                                  <a href="#!" class="dropdown-item">
                                    Action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Another action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Something else here
                                  </a>
                                </div>
                              </div>

                            </div>
                          </div> <!-- / .row -->

                          <!-- Image -->
                          <a href="profile-posts.html" class="avatar avatar-xl card-avatar">
                            <img src="assets/img/avatars/profiles/avatar-3.jpg" class="avatar-img rounded-circle" alt="...">
                          </a>

                          <!-- Body -->
                          <div class="text-center mb-5">

                            <!-- Heading -->
                            <h2 class="card-title">
                              <a class="item-name" href="profile-posts.html">Glen Rouse</a>
                            </h2>

                            <!-- Text -->
                            <p class="small text-muted mb-3">
                              <span class="item-title">Owner</span> at <span class="item-company">Uber</span>
                            </p>

                            <!-- Buttons -->
                            <a class="btn btn-sm btn-white" href="tel:1-123-456-7890">
                              <i class="fe fe-phone me-1"></i> Call
                            </a>
                            <a class="btn btn-sm btn-white" href="mailto:john.doe@company.com">
                              <i class="fe fe-mail me-1"></i> Email
                            </a>

                          </div>

                          <!-- Divider -->
                          <hr class="card-divider mb-0">

                          <!-- List group -->
                          <div class="list-group list-group-flush mb-n3">
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Company</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Text -->
                                  <small>Uber</small>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Lead Score</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Badge -->
                                  <span class="item-score badge bg-danger-soft">2/10</span>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                          </div>

                        </div>
                      </div>

                    </div>
                    <div class="col-12 col-md-6 col-xl-4">

                      <!-- Card -->
                      <div class="card">
                        <div class="card-body">

                          <!-- Header -->
                          <div class="row align-items-center">
                            <div class="col">

                              <!-- Checkbox -->
                              <div class="form-check form-check-circle">
                                <input class="form-check-input list-checkbox" type="checkbox" id="cardsCheckboxEleven">
                                <label class="form-check-label" for="cardsCheckboxEleven"></label>
                              </div>

                            </div>
                            <div class="col-auto">

                              <!-- Dropdown -->
                              <div class="dropdown">
                                <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                  <i class="fe fe-more-vertical"></i>
                                </a>
                                <div class="dropdown-menu dropdown-menu-end">
                                  <a href="#!" class="dropdown-item">
                                    Action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Another action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Something else here
                                  </a>
                                </div>
                              </div>

                            </div>
                          </div> <!-- / .row -->

                          <!-- Image -->
                          <a href="profile-posts.html" class="avatar avatar-xl card-avatar">
                            <img src="assets/img/avatars/profiles/avatar-4.jpg" class="avatar-img rounded-circle" alt="...">
                          </a>

                          <!-- Body -->
                          <div class="text-center mb-5">

                            <!-- Heading -->
                            <h2 class="card-title">
                              <a class="item-name" href="profile-posts.html">Dianna Smiley</a>
                            </h2>

                            <!-- Text -->
                            <p class="small text-muted mb-3">
                              <span class="item-title">Designer</span> at <span class="item-position">Twitter</span>
                            </p>

                            <!-- Buttons -->
                            <a class="btn btn-sm btn-white" href="tel:tel:1-123-456-7890">
                              <i class="fe fe-phone me-1"></i> Call
                            </a>
                            <a class="btn btn-sm btn-white" href="mailto:john.doe@company.com">
                              <i class="fe fe-mail me-1"></i> Email
                            </a>

                          </div>

                          <!-- Divider -->
                          <hr class="card-divider mb-0">

                          <!-- List group -->
                          <div class="list-group list-group-flush mb-n3">
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Company</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Text -->
                                  <small>Twitter</small>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Lead Score</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Badge -->
                                  <span class="item-score badge bg-warning-soft">6/10</span>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                          </div>

                        </div>
                      </div>

                    </div>
                    <div class="col-12 col-md-6 col-xl-4">

                      <!-- Card -->
                      <div class="card">
                        <div class="card-body">

                          <!-- Header -->
                          <div class="row align-items-center">
                            <div class="col">

                              <!-- Checkbox -->
                              <div class="form-check form-check-circle">
                                <input class="form-check-input list-checkbox" type="checkbox" id="cardsCheckboxTwelve">
                                <label class="form-check-label" for="cardsCheckboxTwelve"></label>
                              </div>

                            </div>
                            <div class="col-auto">

                              <!-- Dropdown -->
                              <div class="dropdown">
                                <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                  <i class="fe fe-more-vertical"></i>
                                </a>
                                <div class="dropdown-menu dropdown-menu-end">
                                  <a href="#!" class="dropdown-item">
                                    Action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Another action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Something else here
                                  </a>
                                </div>
                              </div>

                            </div>
                          </div> <!-- / .row -->

                          <!-- Image -->
                          <a href="profile-posts.html" class="avatar avatar-xl card-avatar">
                            <img src="assets/img/avatars/profiles/avatar-5.jpg" class="avatar-img rounded-circle" alt="...">
                          </a>

                          <!-- Body -->
                          <div class="text-center mb-5">

                            <!-- Heading -->
                            <h2 class="card-title">
                              <a class="item-name" href="profile-posts.html">Daniela Dewitt</a>
                            </h2>

                            <!-- Text -->
                            <p class="small text-muted mb-3">
                              <span class="item-title">Founder</span> at <span class="item-company">Netflix</span>
                            </p>

                            <!-- Buttons -->
                            <a class="btn btn-sm btn-white" href="tel:1-123-456-7890">
                              <i class="fe fe-phone me-1"></i> Call
                            </a>
                            <a class="btn btn-sm btn-white" href="mailto:john.doe@company.com">
                              <i class="fe fe-mail me-1"></i> Email
                            </a>

                          </div>

                          <!-- Divider -->
                          <hr class="card-divider mb-0">

                          <!-- List group -->
                          <div class="list-group list-group-flush mb-n3">
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Company</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Text -->
                                  <small>Netflix</small>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Lead Score</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Badge -->
                                  <span class="item-score badge bg-success-soft">8/10</span>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                          </div>

                        </div>
                      </div>

                    </div>
                    <div class="col-12 col-md-6 col-xl-4">

                      <!-- Card -->
                      <div class="card">
                        <div class="card-body">

                          <!-- Header -->
                          <div class="row align-items-center">
                            <div class="col">

                              <!-- Checkbox -->
                              <div class="form-check form-check-circle">
                                <input class="form-check-input list-checkbox" type="checkbox" id="cardsCheckBoxThirteen">
                                <label class="form-check-label" for="cardsCheckBoxThirteen"></label>
                              </div>

                            </div>
                            <div class="col-auto">

                              <!-- Dropdown -->
                              <div class="dropdown">
                                <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                  <i class="fe fe-more-vertical"></i>
                                </a>
                                <div class="dropdown-menu dropdown-menu-end">
                                  <a href="#!" class="dropdown-item">
                                    Action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Another action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Something else here
                                  </a>
                                </div>
                              </div>

                            </div>
                          </div> <!-- / .row -->

                          <!-- Image -->
                          <a href="profile-posts.html" class="avatar avatar-xl card-avatar">
                            <img src="assets/img/avatars/profiles/avatar-6.jpg" class="avatar-img rounded-circle" alt="...">
                          </a>

                          <!-- Body -->
                          <div class="text-center mb-5">

                            <!-- Heading -->
                            <h2 class="card-title">
                              <a class="item-name" href="profile-posts.html">Ab Hadley</a>
                            </h2>

                            <!-- Text -->
                            <p class="small text-muted mb-3">
                              <span class="item-title">Owner</span> at <span class="item-company">Lyft</span>
                            </p>

                            <!-- Buttons -->
                            <a class="btn btn-sm btn-white" href="tel:1-123-456-7890">
                              <i class="fe fe-phone me-1"></i> Call
                            </a>
                            <a class="btn btn-sm btn-white" href="mailto:john.doe@company.com">
                              <i class="fe fe-mail me-1"></i> Email
                            </a>

                          </div>

                          <!-- Divider -->
                          <hr class="card-divider mb-0">

                          <!-- List group -->
                          <div class="list-group list-group-flush mb-n3">
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Company</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Text -->
                                  <small>Lyft</small>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Lead Score</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Badge -->
                                  <span class="item-score badge bg-warning-soft">4/10</span>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                          </div>

                        </div>
                      </div>

                    </div>
                    <div class="col-12 col-md-6 col-xl-4">

                      <!-- Card -->
                      <div class="card">
                        <div class="card-body">

                          <!-- Header -->
                          <div class="row align-items-center">
                            <div class="col">

                              <!-- Checkbox -->
                              <div class="form-check form-check-circle">
                                <input class="form-check-input list-checkbox" type="checkbox" id="cardsCheckboxFourteen">
                                <label class="form-check-label" for="cardsCheckboxFourteen"></label>
                              </div>

                            </div>
                            <div class="col-auto">

                              <!-- Dropdown -->
                              <div class="dropdown">
                                <a href="#" class="dropdown-ellipses dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                  <i class="fe fe-more-vertical"></i>
                                </a>
                                <div class="dropdown-menu dropdown-menu-end">
                                  <a href="#!" class="dropdown-item">
                                    Action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Another action
                                  </a>
                                  <a href="#!" class="dropdown-item">
                                    Something else here
                                  </a>
                                </div>
                              </div>

                            </div>
                          </div> <!-- / .row -->

                          <!-- Image -->
                          <a href="profile-posts.html" class="avatar avatar-xl card-avatar">
                            <img src="assets/img/avatars/profiles/avatar-7.jpg" class="avatar-img rounded-circle" alt="...">
                          </a>

                          <!-- Body -->
                          <div class="text-center mb-5">

                            <!-- Heading -->
                            <h2 class="card-title">
                              <a class="item-name" href="profile-posts.html">Adolfo Hess</a>
                            </h2>

                            <!-- Text -->
                            <p class="small text-muted mb-3">
                              <span class="item-title">Designer</span> at <span class="item-position">Google</span>
                            </p>

                            <!-- Buttons -->
                            <a class="btn btn-sm btn-white" href="tel:tel:1-123-456-7890">
                              <i class="fe fe-phone me-1"></i> Call
                            </a>
                            <a class="btn btn-sm btn-white" href="mailto:john.doe@company.com">
                              <i class="fe fe-mail me-1"></i> Email
                            </a>

                          </div>

                          <!-- Divider -->
                          <hr class="card-divider mb-0">

                          <!-- List group -->
                          <div class="list-group list-group-flush mb-n3">
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Company</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Text -->
                                  <small>Google</small>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                            <div class="list-group-item">
                              <div class="row">
                                <div class="col">

                                  <!-- Text -->
                                  <small>Lead Score</small>

                                </div>
                                <div class="col-auto">

                                  <!-- Badge -->
                                  <span class="item-score badge bg-success-soft">7/10</span>

                                </div>
                              </div> <!-- / .row -->
                            </div>
                          </div>

                        </div>
                      </div>

                    </div>
                  </div>

                  <!-- Pagination -->
                  <div class="row g-0">

                    <!-- Pagination (prev) -->
                    <ul class="col list-pagination-prev pagination pagination-tabs justify-content-start">
                      <li class="page-item">
                        <button class="page-link"
                        :disabled="!previous_offset"
                        @click="(offset = previous_offset), getUsers()"
                        >
                          <i class="fe fe-arrow-left me-1"></i> Prev
                        </button>
                      </li>
                    </ul>

                    <!-- Pagination -->
                    <ul class="col list-pagination pagination pagination-tabs justify-content-center"></ul>

                    <!-- Pagination (next) -->
                    <ul class="col list-pagination-next pagination pagination-tabs justify-content-end">
                      <li class="page-item">
                        <button class="page-link" 
                        :disabled="next_offset == false"
                        @click="(offset = next_offset), getUsers()">
                          Next <i class="fe fe-arrow-right ms-1"></i>
                        </button>
                      </li>
                    </ul>

                  </div>

                  <!-- Alert -->
                  <div class="list-alert alert alert-dark alert-dismissible border fade" role="alert">

                    <!-- Content -->
                    <div class="row align-items-center">
                      <div class="col">

                        <!-- Checkbox -->
                        <div class="form-check">
                          <input class="form-check-input" id="cardAlertCheckbox" type="checkbox" checked disabled>
                          <label class="form-check-label text-white" for="cardAlertCheckbox">
                            <span class="list-alert-count">0</span> deal(s)
                          </label>
                        </div>

                      </div>
                      <div class="col-auto me-n3">

                        <!-- Button -->
                        <button class="btn btn-sm btn-white-20">
                          Edit
                        </button>

                        <!-- Button -->
                        <button class="btn btn-sm btn-white-20">
                          Delete
                        </button>

                      </div>
                    </div> <!-- / .row -->

                    <!-- Close -->
                    <button type="button" class="list-alert-close btn-close" aria-label="Close">

                    </button>

                  </div>

                </div>

              </div>
            </div>

          </div>
        </div> <!-- / .row -->
</template>
<script>
export default {
  props: ["pagination"],
  data() {
    return {
      users: {},
      busy: false,
      next_offset: false,
      previous_offset: false,
      offset: "",
      limit: 10,
      order_by: "-pk",
      search: ""
    };
  },
  mounted() {
    // docReady(tooltipInit);
    let _this = this;
    _this.getUsers();
  },
  methods: {
    getParameterByName(url, name) {
      var match = RegExp("[?&]" + name + "=([^&]*)").exec(url);
      return match && decodeURIComponent(match[1].replace(/\+/g, " "));
    },
    getUsers() {
      let _this = this;
      _this.busy = true;
      axios
        .get(
          `/users/?limit=${_this.limit}&offset=${_this.offset}&order_by=${_this.order_by}&search=${_this.search}`
        )
        .then((res) => {
          _this.users = res.data;
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
          _this.users = false;
        });
    },
    orderusersBy(order_by) {
      let _this = this;
      if (order_by == _this.order_by) {
        _this.order_by = `-${order_by}`;
      } else {
        _this.order_by = order_by;
      }
      _this.offset = "";
      _this.getUsers();
    },
  },
  watch: {
    busy(oldVal, newVal) {
      // docReady(tooltipInit);
    },
  },
};
</script>