<template>
  <MenuBtn label="label" />
</template>

<script>
import { defineComponent, ref } from "vue";
import MenuBtn from "src/components/MenuBtn";
import axios from "axios";
axios.get("http://localhost:5000/").then((resp) => {
  console.log(resp.data);
});
export default defineComponent({
  components: { MenuBtn },
  setup() {
    return { label: ref("Label") };
  },
});
</script>
