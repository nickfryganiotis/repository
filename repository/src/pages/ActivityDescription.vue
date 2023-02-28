<template>
  <div class="row q-pa-lg" v-if="status === 'success'">
    <div class="col-2"></div>

    <div class="col-2 q-ml-md">
      <div class="text-h4 text-weight-regular">
        {{ posts["activity_title"] }}
      </div>
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
import { useRoute } from "vue-router";
import axios from "axios";
import { useQuery } from "vue-query";

export default defineComponent({
  setup() {
    //const activityId = computed(() => route.params.activityId);
    const route = useRoute();
    const {
      status,
      data: posts = [],
      error,
    } = useQuery("getActivity", async () => {
      //act_id = route.params.activityId;
      //console.log(act_id);

      const resp = await axios.get("http://localhost:5000/get_activity", {
        params: { activity_id: route.params.activityId },
      });
      console.log(resp);
      return resp.data;
      //.then((resp) => {
      //        return resp.data;
      //    })
      //  .catch((error) => {
      //  return error;
      //});
    });

    return {
      ratingModel: 3,
      //activityId,
      status,
      posts,
      error,
    };
  },
});
</script>
