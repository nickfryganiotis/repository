<template>
  <div class="col q-mt-lg q-ml-lg q-pt-lg">
    <div class="text-h4">{{ page }}/6 Create a new Activity</div>
  </div>
  <div v-if="page == 1">
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
        Give a short description of the acitivity (objectives and/or methology,
        70 words)
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
        Should the activity be executed periodically? This means that the
        activity could be integrated to the routines of the classroom.
      </div>
      <q-radio v-model="periodicity" val="yes" label="Yes" />
      <div></div>
      <q-radio v-model="periodicity" val="no" label="No" />
    </div>

    <div class="row q-my-md q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2 col-12">
        What is the duration of the activity? (an activity with more than four
        hours of duration should be presented as a different activity)
      </div>
      <q-checkbox
        class="col-3"
        v-model="lective_hours.one"
        label="one lective hour (50 minutes)"
      />
      <q-checkbox
        class="col-3"
        v-model="lective_hours.four"
        label="four lective hours"
      />
      <div class="col-6"></div>
      <q-checkbox
        class="col-3"
        v-model="lective_hours.two"
        label="two lective hours"
      />
      <q-checkbox class="col-3" v-model="lective_hours.other" label="Other" />
      <div class="col-6"></div>
      <q-checkbox v-model="lective_hours.three" label="three lective hours" />
    </div>
  </div>
  <div v-else-if="page == 2"></div>
  <div class="row justify-end q-pr-lg q-py-md">
    <q-btn label="Next" color="primary" @click="page++" />
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
      page: ref(1),
      lective_hours: ref({
        one: false,
        two: false,
        three: false,
        four: false,
        other: false,
      }),
    };
  },
});
</script>
