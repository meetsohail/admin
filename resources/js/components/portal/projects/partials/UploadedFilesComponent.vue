<template>
  <div class="card" v-if="importkeywords">
        <div class="card-header bg-light">
        <div class="row">
        <div class="col-lg-3">
          <h5 class="float-left">Uploaded Files</h5>
        </div>
          </div>
        </div>
        <div class="card-body">
           <div v-if="busy" class="row g-0 p-4 text-center">
            <loading-component
              :busy="busy"
              bText="Loading keyword data..."
            ></loading-component>
          </div>
          <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
              <thead>
                <tr>
                  <th>File Name</th>
                  <th>File Source</th>
                  <th>Created at</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody v-if="importkeywords.count > 0">
                <tr v-for="file in importkeywords.results" :key="file.id">
                <td>{{ file.csv_file }}</td>
                  <td v-text="file.file_source"></td>
                 
                  <td>{{ file.created_at }}</td>
                  <td v-if="file.is_processed"><span class="badge badge-success">Processed</span></td>
                  <td v-else><span class="badge bg-info">In Process</span></td>
                </tr>
                </tbody>
              <tbody v-else>
                <tr>
                  <td class="text-center" colspan="4">File not found!</td>
                </tr>
              </tbody>
            </table>
            
            <div class="card-footer bg-light text-right">
              <button
                :disabled="!key_prev_offset"
                @click="(offset = key_prev_offset), getImportKeywords()"
                class="btn btn-falcon-default"
              >
                Previous
              </button>
              <button
                :disabled="key_next_offset == false"
                @click="(offset = key_next_offset), getImportKeywords()"
                class="btn btn-falcon-default"
              >
                Next
              </button>
            </div>
          </div>
        </div>
      </div>
</template>