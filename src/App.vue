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
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: top;
}

/* 当容器宽度不足以容纳 WordCloud 的最小宽度加上 BookmarkList 的宽度时，改为列排列 */
@media (max-width: 1080px) {
  .container {
    flex-direction: column;
  }
}
</style>