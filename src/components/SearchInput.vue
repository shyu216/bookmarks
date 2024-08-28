<template>
  <v-row>
    <v-col cols="12" sm="8" md="6" lg="4" class="mx-auto">
      <v-text-field
        v-model="searchQuery"
        bg-color="purple-lighten-5"
        class="rounded elevation-3"
        prepend-inner-icon="fas fa-search"
        label="Keyword"
        hide-details="auto"
        @input="updateQuery"
      >
      </v-text-field>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: "",
    };
  },
  mounted() {
    // 监听 Vuex store 中特定状态的变化
    this.$store.watch(
      (state) => state.searchQuery, // 这是你想要监听的 Vuex store 中的状态
      (newValue) => {
        // 当状态变化时，这个回调函数会被调用
        this.searchQuery = newValue; // 更新你的 input 的值
      }
    );
  },
  methods: {
    updateQuery() {
      // 使用事件总线传递搜索查询
      this.$store.commit("updateSearchQuery", this.searchQuery);
      console.log("Committing query:", this.searchQuery);
    },
  },
};
</script>
