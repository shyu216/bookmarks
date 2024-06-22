<template>
    <div class="search-container">
        <font-awesome-icon :icon="['fas', 'search']" class="search-icon"/>
        <input type="text" v-model="searchQuery" placeholder="Search bookmarks..." @input="updateQuery" class="search-input" />
    </div>
</template>

<script>
export default {
    data() {
        return {
            searchQuery: ''
        };
    },
    methods: {
        updateQuery() {
            this.$emit('update:query', this.searchQuery);
        }
    }
}
</script>

<style scoped>
.search-container {
    display: flex;
    align-items: center;
    justify-content: right;
    border-radius: 8px;
}

.search-input {    
    transition: all 0.3s ease; /* 平滑过渡效果 */ 
    font-size: 24px; /* 设置字体大小 */
    padding: 10px 20px; /* 调整内边距以适应字体大小 */
    height: auto; /* 自动调整高度以适应内容 */
    border-radius: 8px;
    border-color: #4DB330;
    color: #17672c;
}

.search-icon {
    color: #17672c;
    font-size: 32px;
    margin-right: 20px;
}
</style>