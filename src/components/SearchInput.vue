<template>
    <div class="search-container">
        <font-awesome-icon :icon="['fas', 'search']" class="search-icon" />
        <input type="text" v-model="searchQuery" placeholder="Search bookmarks..." @input="updateQuery"
            class="search-input" />
    </div>
</template>

<script>
export default {
    data() {
        return {
            searchQuery: ''
        };
    }, mounted() {
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
            this.$store.commit('updateSearchQuery', this.searchQuery);
            console.log('Committing query:', this.searchQuery);
        }
    }
}
</script>

<style scoped>
.search-container {
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
}

.search-input {
    transition: all 0.3s ease;
    /* 平滑过渡效果 */
    font-size: 18px;
    /* 设置字体大小 */
    padding: 10px;
    /* 调整内边距以适应字体大小 */
    height: auto;
    /* 自动调整高度以适应内容 */
    border-radius: 8px;
    border-color: #4DB330;
    color: #17672c;
}

.search-icon {
    color: #17672c;
    font-size: 24px;
    margin-right: 10px;
}
</style>