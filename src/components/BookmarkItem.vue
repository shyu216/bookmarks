<template>
    <container v-if="show" class="list-item">
        <container class="title">
            <img :src="bookmark.icon" alt="icon" class="icon" />
            <container class="content">
                <h3>{{ bookmark.title }}</h3>
                <p>{{ bookmark.description }}</p>
            </container>
        </container>
        <container class="date-link">
            <p>Added on: {{ new Date(parseInt(bookmark.add_date) * 1000).toLocaleDateString() }}
            </p>
            <a :href="bookmark.href" target="_blank" class="badge link">
                <font-awesome-icon :icon="['fas', 'link']" />
                Visit Link
            </a>
        </container>
        <container class="tags">
            <span v-for="tag in bookmark.tags" :key="tag" class="badge tag" @click="updateQuery(tag)">
                {{ tag }}
            </span>
        </container>
    </container>
</template>

<script>
export default {
    props: ['bookmark', 'show'],
    methods: {
        updateQuery(searchQuery) {
            // 使用事件总线传递搜索查询
            this.$store.commit('updateSearchQuery', searchQuery);
            console.log('Committing query:', searchQuery);
        }
    }
}
</script>
