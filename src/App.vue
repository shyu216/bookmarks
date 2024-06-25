<script setup>
import BookmarkList from "./components/BookmarkList.vue"
import WordCloud from "./components/WordCloud.vue"
</script>

<template>
  <div class="container">
      <WordCloud />
      <div class="divider"></div>
      <BookmarkList />
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  gap: 10vw;
  overflow: hidden;
}

.divider {
  width: 5px;
  background-color: rgba(23, 103, 44, 0.5); /* 分割线颜色，透明度设置为 0.5 */
  height: 60%; /* 或者设置为特定的高度 */
}

/* 当容器宽度不足以容纳 WordCloud 的最小宽度加上 BookmarkList 的宽度时，改为列排列 */
@media (max-width: 1080px) {
  .container {
    flex-direction: column;
    width: 100%;
    gap: 0vh;
  }

  .divider {
    display: none;
  }
}
</style>