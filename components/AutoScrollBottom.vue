<script setup>
import { onMounted } from 'vue'

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

onMounted(() => {
  setTimeout(() => {
    const el = document.getElementById(props.target)
    if (el) el.scrollTop = el.scrollHeight 
  }, props.delay)
})
</script>

<template>
  <div style="display: none;"></div>
</template>
