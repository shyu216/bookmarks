<template>
  <v-row class="my-2 mx-4">
    <template v-for="(bookmark, index) in bookmarks">
      <v-col
        :key="bookmark.href"
        v-if="shouldShowBookmark(bookmark)"
        cols="6"
        md="4"
        lg="3"
      >
        <v-lazy :options="{ threshold: 0.5 }" transition="fade-transition">
          <BookmarkItem :bookmark="bookmark" />
        </v-lazy>
      </v-col>
    </template>
    <template v-if="bookmarks.length === 0">
      <v-container fill-height>
        <v-row align="center" justify="center">
          <v-col cols="auto">
            <v-progress-circular
              :size="70"
              :width="7"
              color="purple"
              indeterminate
            ></v-progress-circular>
          </v-col>
        </v-row>
      </v-container>
    </template>
  </v-row>
</template>

<script>
import BookmarkItem from "./BookmarkItem.vue";

import { mapState } from "vuex";

export default {
  components: {
    BookmarkItem,
  },
  data() {
    return {
      bookmarks: [],
      keyword: "",
    };
  },
  computed: {
    ...mapState({
      searchQuery: (state) => state.searchQuery, // 从 Vuex store 映射 searchQuery 状态
    }),
  },
  watch: {
    // 监听 searchQuery 的变化
    searchQuery(newVal, oldVal) {
      console.log(`searchQuery 更新了，新值: ${newVal}, 旧值: ${oldVal}`);
      this.keyword = newVal;
    },
  },
  mounted() {
    const start_time = performance.now();
    fetch("./sites.json", {
      headers: {
        "Content-Type": "application/json; charset=utf-8",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        this.bookmarks = data;
        const end_time = performance.now();
        console.log(
          "Bookmarks loaded:",
          this.bookmarks.length,
          ", in",
          (end_time - start_time) / 1000,
          "s"
        );
      })
      .catch((error) => console.error("Error loading bookmarks:", error));
  },
  methods: {
    shouldShowBookmark(bookmark) {
      // 如果 keyword 为空，返回 true 显示所有书签
      if (!this.keyword.trim()) {
        return true;
      }
      // 使用 includes 方法检查书签的标题中是否包含关键词
      return (
        bookmark.title.toLowerCase().includes(this.keyword.toLowerCase()) ||
        this.keyword.toLowerCase() in bookmark.tags ||
        bookmark.description?.toLowerCase().includes(this.keyword.toLowerCase())
      );
    },
  },
};
</script>
