<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref } from 'vue'
import * as THREE from 'three'

const el = ref<HTMLElement | null>(null)

let renderer: THREE.WebGLRenderer | null = null
let scene: THREE.Scene | null = null
let camera: THREE.PerspectiveCamera | null = null
let root: THREE.Group | null = null
let raf = 0

// אינטראקציה בסיסית (Orbit-ish בלי תלות חיצונית)
let isDown = false
let lastX = 0
let lastY = 0
let theta = 0.8
let phi = 0.9
let radius = 4.2

function clamp(v: number, lo: number, hi: number) {
  return Math.max(lo, Math.min(hi, v))
}

function buildCube2x2() {
  const g = new THREE.Group()

  const cubeSize = 0.95
  const gap = 0.05
  const offset = (cubeSize + gap) / 2

  const colors = {
    U: 0xffffff,
    D: 0xffff00,
    F: 0x00aa00,
    B: 0x0044aa,
    R: 0xaa0000,
    L: 0xff8800,
    body: 0x111111,
  }

  // חומרי פנים (לכל “קובייה קטנה”)
  const mats = [
    new THREE.MeshLambertMaterial({ color: colors.R }),   // +X
    new THREE.MeshLambertMaterial({ color: colors.L }),   // -X
    new THREE.MeshLambertMaterial({ color: colors.U }),   // +Y
    new THREE.MeshLambertMaterial({ color: colors.D }),   // -Y
    new THREE.MeshLambertMaterial({ color: colors.F }),   // +Z
    new THREE.MeshLambertMaterial({ color: colors.B }),   // -Z
  ]

  const geom = new THREE.BoxGeometry(cubeSize, cubeSize, cubeSize)

  // 8 קוביות קטנות במבנה 2×2×2
  const coords = [-offset, offset]
  for (const x of coords) for (const y of coords) for (const z of coords) {
    const m = new THREE.Mesh(geom, mats)
    m.position.set(x, y, z)
    g.add(m)

    // קווי מתאר עדינים
    const edges = new THREE.EdgesGeometry(geom)
    const line = new THREE.LineSegments(
      edges,
      new THREE.LineBasicMaterial({ color: colors.body, transparent: true, opacity: 0.65 })
    )
    line.position.copy(m.position)
    g.add(line)
  }

  // מסגרת/בסיס קל
  const frame = new THREE.Mesh(
    new THREE.BoxGeometry(2.15, 2.15, 2.15),
    new THREE.MeshBasicMaterial({ color: 0x000000, wireframe: true, transparent: true, opacity: 0.08 })
  )
  g.add(frame)

  return g
}

function resize() {
  if (!el.value || !renderer || !camera) return
  const w = el.value.clientWidth
  const h = el.value.clientHeight
  renderer.setSize(w, h, false)
  camera.aspect = w / h
  camera.updateProjectionMatrix()
}

function updateCamera() {
  if (!camera) return
  const x = radius * Math.sin(phi) * Math.cos(theta)
  const y = radius * Math.cos(phi)
  const z = radius * Math.sin(phi) * Math.sin(theta)
  camera.position.set(x, y, z)
  camera.lookAt(0, 0, 0)
}

function animate() {
  raf = requestAnimationFrame(animate)
  if (root) {
    root.rotation.y += 0.006 // סיבוב קל “חי”
  }
  updateCamera()
  renderer?.render(scene!, camera!)
}

function onPointerDown(e: PointerEvent) {
  isDown = true
  lastX = e.clientX
  lastY = e.clientY
}
function onPointerMove(e: PointerEvent) {
  if (!isDown) return
  const dx = e.clientX - lastX
  const dy = e.clientY - lastY
  lastX = e.clientX
  lastY = e.clientY
  theta -= dx * 0.008
  phi = clamp(phi + dy * 0.008, 0.2, Math.PI - 0.2)
}
function onPointerUp() {
  isDown = false
}
function onWheel(e: WheelEvent) {
  radius = clamp(radius + e.deltaY * 0.0025, 2.8, 7.5)
}

onMounted(() => {
  if (!el.value) return

  scene = new THREE.Scene()
  scene.background = new THREE.Color(0x000000)
  scene.background = null as any // שקוף (נחמד על רקע Slidev)

  camera = new THREE.PerspectiveCamera(45, 1, 0.1, 100)
  updateCamera()

  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true })
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2))

  el.value.appendChild(renderer.domElement)

  // תאורה
  const amb = new THREE.AmbientLight(0xffffff, 0.75)
  scene.add(amb)
  const dir = new THREE.DirectionalLight(0xffffff, 0.8)
  dir.position.set(3, 5, 4)
  scene.add(dir)

  root = buildCube2x2()
  scene.add(root)

  // events
  el.value.addEventListener('pointerdown', onPointerDown)
  window.addEventListener('pointermove', onPointerMove)
  window.addEventListener('pointerup', onPointerUp)
  el.value.addEventListener('wheel', onWheel, { passive: true })
  window.addEventListener('resize', resize)

  resize()
  animate()
})

onBeforeUnmount(() => {
  cancelAnimationFrame(raf)
  window.removeEventListener('resize', resize)
  window.removeEventListener('pointermove', onPointerMove)
  window.removeEventListener('pointerup', onPointerUp)
  if (el.value) {
    el.value.removeEventListener('pointerdown', onPointerDown)
    el.value.removeEventListener('wheel', onWheel as any)
  }
  if (renderer?.domElement && el.value?.contains(renderer.domElement)) {
    el.value.removeChild(renderer.domElement)
  }
  renderer?.dispose()
  renderer = null
  scene = null
  camera = null
  root = null
})
</script>

<template>
  <div ref="el" class="w-full h-full rounded-2xl overflow-hidden"
       style="border:1px solid rgba(255,255,255,0.10); background: rgba(255,255,255,0.02);" />
</template>
