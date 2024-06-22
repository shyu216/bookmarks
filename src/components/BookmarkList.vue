<template>
    <div class="list">
        <transition-group name="fade" tag="ul" v-if="filteredBookmarks.length">
            <search-input @update:query="searchQuery = $event" />
            <bookmark-list-item v-for="(bookmark, index) in filteredBookmarks" :key="bookmark.href" :bookmark="bookmark" :style="{ 'animation-delay': index * 0.2 + 's' }" />
        </transition-group>
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
        fetch('bookmark.json', {
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


.list {    
    width: 40%; /* 设置宽度为页面宽度的40% */
}

@media (max-width: 768px) { /* 假设在屏幕宽度小于768px时调整为全宽 */
    .list {
        width: 100%; /* 在小屏幕上宽度调整为100% */
    }
}


.fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s ease;
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
    opacity: 0;
}
.bookmark-list-item {
    animation: fadeIn 0.5s ease forwards;
}
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>