import { defineCodeRunnersSetup } from '@slidev/types'

export default defineCodeRunnersSetup(() => {
    return {
        async python(code, ctx) {
            try {
                const response = await fetch('http://localhost:3031/run-python', {
                    method: 'POST',
                    headers: { 'Content-Type': 'text/plain' },
                    body: code,
                })
                return await response.json()
            } catch (e: any) {
                return {
                    text: `Error connecting to backend runner: ${e.message}\nMake sure runner-server.js is running.`,
                    error: e.message
                }
            }
        }
    }
})
