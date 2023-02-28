<template>
  <q-page>
    <div class="row q-pt-xl">
      <div class="col-1"></div>
      <div class="col text-h5 text-weight-regular">
        The most popular activities
      </div>
    </div>

    <q-carousel
      v-if="status === 'success'"
      v-model="slide"
      transition-prev="slide-right"
      transition-next="slide-left"
      swipeable
      animated
      control-color="primary"
      infinite
      padding
      arrows
      height="350px"
      class="shadow-2 q-mt-lg rounded-borders"
    >
      <q-carousel-slide
        v-for="n in 4"
        :key="n"
        :name="n"
        class="column no-wrap"
      >
        <div
          class="q-pt-md row fit justify-start items-center q-gutter-xs q-col-gutter no-wrap"
        >
          <div class="col-2"></div>

          <ActivityCard
            class="col-2"
            v-for="(act, index) in Object.values(data).slice(
              (n - 1) * 4,
              n * 4
            )"
            :id="act['id']"
            :title="act['activity_title']"
            :target_age_group_left="act['target_age_group_left']"
            :target_age_group_right="act['target_age_group_right']"
            :key="index"
            :ratingModel="ratingModel[(n - 1) * 4 + index]"
            :responses="responses[(n - 1) * 4 + index]"
            :emosocio_competences="act['emosocio_competences'].join(', ')"
          />

          <div class="col-2"></div>
        </div>
      </q-carousel-slide>
    </q-carousel>

    <div class="row q-pt-lg">
      <div class="col-1"></div>
      <div class="col text-h5 text-weight-regular">All activities</div>
    </div>
    <div v-for="n in counter" :key="n">
      <div
        class="q-pt-xl row fit items-center q-gutter-xs q-col-gutter no-wrap"
      >
        <div class="col-2"></div>
        <div v-if="status === 'loading'">Loading...</div>
        <ActivityCard
          v-else-if="status === 'success'"
          class="col-2"
          v-for="(act, index) in Object.values(data).slice((n - 1) * 4, n * 4)"
          :id="act['id']"
          :title="act['activity_title']"
          :target_age_group_left="act['target_age_group_left']"
          :target_age_group_right="act['target_age_group_right']"
          :key="index"
          :ratingModel="ratingModel[(n - 1) * 4 + index]"
          :responses="responses[(n - 1) * 4 + index]"
          :emosocio_competences="act['emosocio_competences'].join(', ')"
        />
        <div class="col-2"></div>
      </div>
    </div>

    <div class="row justify-end q-pr-lg q-py-md">
      <q-btn
        v-if="status === 'success'"
        flat
        label="Show more"
        @click="
          counter =
            counter * 4 < Object.values(data).length ? counter + 1 : counter
        "
      ></q-btn>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref, reactive, computed } from "vue";
import ActivityCard from "src/components/ActivityCard.vue";
import { useRouter, useRoute } from "vue-router";
import axios from "axios";
import { useQuery } from "vue-query";

export default defineComponent({
  name: "IndexPage",
  components: { ActivityCard },

  setup() {
    const { push } = useRouter();
    const route = useRoute();
    const goToActivityDescription = (title) => {
      push({ path: "/activity_description", props: { title: title } });
    };

    const { status, data, error } = useQuery("getActivities", () =>
      axios
        .get("http://localhost:5000/get_activities")
        .then((resp) => {
          return resp.data;
        })
        .catch((error) => {
          return error;
        })
    );

    return {
      slide: ref(1),
      showMore: ref(false),
      counter: ref(1),
      ratingModel: ref([3, 1, 3, 2, 1, 4, 3, 2, 1, 3, 3, 2, 1, 3, 2, 2]),
      responses: ref([
        317, 102, 317, 205, 102, 404, 317, 205, 102, 317, 317, 205, 102, 317,
        205, 205,
      ]),
      route,
      goToActivityDescription,
      status,
      error,
      data,
    };
  },
});
</script>
