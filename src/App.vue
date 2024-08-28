<template>
  <v-app :theme="theme">
    <v-app-bar color="purple-darken-3" class="px-3">
      <template v-slot:prepend>
        <v-avatar size="32px" class="ml-3">
          <v-img
            alt="Avatar"
            src="@/../public/icon/android-chrome-192x192.png"
          ></v-img>
        </v-avatar>
      </template>
      <v-toolbar-title>
        <strong>The Bookmarks</strong>
        <span class="hidden-sm-and-down">
          find the desired sites with one click
        </span>
      </v-toolbar-title>

      <!-- <v-spacer></v-spacer> -->

      <v-btn
        class="mr-6"
        prepend-icon="fas fa-map-signs"
        slim
        @click.stop="drawer = !drawer"
      >
        {{ drawer ? "Close" : "Open" }} Word Cloud
      </v-btn>

      <v-btn
        :prepend-icon="theme === 'light' ? 'far fa-sun' : 'far fa-moon'"
        slim
        @click="changeTheme"
      >
        Switch {{ theme === "light" ? "Light" : "Dark" }} Mode
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer
      location="right"
      :width="600"
      v-model="drawer"
      temporary
      class="pt-4"
    >
      <WordCloud />
    </v-navigation-drawer>

    <v-main>
      <v-app-bar color="transparent" :elevation="0">
        <SearchInput />
      </v-app-bar>
      <Bookmark />
    </v-main>
  </v-app>
</template>

<script setup>
import WordCloud from "@/components/WordCloud.vue";
import Bookmark from "@/components/Bookmark.vue";
import SearchInput from "@/components/SearchInput.vue"; // 导入SearchInput组件
import { ref } from "vue";

const theme = ref("light");

function changeTheme() {
  theme.value = theme.value === "light" ? "dark" : "light";
}
</script>

<script>
export default {
  data() {
    return {
      drawer: false,
    };
  },
};
</script>
