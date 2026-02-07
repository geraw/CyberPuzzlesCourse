<template>
  <div class="transition-system-container flex justify-center items-center mt-8"
       @mousedown.stop @touchstart.stop @pointerdown.stop>
    <svg ref="svgRef" :width="width" :height="height" class="overflow-visible">
      <defs>
        <marker id="arrowhead-ts-d3" markerWidth="10" markerHeight="7" 
          refX="9" refY="3.5" orient="auto">
          <polygon points="0 0, 10 3.5, 0 7" fill="#333" />
        </marker>
      </defs>
      <g ref="zoomLayer">
        <g class="links"></g>
        <g class="nodes"></g>
      </g>
    </svg>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue';
import * as d3 from 'd3';
import katex from 'katex';
import 'katex/dist/katex.min.css';

// Interfaces
interface State {
  id: string;
  x?: number;
  y?: number;
  label?: string; // Atomic Propositions (below right)
  name?: string;  // Inside the rectangle
  initial?: boolean;
}

interface Transition {
  source: string;
  target: string;
  action?: string;
  loopDirection?: string; // e.g., '0deg', '90deg'
  loopSweep?: string;     // Not fully used in simple D3 bezier logic but kept for compat
}

interface Props {
  states: State[];
  transitions: Transition[];
  width?: number;
  height?: number;
  auto?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  width: 600,
  height: 400,
  auto: true
});

const svgRef = ref<SVGSVGElement | null>(null);
const zoomLayer = ref<SVGGElement | null>(null);

let simulation: d3.Simulation<d3.SimulationNodeDatum, undefined> | null = null;

// Helper to render KaTeX with delimiters $...$
// Passes content directly to KaTeX like the rest of Slidev
const renderMath = (str: string): string => {
    if (!str) return '';
    
    // Split by $ delimiter and render math parts
    const parts = str.split('$');
    if (parts.length < 3) return str;

    return parts.map((part, index) => {
        if (index % 2 === 1) {
            // Math part - pass directly to KaTeX
            try {
                return katex.renderToString(part, { throwOnError: false });
            } catch (e) {
                return part;
            }
        }
        return part;
    }).join('');
};

