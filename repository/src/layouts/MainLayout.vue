<template>
  <q-layout view="lhh LpR lFf">
    <q-header elevated>
      <q-toolbar class="justify-between q-py-sm">
        <q-space />

        <MenuBtn
          target="_blank"
          v-for="(item, index) in secondaryMenu"
          :key="index"
          :label="item['label']"
          :href="item['url']"
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

        <MenuBtn label="Home" @click="goToLandingPage" />

        <MenuBtn
          label="Create a new activity"
          @click="goToCreateActivityPage"
        />

        <MenuBtn
          label="Search for an activity"
          @click="goToSearchActivityPage"
        />

        <MenuBtn label="Contact" @click="gotToContactPage" />
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
import MenuBtn from "../components/MenuBtn";
import { fabPython } from "@quasar/extras/fontawesome-v6";

export default defineComponent({
  name: "MainLayout",

  components: {
    MenuBtn,
  },

  setup() {
    const leftDrawerOpen = ref(false);
    const secondaryMenu = [
      { label: "Educardia", url: "https://educardia.eu/" },
      { label: "EmoSocio", url: "https://netmode.gitlab.io/emosocio/" },
      { label: "EmoSociograms", url: "https://emosociograms.com/" },
    ];

    const { push } = useRouter();
    const route = useRoute();
    const goToLandingPage = () => {
      push("/");
    };
    const goToSearchActivityPage = () => {
      push("/search_activity");
    };
    const goToCreateActivityPage = () => {
      push("/create_activity");
    };
    const gotToContactPage = () => {
      push("/contact_page");
    };

    return {
      leftDrawerOpen,
      secondaryMenu,
      fabPython,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
      route,
      goToLandingPage,
      goToSearchActivityPage,
      goToCreateActivityPage,
      gotToContactPage,
    };
  },
});
</script>

<style scoped>
.custom-height {
  height: 100px;
}
</style>
