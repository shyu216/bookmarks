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
            <span v-for="tag in bookmark.tags" :key="tag" class="badge tag">
                {{ tag }}
            </span>
        </container>
    </container>
</template>

<script>
export default {
    props: ['bookmark', 'show']
}
</script>

<style scoped>
.list-item {
    transition: height 0.3s ease;
    border-radius: 8px;
    background-color: #4DB330;
    padding: 10px;
    margin: 10px 0;
    display: flex;
    flex-direction: column;
    font-size: 14px;
    gap: 0px;
}

.list-item:hover .tags {
    display: flex;
    flex-wrap: wrap;
}

.title {
    display: flex;  
    align-items: center;
    justify-content: left;
}

.icon {
    width: 40px;
    min-width: 40px;
    max-width: 40px;
    height: 40px;
    min-height: 40px;
    max-height: 40px;
}

.date-link {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.content {
    margin-left: 10px;
}

.content p {
    font-size: 14px;
    margin-top: 0;
}

.content h3 {
    margin-bottom: 0;
    font-weight: bold;
}

.tags {
    display: none;
    align-items: center;
    justify-content: flex-start;
}


.badge {
    display: inline-flex;
    align-items: center;
    padding: 3px 8px;
    border-radius: 8px;
    color: #17672c;
}


.badge:hover svg {
    transform: scale(1.2);
}


.link svg {
    margin-right: 5px;
    transition: transform 0.3s ease;
}


.tag {
    margin-right: 5px;
    margin-bottom: 5px;
    background-color: #FFA21F;
    padding: 3px 8px;
    border-radius: 8px;
}
</style>