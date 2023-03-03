<template>
  <q-card class="rounded-borders">
    <q-card-section>
      <router-link
        :to="{
          name: 'ActivityDescription',
          params: { activityId: id },
        }"
      >
        <div class="text-h5">{{ title }}</div>
      </router-link>
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
      <div class="row q-pt-xs text-negative">
        <div
          v-for="(emo_comp, index) in emosocio_competences"
          :key="index"
          @click="getActivityDefinition($event)"
        >
          {{ `${emo_comp},` }}
        </div>
      </div>
    </q-card-section>
    <q-dialog v-model="popup">
      <q-card>
        <q-card-section>
          <div class="text-h6">{{ act_name }}</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          {{ act_def }}
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="OK" color="primary" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-card>
</template>

<script>
/* used value instead of v-model as i cannot mutate it*/
import { defineComponent, ref } from "vue";
import { emo_comp_defs } from "src/texts/emosocio_competences";

export default defineComponent({
  name: "ActivityCard",
  props: {
    id: { type: Number },
    title: { type: String },
    target_age_group_left: { type: Number },
    target_age_group_right: { type: Number },
    ratingModel: { type: Number },
    responses: { type: Number },
    emosocio_competences: { type: Array },
  },

  setup(props) {
    const popup = ref(false);
    const act_name = ref("");
    const act_def = ref("");
    const getActivityDefinition = (e) => {
      console.log(e.target.textContent.slice(0, -1));
      act_name.value = e.target.textContent.slice(0, -1);
      act_def.value = emo_comp_defs[act_name.value];
      popup.value = true;
    };
    return { getActivityDefinition, popup, act_def, act_name };
  },
});
</script>
