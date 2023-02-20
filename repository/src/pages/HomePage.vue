<template>
  <q-page>
    <div class="row q-pt-xl">
      <div class="col-1"></div>
      <div class="col text-body1 text-weight-regular">
        The most popular activities
      </div>
    </div>

    <q-carousel
      v-model="slide"
      transition-prev="slide-right"
      transition-next="slide-left"
      swipeable
      animated
      control-color="primary"
      infinite
      padding
      arrows
      height="500px"
      class="shadow-2 q-mt-lg rounded-borders"
    >
      <q-carousel-slide
        v-for="n in 4"
        :key="n"
        :name="n"
        class="column no-wrap"
      >
        <div
          class="row fit justify-start items-center q-gutter-xs q-col-gutter no-wrap"
        >
          <div class="col-2"></div>
          <div v-if="status === 'loading'">Loading...</div>
          <ActivityCard
            v-else
            class="col-2"
            v-for="(act, index) in Object.values(data).slice(
              (n - 1) * 4,
              n * 4
            )"
            :key="index"
            :img="act['img_url']"
            :ratingModel="ratingModel"
            :text="lorem"
          />

          <div class="col-2"></div>
        </div>
        <div
          class="row fit justify-start items-center q-gutter-xs q-col-gutter no-wrap"
        >
          <div class="col-2"></div>
          <q-btn
            v-for="n in 4"
            :key="n"
            class="rounded-borders col-2"
            label="Short activity description"
            @click="goToActivityDescription"
          />
          <div class="col-2"></div>
        </div>
      </q-carousel-slide>
    </q-carousel>

    <div class="row q-pt-lg">
      <div class="col-1"></div>
      <div class="col text-body1 text-weight-regular">All activities</div>
    </div>
    <div v-for="n in counter" :key="n">
      <div
        class="q-pt-lg row fit items-center q-gutter-xs q-col-gutter no-wrap"
      >
        <div class="col-2"></div>
        <div v-if="status === 'loading'">Loading...</div>
        <ActivityCard
          v-else
          class="col-2"
          v-for="(act, index) in Object.values(data).slice((n - 1) * 4, n * 4)"
          :key="index"
          :img="act['img_url']"
          :ratingModel="ratingModel"
          :text="lorem"
        />
        <div class="col-2"></div>
      </div>
      <div
        class="q-pt-lg row fit justify-start items-center q-gutter-xs q-col-gutter no-wrap"
      >
        <div class="col-2"></div>
        <q-btn
          v-for="n in 4"
          :key="n"
          class="rounded-borders col-2"
          label="Short activity description"
        />

        <div class="col-2"></div>
      </div>
    </div>

    <div class="row reverse q-pr-lg">
      <q-btn
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
import { defineComponent, ref, reactive } from "vue";
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
    const goToActivityDescription = () => {
      push("/activity_description");
    };
    const activities_back = reactive({
      carousels: "",
      total_act: "",
    });

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
      lorem:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
      ratingModel: ref(3),
      activities_back,
      route,
      goToActivityDescription,
      status,
      data,
      error,
    };
  },
});
</script>
