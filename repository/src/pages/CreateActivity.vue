<template>
  <div class="col q-mt-lg q-ml-lg q-pt-lg">
    <div class="text-h4">1/6 Create a new Activity</div>
  </div>
  <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
    <div class="text-body2">What is the title of the activity:</div>
    <q-input
      filled
      v-model="activity_title"
      lazy-rules
      :rules="[(val) => (val && val.length > 0) || 'Please type something']"
    />
  </div>
  <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
    <div class="text-body2">
      Give a short description of the acitivity (objectives and/or methology, 70
      words)
    </div>
    <q-input
      filled
      v-model="short_description"
      lazy-rules
      :rules="[(val) => (val && val.length > 0) || 'Please type something']"
    />
  </div>
  <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
    <div class="text-body2">Describe the activity in detail (500 words)</div>
    <q-input
      class="max-width: 300px"
      v-model="description"
      filled
      type="textarea"
    />
  </div>

  <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
    <div class="text-body2">
      Should the activity be executed periodically? This means that the activity
      could be integrated to the routines of the classroom.
    </div>
    <q-radio v-model="periodicity" val="yes" label="Yes" />
    <div></div>
    <q-radio v-model="periodicity" val="no" label="No" />
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    return {
      activity_title: ref(""),
      short_description: ref(""),
      description: ref(""),
      periodicity: ref("no"),
    };
  },
});
</script>
