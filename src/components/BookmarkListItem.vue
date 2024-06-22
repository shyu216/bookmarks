<template>

    <div class="item">
        <div class="title">
            <img :src="bookmark.icon" alt="icon" class="icon" />
            <div class="content">
                <h3>{{ bookmark.title }}</h3>
                <p>{{ bookmark.description }}</p>
            </div>
        </div>
        <div class="row">
            <p>Added on: {{ new Date(parseInt(bookmark.add_date) * 1000).toLocaleDateString() }}
            </p>
            <a :href="bookmark.href" target="_blank" class="badge link">
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
    color: #17672c;
}

.link svg {
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
    background-color: #4DB330;
    /* Deep green */
    padding: 10px;
    margin: 10px 0;
    display: flex;
    flex-direction: column;
    font-size: 20px;
}

.icon {
    width: 60px;
    min-width: 60px;
    /* Adjusted size */
    height: auto;
    /* Maintain aspect ratio */
}

.title {
    display: flex;
    align-items: center;
}

.row {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    justify-content: space-between;
    /* Add some space between rows */
}

.content {
    margin-left: 10px;
    /* Space between icon and text */
}

.content p{
    font-size: 16px;
    margin-top: 0; /* 移除p的上边距 */
}

.content h3 {
  margin-bottom: 0; /* 移除h3的下边距 */
}

.tags {
    display: none;
    justify-content: flex-start;
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
    background-color: #FFA21F;
    padding: 3px 8px;
    border-radius: 8px;
}
</style>