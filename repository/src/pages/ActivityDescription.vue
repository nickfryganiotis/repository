<template>
  <div class="row q-pa-lg">
    <div class="col-2"></div>
    <div class="col-2">
      <q-img :src="activity"></q-img>
    </div>
    <div class="col-2 q-ml-md">
      <div class="text-h4 text-weight-regular">{{ title }}</div>
      <q-rating
        :model-value="ratingModel"
        size="2em"
        :max="5"
        color="yellow"
        readonly
      />
      <div>317 responses</div>
      <p>
        Short description bla bla bla bla bla bla bla bla bla bla bla bla bla
        bla bla bla
      </p>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  props: {
    title: { type: String },
  },
  setup() {
    return {
      activity: "https://cdn.quasar.dev/img/mountains.jpg",
      ratingModel: 3,
    };
  },
});
</script>
