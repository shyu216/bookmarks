<template>
    <div class="tutorial-card-container">
        <font-awesome-icon :icon="['fas', 'circle-question']" @click="toggleCardVisibility" class="tutorial-icon" />
        <div v-if="isCardVisible" class="tutorial-card">
            <h3>📚 游历Dale的藏书阁 🌍</h3>
            <p>🚪 此间，收藏着Dale遍访诸网之珍稀，每一处皆是意外之喜！🎁</p>
            <p>🔍 徜徉于词云之海，觅🔑关键词之踪。每一语，皆开新世界之门！</p>
            <p>🏷️ 探书签之标签，如寻珍宝之匣，待君一一揭晓。</p>
            <p>💡 任意所思所忆，或一念，或一记，此间应有回响。</p>
            <p>🌈 愿君于此小小网页，发现乐趣，带来欢愉！🌟</p>
            <div class="close-div">
                <font-awesome-icon :icon="['fas', 'x']" @click="toggleCardVisibility" class="close-icon" />
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            isCardVisible: false,
        };
    },
    methods: {
        toggleCardVisibility() {
            this.isCardVisible = !this.isCardVisible;
        },
    },
};
</script>

<style>
.tutorial-card {
    /* 卡片样式 */
    position: absolute;
    background-color: white;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    padding: 20px;
    border-radius: 8px;
    width: 300px;
    top: 50px;
    /* 根据需要调整 */
    left: 50%;
    /* 根据需要调整 */
    transform: translateX(-50%);
}

.tutorial-icon {
    color: #17672c;
    font-size: 28px;
}

.close-div {
    width: 100%;
    display: flex;
    justify-content: center;
}

.close-icon {
    color: #17672c;
    font-size: 22px;
}
</style>