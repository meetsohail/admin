<template>
  <div>
    <div class="row no-gutters">
      <div class="row">
        <div class="col-12">
          <div class="card mb-3">
            <div class="card-header bg-light">
              <div class="row align-items-center justify-content-between">
                <div class="col-6 col-sm-auto d-flex align-items-center pr-0">
                  <h5 class="fs-0 mb-0 text-nowrap py-2 py-xl-0">
                    Manage Users
                    <!-- <span v-if="users.count"> ({{ users.count | toNumber }})</span> -->
                  </h5>
                  <input
                        v-model="search"
                        @keyup.enter="getUsers()"
                        type="text"
                        class="form-control ml-4"
                        placeholder="Search users..."
                      />
                </div>
              </div>
            </div>
            <div class="card-body px-0 pt-0">
              <div v-if="busy" class="row g-0 p-4 text-center">
                <loading-component
                  :busy="busy"
                  nText
                  bText="Loading users..."
                ></loading-component>
              </div>
              <div v-else>
                <div v-if="!users || users.count == 0" class="row g-0 pt-4 text-center">
                  <h3 class="text-center text-muted">No users found!</h3>
                </div>
                <div v-else class="row g-0">
                  <div class="table-responsive">
                    <table class="table">
                      <thead class="bg-dark text-white gradient-dark text-white">
                        <tr>
                          <th>Name</th>
                          <th>Email Address</th>
                          <th colspan="2">
                            <a
                              class="text-decoration-none text-white"
                              @click="orderusersBy('date_joined')"
                              href="javascript:void(0)"
                            >
                              <i v-if="order_by == 'date_joined'" class="fas fa-arrow-up"></i>
                              <i
                                v-if="order_by == '-date_joined'"
                                class="fas fa-arrow-down"
                              ></i>
                              Date Joined
                            </a>
                          </th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="user in users.results" :key="user.id">
                          <td>{{ user.first_name }} {{ user.last_name }}</td>
                          <td>{{ user.email }}</td>
                          <td>{{ user.date_joined }}</td>
                          <td>
                            <router-link :to="{name: 'updateuser', params:{id: user.id}}" class="btn btn-black btn-sm text-white">
                              <i class="fas fa-edit"></i> 
                            </router-link>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
            <div class="card-footer bg-light text-right">
              <button
                :disabled="!previous_offset"
                @click="(offset = previous_offset), getUsers()"
                class="btn btn-falcon-default"
              >
                Previous
              </button>
              <button
                :disabled="next_offset == false"
                @click="(offset = next_offset), getUsers()"
                class="btn btn-falcon-default"
              >
                Next
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
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
    docReady(tooltipInit);
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
      docReady(tooltipInit);
    },
  },
};
</script>
