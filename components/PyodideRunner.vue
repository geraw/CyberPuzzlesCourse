<template>
  <div class="pyodide-runner" dir="ltr">
    <div class="columns">
      <div class="col-code">
        <div class="col-header">Code</div>
        <textarea v-model="code" rows="18" spellcheck="false" />
        <div class="controls">
          <button @click="run" :disabled="running || loading">
            {{ loading ? '⏳ Loading Pyodide...' : running ? '⏳ Running...' : '▶ Run' }}
          </button>
        </div>
      </div>
      <div class="col-output">
        <div class="col-header">Output</div>
        <pre class="output" :class="{ error: !!errorText }">{{ errorText || outputText || '(click Run)' }}</pre>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

const props = defineProps<{
  src: string
}>()

const code = ref('# Loading...')
const outputText = ref('')
const errorText = ref('')
const running = ref(false)
const loading = ref(true)

let pyodide: any = null

async function loadPyodideFromCDN() {
  if ((window as any).loadPyodide) {
    return (window as any).loadPyodide
  }
  return new Promise<any>((resolve, reject) => {
    const script = document.createElement('script')
    script.src = 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js'
    script.onload = () => resolve((window as any).loadPyodide)
    script.onerror = reject
    document.head.appendChild(script)
  })
}

onMounted(async () => {
  try {
    const resp = await fetch(props.src)
    code.value = await resp.text()
  } catch (e: any) {
    code.value = `# Failed to load ${props.src}: ${e.message}`
  }

  try {
    const loadPyodide = await loadPyodideFromCDN()
    pyodide = await loadPyodide({
      indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/'
    })
    loading.value = false
  } catch (e: any) {
    errorText.value = `Failed to load Pyodide: ${e.message}`
    loading.value = false
  }
})

async function run() {
  if (!pyodide || running.value) return
  running.value = true
  outputText.value = ''
  errorText.value = ''

  try {
    pyodide.setStdout({
      write: (buf: Uint8Array) => {
        outputText.value += new TextDecoder().decode(buf)
        return buf.length
      },
      isatty: false,
    })
    pyodide.setStderr({
      write: (buf: Uint8Array) => {
        errorText.value += new TextDecoder().decode(buf)
        return buf.length
      },
      isatty: false,
    })
    await pyodide.runPythonAsync(code.value)
  } catch (e: any) {
    errorText.value += e.toString()
  } finally {
    running.value = false
  }
}
</script>

<style scoped>
.pyodide-runner {
  font-family: 'Fira Code', monospace;
  text-align: left;
  direction: ltr;
}
.columns {
  display: flex;
  gap: 12px;
}
.col-code {
  flex: 3;
  display: flex;
  flex-direction: column;
}
.col-output {
  flex: 2;
  display: flex;
  flex-direction: column;
}
.col-header {
  font-size: 11px;
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: #89b4fa;
  margin-bottom: 4px;
}
.col-code textarea {
  width: 100%;
  flex: 1;
  font-family: 'Fira Code', monospace;
  font-size: 11px;
  background: #1e1e2e;
  color: #cdd6f4;
  border: 1px solid #45475a;
  border-radius: 6px;
  padding: 8px;
  resize: none;
  tab-size: 4;
  line-height: 1.5;
}
.controls {
  margin-top: 6px;
}
.controls button {
  background: #89b4fa;
  color: #1e1e2e;
  border: none;
  padding: 5px 16px;
  border-radius: 4px;
  font-size: 13px;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.2s;
}
.controls button:hover:not(:disabled) {
  background: #74c7ec;
}
.controls button:disabled {
  opacity: 0.5;
  cursor: wait;
}
.output {
  flex: 1;
  font-family: 'Fira Code', monospace;
  font-size: 10px;
  background: #181825;
  color: #a6e3a1;
  border: 1px solid #313244;
  border-radius: 6px;
  padding: 8px;
  overflow-y: auto;
  white-space: pre-wrap;
  margin: 0;
  min-height: 200px;
}
.output.error {
  color: #f38ba8;
}
</style>
