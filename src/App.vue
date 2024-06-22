<script setup>
import BookmarkList from "./components/BookmarkList.vue"
import WordCloud from "./components/WordCloud.vue"
</script>

<template>
  <div class="container">
    <WordCloud />
    <BookmarkList />
  </div>
</template>

<style scoped>
.container {
  justify-content: space-between;
  display: flex;
}
</style>