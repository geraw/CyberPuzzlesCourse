<script setup>
import { onMounted } from 'vue'
import { onSlideEnter } from '@slidev/client'

const props = defineProps({
  target: {
    type: String,
    required: true
  },
  delay: {
    type: Number,
    default: 1000
  }
})

const scrollDown = () => {
  setTimeout(() => {
    const el = document.getElementById(props.target)
    if (el) el.scrollTop = el.scrollHeight 
  }, props.delay)
}

onMounted(scrollDown)
onSlideEnter(scrollDown)
</script>

<template>
  <div style="display: none;"></div>
</template>
