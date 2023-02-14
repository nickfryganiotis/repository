<template>
  <q-card class="rounded-borders">
    <img :src="img" />
    <q-card-section>
      <q-rating
        :model-value="ratingModel"
        size="2em"
        :max="5"
        color="yellow"
        readonly
      />
      <div class="q-pa-xs text-caption">317 responses</div>
    </q-card-section>
    <q-card-section class="q-pt-none">
      {{ text }}
    </q-card-section>
  </q-card>
</template>

<script>
/* used value instead of v-model as i cannot mutate it*/
import { defineComponent } from "vue";

export default defineComponent({
  name: "ActivityCard",
  props: {
    img: { type: String },
    ratingModel: { type: Number },
    text: { type: String },
  },
});
</script>
