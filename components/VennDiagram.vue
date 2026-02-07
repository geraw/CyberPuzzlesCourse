<template>
  <div class="venn-container flex justify-center items-center mt-8">
    <div ref="vennRef"></div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from "vue"
import * as d3 from "d3"
import * as venn from "venn.js/build/venn.js"

interface Props {
  topText?: string[]
  leftText?: string[]
  rightText?: string[]
  annotationText?: string
  annotationX?: number
  annotationY?: number
  annotationRotate?: number
  arrowPath?: string
}

const props = withDefaults(defineProps<Props>(), {
  topText: () => ['שפות לתיאור', 'מערכות', '(תגובתיות)'],
  leftText: () => ['אלגוריתמים', 'לאימות'],
  rightText: () => ['שפות לתיאור', 'דרישות', '(תכונות של', 'מערכות)'],
  annotationText: 'נתחיל כאן',
  annotationX: 100,
  annotationY: 80,
  annotationRotate: -15,
  arrowPath: 'M110,90 Q150,120 200,140'
})

const vennRef = ref(null)

const drawDiagram = () => {
  if (!vennRef.value) return;
  
  // Clear previous diagram
  d3.select(vennRef.value).selectAll("*").remove();

  const sets = [
    { sets: ["A"], label: props.topText.join("\n"), size: 12 }, // Top
    { sets: ["B"], label: props.rightText.join("\n"), size: 12 }, // Right
    { sets: ["C"], label: props.leftText.join("\n"), size: 12 }, // Left
    { sets: ["A","B"], size: 4 },
    { sets: ["A","C"], size: 4 },
    { sets: ["B","C"], size: 4 },
    { sets: ["A","B","C"], size: 2 }
  ]

  const chart = venn.VennDiagram()
    .width(600)
    .height(450);
  
  const div = d3.select(vennRef.value);
  div.datum(sets).call(chart);

  // Styling circles
  div.selectAll("path")
    .style("stroke-opacity", 1)  // Make stroke visible
    .style("stroke", "#fff")
    .style("stroke-width", 3)
    .style("fill-opacity", 0.9)
    .style("fill", "#E09F7D");

  // Styling text
  div.selectAll("text")
    .style("fill", "#5D4037")
    .style("font-family", "Arial, sans-serif")
    .style("font-weight", "bold")
    .style("font-size", "14px"); // Initial size, D3-venn might scale it
  
  // Fix multiline text manually since d3-venn doesn't support it out of the box
  div.selectAll("text").each(function(d) {
    if (!d.label) return; // Skip if no label
    const el = d3.select(this);
    const lines = d.label.split("\n");
    if (lines.length > 1) {
      el.text("");
      const x = el.attr("x");
      const y = parseFloat(el.attr("y"));
      const fontSize = 16; // Adjust as needed
      
      lines.forEach((line, i) => {
        el.append("tspan")
          .attr("x", x)
          .attr("y", y + (i - (lines.length-1)/2) * fontSize * 1.2) // Center appropriately
          .attr("text-anchor", "middle")
          .text(line);
      });
    }
  });

  // Add "Start Here" Annotation manually (since it's not part of standard Venn)
  const svg = div.select("svg");
  
  // Define Arrowhead
  svg.append("defs").append("marker")
    .attr("id", "arrowhead")
    .attr("markerWidth", 10)
    .attr("markerHeight", 7)
    .attr("refX", 0)
    .attr("refY", 3.5)
    .attr("orient", "auto")
    .append("polygon")
    .attr("points", "0 0, 10 3.5, 0 7")
    .attr("fill", "#5D4037");

  // Add Annotation Text
  svg.append("text")
    .attr("x", props.annotationX)
    .attr("y", props.annotationY)
    .attr("fill", "#D94921")
    .attr("font-family", "'Kaushan Script', cursive")
    .attr("font-size", "32")
    .attr("transform", `rotate(${props.annotationRotate} ${props.annotationX} ${props.annotationY})`)
    .text(props.annotationText);

  // Add Arrow Path
  svg.append("path")
    .attr("d", props.arrowPath)
    .attr("stroke", "#5D4037")
    .attr("stroke-width", 4)
    .attr("fill", "none")
    .attr("marker-end", "url(#arrowhead)");
}

onMounted(() => {
  drawDiagram();
});

watch(() => props, drawDiagram, { deep: true });
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Kaushan+Script&display=swap');

.venn-container svg {
  overflow: visible;
}
</style>
