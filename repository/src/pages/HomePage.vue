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
          <q-card
            class="rounded-borders col-2"
            v-for="(img, index) in carousels[n - 1]"
            :key="index"
          >
            <img :src="img" />

            <q-card-section>
              <q-rating
                v-model="ratingModel"
                size="2em"
                :max="5"
                color="yellow"
                readonly
              />

              <div class="q-pa-xs text-caption">317 responses</div>
            </q-card-section>

            <q-card-section class="q-pt-none">
              {{ lorem }}
            </q-card-section>
          </q-card>
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
        <q-card
          v-for="(img, index) in activities.slice((n - 1) * 4, n * 4)"
          class="rounded-borders col-2"
          :key="index"
        >
          <img :src="img" />
          <q-card-section>
            <q-rating
              v-model="ratingModel"
              size="2em"
              :max="5"
              color="yellow"
              readonly
            />

            <div class="q-pa-xs text-caption">317 responses</div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            {{ lorem }}
          </q-card-section>
        </q-card>
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
</template>

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "IndexPage",

  setup() {
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
    };
  },
});
</script>
