<template>
    <svg id="bookmark-svg" width="600" height="800"></svg>
</template>

<script>
import * as d3 from "d3";
import cloud from "d3-cloud";

export default {
  data() {
    return {
      tags: [],
    };
  },
  mounted() {
    fetch("./bookmark.json")
      .then((response) => response.json())
      .then((data) => {
        data.forEach((bookmark) => {
          this.tags.push(...bookmark.tags);
        });
        this.generateWordCloud();
      })
      .catch((error) => console.error("Error loading bookmarks:", error));
  },
  methods: {
    updateQuery(searchQuery) {
      // 使用事件总线传递搜索查询
      this.$store.commit("updateSearchQuery", searchQuery);
      console.log("Committing query:", searchQuery);
    },
    generateWordCloud() {
      const tagCounts = this.tags.reduce((acc, tag) => {
        acc[tag] = (acc[tag] || 0) + 1;
        return acc;
      }, {});

      const wordCloudData = Object.keys(tagCounts).map((key) => ({
        text: key,
        count: tagCounts[key],
        size: Math.max(Math.log(tagCounts[key]) * 20, 10), // 使用对数调整大小，并确保最小值为10
      }));

      const svg = d3.select("#bookmark-svg");
      const width = +svg.attr("width");
      const height = +svg.attr("height");

      const layout = cloud()
        .size([width, height])
        .words(wordCloudData)
        .padding(1)
        // .rotate(() => ~~(Math.random() * 2) * 90)
        .rotate(() => Math.random() * 60)
        .font("Impact")
        .fontSize((d) => d.size)
        .on("end", this.drawWordCloud);

      layout.start();
    },
    drawWordCloud(words) {
      const svg = d3.select("#bookmark-svg");
      const width = +svg.attr("width");
      const height = +svg.attr("height");

      const color = d3.scaleOrdinal([
        "#1A402E",
        "#4C9DA0",
        "#89CF99",
        "#4D8C51",
        "#BCDC5C",
        "#38734D",
        "#8c9ed5",
        "#6c7cbb",
        "#362c34",
        "#766b7b",
      ]);
      const word = svg
        .append("g")
        .attr("transform", `translate(${width / 2},${height / 2})`)
        .selectAll("text")
        .data(words)
        .enter()
        .append("text")
        .style("font-size", (d) => d.size + "px")
        .style("font-family", "Impact")
        .style("fill", (d, i) => color(i))
        .attr("text-anchor", "middle")
        .text((d) => d.text)
        .on("click", (event, d) => this.updateQuery(d.text)) // 添加点击事件监听器
        .on("mouseover", function (event, d) {
          // 创建一个 tooltip 元素
          d3.select(this).append("title").text(`Count: ${d.count}`);
        })
        .on("mouseout", function (event, d) {
          // 移除 tooltip 元素
          d3.select(this).select("title").remove();
        })
        .style("cursor", "pointer") // 将鼠标光标改为指针形状，以提高用户体验
        .transition() // 应用动画
        .duration(3000) // 动画持续时间，单位为毫秒
        .attr(
          "transform",
          (d) => `translate(${d.x},${d.y}) rotate(${d.rotate})`
        ); // 确保单词的位置和旋转也被应用
    },
  },
};
</script>
