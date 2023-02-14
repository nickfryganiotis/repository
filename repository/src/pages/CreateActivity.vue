<template>
  <MenuBtn label="label" />
</template>

<script>
import { defineComponent, ref } from "vue";
import MenuBtn from "src/components/MenuBtn";

export default defineComponent({
  components: { MenuBtn },
  setup() {
    return { label: ref("Label") };
  },
});
</script>
