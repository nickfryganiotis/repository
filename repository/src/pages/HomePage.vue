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
          <ActivityCard
            class="col-2"
            v-for="(img, index) in carousels[n - 1]"
            :key="index"
            :img="img"
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
        <ActivityCard
          class="col-2"
          v-for="(img, index) in activities.slice((n - 1) * 4, n * 4)"
          :key="index"
          :img="img"
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
          counter = counter * 4 < activities.length ? counter + 1 : counter
        "
      ></q-btn>
    </div>
  </q-page>
  <div>{{ activities_back.total_act[0] }}</div>
</template>

<script>
import { defineComponent, ref, reactive, onBeforeMount } from "vue";
import ActivityCard from "src/components/ActivityCard.vue";
import { useRouter, useRoute } from "vue-router";
import axios from "axios";

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
    onBeforeMount(() => {
      axios.get("http://localhost:5000/get_activities").then((resp) => {
        activities_back.carousels = [
          resp.data.slice(0, 4),
          resp.data.slice(4, 8),
          resp.data.slice(8, 12),
          resp.data.slice(12, 16),
        ];
        activities_back.total_act = resp.data;
        console.log(activities_back.total_act);
      });
    });

    return {
      slide: ref(1),
      showMore: ref(false),
      carousels: ref([
        [
          "https://cdn.quasar.dev/img/mountains.jpg",
          "https://cdn.quasar.dev/img/parallax1.jpg",
          "https://cdn.quasar.dev/img/mountains.jpg",
          "https://cdn.quasar.dev/img/parallax1.jpg",
        ],
        [
          "https://cdn.quasar.dev/img/parallax2.jpg",
          "https://cdn.quasar.dev/img/parallax2.jpg",
          "https://cdn.quasar.dev/img/parallax2.jpg",
          "https://cdn.quasar.dev/img/parallax2.jpg",
        ],
        [
          "https://cdn.quasar.dev/img/parallax2.jpg",
          "https://cdn.quasar.dev/img/parallax2.jpg",
          "https://cdn.quasar.dev/img/parallax2.jpg",
          "https://cdn.quasar.dev/img/parallax2.jpg",
        ],
        [
          "https://cdn.quasar.dev/img/mountains.jpg",
          "https://cdn.quasar.dev/img/parallax1.jpg",
          "https://cdn.quasar.dev/img/mountains.jpg",
          "https://cdn.quasar.dev/img/parallax1.jpg",
        ],
      ]),

      activities: ref([
        "https://cdn.quasar.dev/img/mountains.jpg",
        "https://cdn.quasar.dev/img/parallax1.jpg",
        "https://cdn.quasar.dev/img/mountains.jpg",
        "https://cdn.quasar.dev/img/parallax1.jpg",
        "https://cdn.quasar.dev/img/parallax2.jpg",
        "https://cdn.quasar.dev/img/parallax2.jpg",
        "https://cdn.quasar.dev/img/parallax2.jpg",
        "https://cdn.quasar.dev/img/parallax2.jpg",
        "https://cdn.quasar.dev/img/parallax2.jpg",
        "https://cdn.quasar.dev/img/parallax2.jpg",
        "https://cdn.quasar.dev/img/parallax2.jpg",
        "https://cdn.quasar.dev/img/parallax2.jpg",
        "https://cdn.quasar.dev/img/mountains.jpg",
        "https://cdn.quasar.dev/img/parallax1.jpg",
        "https://cdn.quasar.dev/img/mountains.jpg",
        "https://cdn.quasar.dev/img/parallax1.jpg",
      ]),
      counter: ref(1),
      lorem:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
      ratingModel: ref(3),
      activities_back,
      route,
      goToActivityDescription,
    };
  },
});
</script>
