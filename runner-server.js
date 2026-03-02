import express from 'express'
import cors from 'cors'
import bodyParser from 'body-parser'
import { exec } from 'child_process'
import { promisify } from 'util'
import * as fs from 'fs'
import * as path from 'path'
import * as os from 'os'

const app = express()
const port = 3031
const execAsync = promisify(exec)

app.use(cors())
app.use(bodyParser.text({ type: '*/*' }))

app.post('/run-python', async (req, res) => {
    const code = req.body

    // Create a temporary file to run the python code
    const tempDir = os.tmpdir()
    const tmpFile = path.join(tempDir, `slidev-python-${Date.now()}.py`)

    try {
        fs.writeFileSync(tmpFile, code, 'utf-8')
        // Execute using python from the host environment
        const { stdout, stderr } = await execAsync(`python "${tmpFile}"`)
        res.json({
            text: stdout + (stderr ? '\nError:\n' + stderr : '')
        })
    } catch (e) {
        res.json({
            text: (e.stdout || '') + (e.stderr ? '\nError:\n' + e.stderr : '') + `\nExecution Error:\n${e.message}`,
            error: e.message,
        })
    } finally {
        if (fs.existsSync(tmpFile)) {
            fs.unlinkSync(tmpFile)
        }
    }
})

app.listen(port, () => {
    console.log(`Slidev Code Runner Backend listening on port ${port}`)
})
