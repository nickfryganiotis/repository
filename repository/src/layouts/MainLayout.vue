<template>
  <q-layout view="lhh LpR lFf">
    <q-header elevated>
      <q-toolbar class="justify-between q-py-sm">
        <q-space />

        <q-btn
          class="text-body1 text-weight-medium"
          no-caps
          stretch
          flat
          :ripple="false"
          label="Educardia"
        />

        <q-btn
          class="text-body1 text-weight-medium"
          no-caps
          stretch
          flat
          :ripple="false"
          label="EmoSocio"
        />

        <q-btn
          class="text-body1 text-weight-medium"
          no-caps
          stretch
          flat
          :ripple="false"
          label="EmoSociograms"
        />
      </q-toolbar>
      <q-toolbar class="bg-white text-primary justify-between q-py-md">
        <div class="row cursor-pointer" @click="goToLandingPage">
          <q-avatar rounded>
            <img src="../assets/Transparent-Logo-1.webp" alt="logo" />
          </q-avatar>
          <q-toolbar-title style="font-family: 'Lobster'; font-size: 22px">
            Repository
          </q-toolbar-title>
        </div>

        <q-space />

        <q-btn
          class="text-body1 text-weight-medium"
          no-caps
          stretch
          flat
          :ripple="false"
          label="Home"
          @click="goToLandingPage"
        />

        <q-btn
          class="text-body1 text-weight-medium"
          no-caps
          stretch
          flat
          :ripple="false"
          label="Create a New activity"
        />

        <q-btn
          class="text-body1 text-weight-medium"
          no-caps
          stretch
          flat
          :ripple="false"
          label="Search for an Activity"
          @click="goToSearchActivityPage"
        />

        <q-btn
          class="text-body1 text-weight-medium"
          no-caps
          stretch
          flat
          :ripple="false"
          label="Contact"
        />
      </q-toolbar>
    </q-header>

    <q-page-container>
      <q-separator />

      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from "vue";
import { useRouter, useRoute } from "vue-router";
//import { SecMenuBtn } from "../components/SecMenuBtn";
import { fabPython } from "@quasar/extras/fontawesome-v6";

export default defineComponent({
  name: "MainLayout",

  components: {
    //SecMenuBtn,
  },

  setup() {
    const leftDrawerOpen = ref(false);
    const label = ref("Educardia");
    const { push } = useRouter();
    const route = useRoute();
    const goToLandingPage = () => {
      push("/");
    };
    const goToSearchActivityPage = () => {
      push("/search_activity");
    };

    return {
      leftDrawerOpen,
      label,
      fabPython,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
      route,
      goToLandingPage,
      goToSearchActivityPage,
    };
  },
});
</script>

<style scoped>
.custom-height {
  height: 100px;
}
</style>
