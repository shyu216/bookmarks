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
  gap: 10vh;
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
  }

  .divider {
    height: 5px; /* 调整为适合水平分割线的高度 */
    width: 100%; /* 撑满容器宽度 */
    background-color: rgba(23, 103, 44, 0.5); /* 保持之前的颜色和透明度设置 */
  }
}
</style>