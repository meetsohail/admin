<template>
    <div class="container-fluid">
        <div class="row justify-content-center">
          <div class="col-12 col-lg-10 col-xl-8">

            <!-- Header -->
            <div class="header mt-md-5">
              <div class="header-body">
                <div class="row align-items-center">
                  <div class="col">

                    <!-- Pretitle -->
                    <h6 class="header-pretitle">
                      Overview
                    </h6>

                    <!-- Title -->
                    <h1 class="header-title">
                      Account
                    </h1>

                  </div>
                </div> <!-- / .row -->
              <accounts-topbar></accounts-topbar>
              </div>
            </div>

     <!-- Card -->
            <div class="card">
              <div class="card-header">

                <!-- Title -->
                <h4 class="card-header-title">
                  Notifications
                </h4>

                <!-- Button -->
                <button class="btn btn-sm btn-white">
                  Disable all
                </button>

              </div>
              <div class="table-responsive">
                <table class="table table-sm table-nowrap card-table">
                  <thead>
                    <tr>
                      <th>Type</th>
                      <th class="text-center">Call</th>
                      <th class="text-center">Email</th>
                      <th class="text-center">SMS</th>
                    </tr>
                  </thead>
                  <tbody class="fs-base">
                    <tr>
                      <td>
                        Direct messages
                      </td>
                      <td class="text-center"></td>
                      <td class="text-center">

                        <!-- Checkbox -->
                        <div class="form-check d-inline-block me-n3">
                          <input class="form-check-input" type="checkbox" id="emailCheckboxOne" checked>
                          <label class="form-check-label" for="emailCheckboxOne"></label>
                        </div>

                      </td>
                      <td class="text-center">

                        <!-- Checkbox -->
                        <div class="form-check d-inline-block me-n3">
                          <input class="form-check-input" type="checkbox" id="smsCheckboxOne" checked>
                          <label class="form-check-label" for="smsCheckboxOne"></label>
                        </div>

                      </td>
                    </tr>
                    <tr>
                      <td>
                        Reminders
                      </td>
                      <td class="text-center"></td>
                      <td class="text-center">

                        <!-- Checkbox -->
                        <div class="form-check d-inline-block me-n3">
                          <input class="form-check-input" type="checkbox" id="emailCheckboxTwo" checked>
                          <label class="form-check-label" for="emailCheckboxTwo"></label>
                        </div>

                      </td>
                      <td class="text-center">

                        <!-- Checkbox -->
                        <div class="form-check d-inline-block me-n3">
                          <input class="form-check-input" type="checkbox" id="smsCheckboxTwo" checked>
                          <label class="form-check-label" for="smsCheckboxTwo"></label>
                        </div>

                      </td>
                    </tr>
                    <tr>
                      <td>
                        API Limits
                      </td>
                      <td class="text-center">

                        <!-- Checkbox -->
                        <div class="form-check d-inline-block me-n3">
                          <input class="form-check-input" type="checkbox" id="callCheckboxThree">
                          <label class="form-check-label" for="callCheckboxThree"></label>
                        </div>

                      </td>
                      <td class="text-center">

                        <!-- Checkbox -->
                        <div class="form-check d-inline-block me-n3">
                          <input class="form-check-input" type="checkbox" id="emailCheckboxThree" checked>
                          <label class="form-check-label" for="emailCheckboxThree"></label>
                        </div>

                      </td>
                      <td class="text-center">

                        <!-- Checkbox -->
                        <div class="form-check d-inline-block me-n3">
                          <input class="form-check-input" type="checkbox" id="smsCheckboxThree" checked>
                          <label class="form-check-label" for="smsCheckboxThree"></label>
                        </div>

                      </td>
                    </tr>
                    <tr>
                      <td>
                        Policy & Community
                      </td>
                      <td class="text-center">

                        <!-- Checkbox -->
                        <div class="form-check d-inline-block me-n3">
                          <input class="form-check-input" type="checkbox" id="callCheckboxFour">
                          <label class="form-check-label" for="callCheckboxFour"></label>
                        </div>

                      </td>
                      <td class="text-center">

                        <!-- Checkbox -->
                        <div class="form-check d-inline-block me-n3">
                          <input class="form-check-input" type="checkbox" id="emailCheckboxFour" checked>
                          <label class="form-check-label" for="emailCheckboxFour"></label>
                        </div>

                      </td>
                      <td class="text-center">

                        <!-- Checkbox -->
                        <div class="form-check d-inline-block me-n3">
                          <input class="form-check-input" type="checkbox" id="smsCheckboxFour" checked>
                          <label class="form-check-label" for="smsCheckboxFour"></label>
                        </div>

                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <br><br>

          </div>
        </div> <!-- / .row -->
      </div>

</template>
<script>
export default {
    data() {
        return {
        }
    }
};
</script>