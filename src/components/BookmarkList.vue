<template>
    <div class="list">
        <search-input @update:query="searchQuery = $event" class="search" />
        <div v-if="filteredBookmarks.length" class="scrollable">
            <bookmark-list-item v-for="(bookmark, index) in filteredBookmarks" :key="bookmark.href"
                :bookmark="bookmark" />
        </div>
    </div>
</template>

<script>
import BookmarkListItem from './BookmarkListItem.vue';
import SearchInput from './SearchInput.vue'; // 导入SearchInput组件

export default {
    components: {
        BookmarkListItem,
        SearchInput // 注册SearchInput组件
    },
    data() {
        return {
            bookmarks: [],
            searchQuery: '' // 保持searchQuery数据属性
        };
    },
    computed: {
        filteredBookmarks() {
            // 使用搜索查询过滤书签
            return this.bookmarks.filter(bookmark => bookmark.title.toLowerCase().includes(this.searchQuery.toLowerCase()));
        }
    },
    mounted() {
        fetch('./bookmark.json', {
            headers: {
                'Content-Type': 'application/json; charset=utf-8'
            },
        })
            .then(response => response.json())
            .then(data => {
                this.bookmarks = data;
            })
            .catch(error => console.error('Error loading bookmarks:', error));
    }
}
</script>


<style>
.scrollable {
    max-height: 800px;
    overflow-y: auto;
    overflow-x: hidden;
    border-radius: 8px;
}

.search {
    padding-bottom: 10px;
}

.list {
    max-width: 40%;
}
</style>