const render = () => {
    if (!svgRef.value || !zoomLayer.value) return;

    if (simulation) {
       simulation.stop();
       simulation = null;
    }

    const svg = d3.select(svgRef.value);
    const layer = d3.select(zoomLayer.value);
    
    // Clear existing
    layer.select(".links").selectAll("*").remove();
    layer.select(".nodes").selectAll("*").remove();

    const rectW = 60;
    const rectH = 40;

    // Prepare data
    const nodes = props.states.map(s => ({ 
        ...s, 
        x: s.x ?? undefined, 
        y: s.y ?? undefined,
        fx: s.x, 
        fy: s.y
    }));
    
    // Initial positions
    nodes.forEach(n => {
        if (n.x === undefined) n.x = props.width/2 + (Math.random()-0.5)*50;
        if (n.y === undefined) n.y = props.height/2 + (Math.random()-0.5)*50;
    });

    const links = props.transitions.map(t => ({ ...t }));

    // Helper: Rectangle Intersection
    function getRectIntersection(dx: number, dy: number, w: number, h: number) {
       if (dx === 0 && dy === 0) return { x: 0, y: 0 };
       const tX = (w / 2) / Math.abs(dx);
       const tY = (h / 2) / Math.abs(dy);
       const t = Math.min(tX, tY);
       return { x: dx * t, y: dy * t };
    }
    
    // Helper: Self Loop Path
    function getSelfLoopPath(x: number, y: number, dirStr: string = '-45deg') {
       let angle = -Math.PI * 3 / 4; 
       const degMatch = dirStr.match(/(-?[\d.]+)deg/);
       if (degMatch) {
           angle = parseFloat(degMatch[1]) * Math.PI / 180;
       } else if (!isNaN(parseFloat(dirStr))) {
           angle = parseFloat(dirStr) * Math.PI / 180;
       }
       
       const loopWid = 30;
       const spread = Math.PI / 8; 
       const a1 = angle - spread;
       const a2 = angle + spread;
       
       const p1 = getRectIntersection(Math.cos(a1), Math.sin(a1), rectW, rectH);
       const x1 = x + p1.x;
       const y1 = y + p1.y;
       
       const p2 = getRectIntersection(Math.cos(a2), Math.sin(a2), rectW, rectH);
       const x2 = x + p2.x;
       const y2 = y + p2.y;
       
       const cpDist = 60;
       const cx1 = x + Math.cos(a1) * cpDist;
       const cy1 = y + Math.sin(a1) * cpDist;
       const cx2 = x + Math.cos(a2) * cpDist;
       const cy2 = y + Math.sin(a2) * cpDist;
 
       return `M ${x1},${y1} C ${cx1},${cy1} ${cx2},${cy2} ${x2},${y2}`;
    }

    // Determine layout strategy
    const hasMissingCoords = props.states.some(s => s.x === undefined || s.y === undefined);
    const shouldSimulate = props.auto || hasMissingCoords;

    // Drag handlers (defined before use)
    function dragstarted(event: any, d: any) {
        console.log("Drag started", d);
        if (!event.active && simulation) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }
    function dragged(event: any, d: any) {
        console.log("Dragging", event.x, event.y);
        d.fx = event.x;
        d.fy = event.y;
        d.x = event.x;
        d.y = event.y;
    }
    function dragended(event: any, d: any) {
        console.log("Drag ended");
        if (!event.active && simulation) simulation.alphaTarget(0);
    }

    // Drag behavior
    const dragBehavior = d3.drag<SVGGElement, any>()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);

    // Draw Links
    const linkGroup = layer.select(".links");
    const linkSelection = linkGroup.selectAll("g")
        .data(links)
        .enter()
        .append("g")
        .attr("class", "link-group");

    const paths = linkSelection.append("path")
        .attr("stroke", "#333")
        .attr("stroke-width", 2)
        .attr("fill", "none")
        .attr("marker-end", "url(#arrowhead-ts-d3)");

    // Link Labels (foreignObject) - keep reference to foreignObject for positioning
    const linkLabelFOs = linkSelection.append("foreignObject")
        .attr("width", 40)
        .attr("height", 30)
        .style("overflow", "visible");
    
    // Inner div for styling and KaTeX content
    linkLabelFOs.append("xhtml:div")
        .style("display", "flex")
        .style("justify-content", "center")
        .style("align-items", "center")
        .style("width", "100%")
        .style("height", "100%")
        .style("font-size", "14px")
        .style("background-color", "white")
        .html((d: any) => d.action ? renderMath(d.action) : "");

    // Draw Nodes
    const nodeGroup = layer.select(".nodes");
    const nodeSelection = nodeGroup.selectAll("g")
        .data(nodes)
        .enter()
        .append("g")
        .attr("class", "node-group")
        .call(dragBehavior);
    
    console.log("Nodes created with drag:", nodeSelection.size());

    // Node Rectangle
    nodeSelection.append("rect")
        .attr("width", rectW)
        .attr("height", rectH)
        .attr("x", -rectW / 2)
        .attr("y", -rectH / 2)
        .attr("rx", 5)
        .attr("ry", 5)
        .attr("fill", "#FFF59D")
        .attr("stroke", "#000")
        .attr("stroke-width", 2)
        .style("cursor", "grab")
        .on("mousedown", (event: any) => {
            console.log("Rect mousedown");
            event.stopPropagation();
            event.stopImmediatePropagation();
        })
        .on("pointerdown", (event: any) => {
            console.log("Rect pointerdown");
            event.stopPropagation();
            event.stopImmediatePropagation();
        });

    // Initial state arrow
    nodeSelection.filter(d => d.initial).append("path")
        .attr("d", `M -50,0 L -${rectW/2 + 5},0`) 
        .attr("stroke", "#000")
        .attr("stroke-width", 2)
        .attr("marker-end", "url(#arrowhead-ts-d3)");

    // State Name (foreignObject)
    nodeSelection.append("foreignObject")
        .attr("width", rectW)
        .attr("height", rectH)
        .attr("x", -rectW / 2)
        .attr("y", -rectH / 2)
        .style("pointer-events", "none")
        .append("xhtml:div")
        .style("display", "flex")
        .style("justify-content", "center")
        .style("align-items", "center")
        .style("width", "100%")
        .style("height", "100%")
        .style("font-weight", "bold")
        .style("pointer-events", "none")
        .html((d: any) => renderMath(d.text || d.name || d.id));

    // Label (Propositions - Below Right)
    nodeSelection.append("foreignObject")
        .attr("width", 60)
        .attr("height", 30)
        .attr("x", 20 - 30) // Centered on (20, 35)
        .attr("y", 35 - 15)
        .style("pointer-events", "none")
        .append("xhtml:div")
        .style("display", "flex")
        .style("justify-content", "center")
        .style("align-items", "center")
        .style("width", "100%")
        .style("height", "100%")
        .style("font-size", "12px")
        .style("color", "#555")
        .html((d: any) => d.label ? renderMath(d.label) : "");

    // Tick function
    const tick = () => {
        // Debugging
        // console.log("Tick running. Nodes count:", nodes.length, "Links count:", links.length);

        paths.attr("d", d => {
            let source: any = d.source;
            let target: any = d.target;
            
            if (typeof source !== 'object') source = nodes.find(n => n.id === source);
            if (typeof target !== 'object') target = nodes.find(n => n.id === target);
            if (!source || !target) return "";

            if (source.id === target.id) {
               return getSelfLoopPath(source.x!, source.y!, d.loopDirection || '-45deg');
            }

            const dx = target.x! - source.x!;
            const dy = target.y! - source.y!;
            const sourceInt = getRectIntersection(dx, dy, rectW, rectH);
            const targetInt = getRectIntersection(-dx, -dy, rectW, rectH);
            return `M ${source.x! + sourceInt.x},${source.y! + sourceInt.y} L ${target.x! + targetInt.x},${target.y! + targetInt.y}`;
        });

        linkLabelFOs
            .attr("x", (d, i) => {
                 let s: any = d.source;
                 let t: any = d.target;
                 if (typeof s !== 'object') s = nodes.find(n => n.id === s);
                 if (typeof t !== 'object') t = nodes.find(n => n.id === t);
                 
                 if (!s || !t) {
                     console.warn("Link label: source or target missing", d);
                     return 0; // Top Left?
                 }
                 
                 if (s.x === undefined || t.x === undefined) {
                     // console.warn("Link label: coordinates missing", s, t);
                     return 0;
                 }

                 const w = 40;
                 if (s.id === t.id) {
                     const dirStr = d.loopDirection || '-45deg';
                     let angle = -Math.PI * 3 / 4;
                     const degMatch = dirStr.match(/(-?[\d.]+)deg/);
                     if (degMatch) angle = parseFloat(degMatch[1]) * Math.PI / 180;
                     const dist = 70;
                     return s.x! + Math.cos(angle) * dist - w/2;
                 }
                 // Center on link
                 return (s.x! + t.x!) / 2 - w/2;
            })
            .attr("y", d => {
                 let s: any = d.source;
                 let t: any = d.target;
                 if (typeof s !== 'object') s = nodes.find(n => n.id === s);
                 if (typeof t !== 'object') t = nodes.find(n => n.id === t);
                 if (!s || !t) return 0;
                 if (s.y === undefined || t.y === undefined) return 0;

                 const h = 30;
                 if (s.id === t.id) {
                     const dirStr = d.loopDirection || '-45deg';
                     let angle = -Math.PI * 3 / 4;
                     const degMatch = dirStr.match(/(-?[\d.]+)deg/);
                     if (degMatch) angle = parseFloat(degMatch[1]) * Math.PI / 180;
                     const dist = 70;
                     return s.y! + Math.sin(angle) * dist - h/2;
                 }
                 return (s.y! + t.y!) / 2 - h/2;
            });
        
        nodeSelection.attr("transform", d => `translate(${d.x},${d.y})`);
    };

    if (shouldSimulate) {
        simulation = d3.forceSimulation(nodes)
            .force("link", d3.forceLink(links).id((d: any) => d.id).distance(150))
            .force("charge", d3.forceManyBody().strength(-500))
            .force("center", d3.forceCenter(props.width / 2, props.height / 2))
            .force("collide", d3.forceCollide(rectW).iterations(2));
        simulation.on("tick", tick);
    } else {
        tick();
    }


};

onMounted(() => {
   render();
});

watch(() => [props.states, props.transitions, props.width, props.height], () => {
   render();
}, { deep: true });
</script>

<style scoped>
/* No extra css needed */
</style>
