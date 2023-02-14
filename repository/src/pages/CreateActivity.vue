<template>
  <SecMenuBtn label="label" />
</template>

<script>
import { defineComponent, ref } from "vue";
import SecMenuBtn from "src/components/SecMenuBtn";

export default defineComponent({
  components: { SecMenuBtn },
  setup() {
    return { label: ref("Label") };
  },
});
</script>
