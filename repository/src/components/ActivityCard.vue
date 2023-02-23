<template>
  <q-card class="rounded-borders">
    <q-card-section>
      <div class="text-h5">{{ title }}</div>
    </q-card-section>
    <q-card-section class="q-pt-none">
      <q-rating
        :model-value="ratingModel"
        size="2em"
        :max="5"
        color="yellow"
        readonly
      />
      <div class="q-pl-xs q-pt-xs text-caption">
        {{ `${responses} responses` }}
      </div>
      <div class="q-pt-xs">
        {{ `${target_age_group_left} - ${target_age_group_right} years old` }}
      </div>
      <div class="q-pt-xs text-negative">{{ text }}</div>
    </q-card-section>
  </q-card>
</template>

<script>
/* used value instead of v-model as i cannot mutate it*/
import { defineComponent } from "vue";

export default defineComponent({
  name: "ActivityCard",
  props: {
    title: { type: String },
    target_age_group_left: { type: Number },
    target_age_group_right: { type: Number },
    ratingModel: { type: Number },
    responses: { type: Number },
    text: { type: String },
  },
});
</script>
