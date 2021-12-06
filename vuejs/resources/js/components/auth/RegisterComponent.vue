<template>
  <div>
    <logo-component />
    <div class="alert alert-primary" v-if="$route.query.trial">
      Sign up and add a card to your account. Our system will then apply test credits so
      you can trial our API before you make any commitment.
    </div>
    <div class="card">
      <div class="card-body p-4 p-sm-5">
        <div class="row text-left justify-content-between align-items-center mb-2">
          <div class="col-auto">
            <h5>Sign up</h5>
          </div>
          <div class="col-auto">
            <p class="fs--1 text-600 mb-0">
              or <router-link :to="{ name: 'login' }">Sign in</router-link>
            </p>
          </div>
        </div>
        <div class="mb-3">
          <input
            class="form-control"
            :class="{ 'is-invalid': errors.first_name }"
            :disabled="busy"
            v-model="first_name"
            type="text"
            placeholder="First name"
          />
          <div v-if="errors.first_name" class="invalid-feedback">
            {{ errors.first_name[0] }}
          </div>
        </div>
        <div class="mb-3">
          <input
            class="form-control"
            :class="{ 'is-invalid': errors.last_name }"
            :disabled="busy"
            v-model="last_name"
            type="text"
            placeholder="Last name"
          />
          <div v-if="errors.last_name" class="invalid-feedback">
            {{ errors.last_name[0] }}
          </div>
        </div>
        <div class="mb-3">
          <input
            class="form-control"
            :class="{ 'is-invalid': errors.email }"
            :disabled="busy"
            v-model="email"
            type="email"
            placeholder="Email address"
          />
          <div v-if="errors.email" class="invalid-feedback">
            {{ errors.email[0] }}
          </div>
        </div>
        <div class="mb-3">
          <input
            class="form-control"
            autocomplete="new-password"
            :class="{ 'is-invalid': errors.password }"
            :disabled="busy"
            v-model="password"
            type="password"
            placeholder="Password"
          />
          <div v-if="errors.password" class="invalid-feedback">
            {{ errors.password[0] }}
          </div>
        </div>
        <div class="mb-3">
          <input
            class="form-control"
            :class="{ 'is-invalid': errors.confirm_password }"
            :disabled="busy"
            v-model="confirm_password"
            type="password"
            placeholder="Confirm password"
          />
          <div v-if="errors.confirm_password" class="invalid-feedback">
            {{ errors.confirm_password[0] }}
          </div>
        </div>
        <div class="mb-3">
          <button
            @click="signIn()"
            :disabled="busy"
            class="btn btn-primary btn-block mt-3"
          >
            <span v-if="busy">Creating account...</span>
            <span v-else>Create account</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import LogoComponent from "./partials/LogoComponent";
export default {
  components: {
    LogoComponent,
  },
  data() {
    return {
      first_name: "",
      last_name: "",
      email: "",
      password: "",
      confirm_password: "",
      busy: false,
      errors: false,
    };
  },
  methods: {
    signIn() {
      let _this = this;
      _this.busy = true;
      _this.errors = false;
      let fd = new FormData();
      fd.append("email", _this.email);
      fd.append("password", _this.password);
      fd.append("first_name", _this.first_name);
      fd.append("last_name", _this.last_name);
      fd.append("confirm_password", _this.confirm_password);
      axios
        .post("/do-register/", fd)
        .then((res) => {
          _this.busy = false;
          window.location = "";
        })
        .catch((err) => {
          _this.errors = err.response.data.errors;
          _this.busy = false;
        });
    },
  },
};
</script>
