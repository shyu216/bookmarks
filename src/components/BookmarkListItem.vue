<template>

    <div class="item">
        <div class="row">
            <img :src="bookmark.icon" alt="icon" class="icon" />
            <div class="content">
                <h3>{{ bookmark.title }}</h3>
                <p>{{ bookmark.description }}</p>
            </div>
        </div>
        <div class="row">
            <p class="add-date">Added on: {{ new Date(parseInt(bookmark.add_date) * 1000).toLocaleDateString() }}
            </p>
            <a :href="bookmark.href" target="_blank" class="badge link-badge">
                <font-awesome-icon :icon="['fas', 'link']" />
                Visit Link
            </a>
        </div>
        <div class="row tags">
            <span v-for="tag in bookmark.tags" :key="tag" class="badge tag">
                {{ tag }}
            </span>
        </div>
    </div>
</template>

<script>
export default {
    props: ['bookmark']
}
</script>

<style scoped>
h3 {
  font-weight: bold;
}

.badge {
    display: inline-flex;
    align-items: center;
    padding: 3px 8px;
    border-radius: 8px;
}

.link-badge svg {
    margin-right: 5px;
    transition: transform 0.3s ease;
}

.badge:hover svg {
    transform: scale(1.2);
}

.item { 
    transition: width 0.3s ease; /* 可选：平滑过渡效果 */
    /* 其他样式 */
    border-radius: 10px;
    background-color: #004d40;
    /* Deep green */
    padding: 10px;
    margin: 10px 0;
    display: flex;
    flex-direction: column;
}

.icon {
    width: 40px;
    min-width: 40px;
    /* Adjusted size */
    height: auto;
    /* Maintain aspect ratio */
}

.row {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    /* Add some space between rows */
}

.content {
    margin-left: 10px;
    /* Space between icon and text */
}

.add-date {
    width: 200px;
    /* Fixed width for date */
    margin-right: auto;
    /* Pushes the link to the right */
}

.tags {
    display: none;
}
.item:hover .tags {
    display: flex;
    flex-wrap: wrap;
    /* Wrap tags */
}

.tag {
    margin-right: 5px;
    /* Adjusted tag spacing */
    margin-bottom: 5px;
    /* Space between tag rows */
    background-color: #2b60c2;
    padding: 3px 8px;
    border-radius: 8px;
}
</style>