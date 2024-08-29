<template>
  <v-lazy
    :min-height="200"
    :options="{ threshold: 0.5 }"
    transition="fade-transition"
  >
    <v-row class="my-2 mx-4">
         <template v-for="(bookmark, index) in bookmarks">
            <v-col
              :key="bookmark.href"
              v-if="shouldShowBookmark(bookmark)"
              cols="6"
              md="4"
              lg="3"
            >
              <BookmarkItem :bookmark="bookmark" />
            </v-col>
          </template>
    </v-row>
  </v-lazy>
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
    fetch("./sites.json", {
      headers: {
        "Content-Type": "application/json; charset=utf-8",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        this.bookmarks = data;
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
        bookmark.tags?.some((tag) =>
          tag.toLowerCase().includes(this.keyword.toLowerCase())
        ) ||
        bookmark.description?.toLowerCase().includes(this.keyword.toLowerCase())
      );
    },
  },
};
</script>
