<template>
    <div class="wordcloud">
        <svg width="1000" height="1000"></svg>
    </div>
</template>


<script>
import * as d3 from 'd3';
import cloud from 'd3-cloud';

export default {
    data() {
        return {
            tags: []
        };
    },
    mounted() {
        fetch('./bookmark.json')
            .then(response => response.json())
            .then(data => {
                data.forEach(bookmark => {
                    this.tags.push(...bookmark.tags);
                });
                this.generateWordCloud();
            })
            .catch(error => console.error('Error loading bookmarks:', error));
    },
    methods: {
        generateWordCloud() {
            const tagCounts = this.tags.reduce((acc, tag) => {
                acc[tag] = (acc[tag] || 0) + 1;
                return acc;
            }, {});

            const wordCloudData = Object.keys(tagCounts).map(key => ({
                text: key,
                size: tagCounts[key] * 10 // 调整大小因子以适应你的需求
            }));

            const layout = cloud()
                .size([1000, 1000])
                .words(wordCloudData)
                .padding(5)
                .rotate(() => ~~(Math.random() * 2) * 90)
                .font("Impact")
                .fontSize(d => d.size)
                .on("end", this.drawWordCloud);

            layout.start();
        },
        drawWordCloud(words) {
            const svg = d3.select("svg");
            const width = +svg.attr("width");
            const height = +svg.attr("height");

            const color = d3.scaleOrdinal(["#1A402E", "#4C9DA0", "#89CF99", "#4D8C51", "#BCDC5C", "#38734D", "#8c9ed5", "#6c7cbb", "#362c34", "#766b7b"]);
            const word = svg.append("g")
                .attr("transform", `translate(${width / 2},${height / 2})`)
                .selectAll("text")
                .data(words)
                .enter().append("text")
                .style("font-size", d => d.size + "px")
                .style("font-family", "Impact")
                .style("fill", (d, i) => color(i)) // 使用颜色集
                .attr("text-anchor", "middle")
                .attr("transform", d => `translate(${d.x},${d.y})rotate(${d.rotate})`)
                .text(d => d.text);
        }
    }
}
</script>

<style>
.wordcloud {
    text-align: center;
    max-width: 50%;
    overflow: hidden;
}
</style>