<template>
  <v-layout class="rounded rounded-md">
    <Header />
    <v-main>
      <WordCloud />
      <Bookmark />
    </v-main>
  </v-layout>
</template>

<script setup>
import Header from "@/components/Header.vue";
import WordCloud from "@/components/WordCloud.vue";
import Bookmark from "@/components/Bookmark.vue";
</script>
