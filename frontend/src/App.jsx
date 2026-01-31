import { useState } from "react"
import { processImage } from "./api"

export default function App() {
  const [file, setFile] = useState(null)
  const [task, setTask] = useState("vision")
  const [output, setOutput] = useState("")

  async function handleSubmit() {
    const res = await processImage(file, task)
    setOutput(JSON.stringify(res, null, 2))
  }

  return (
    <div style={{ padding: 40 }}>
      <h2>Travel Vision AI</h2>

      <input type="file" onChange={e => setFile(e.target.files[0])} />

      <select onChange={e => setTask(e.target.value)}>
        <option value="vision">Location & Places</option>
        <option value="caption">Image Caption</option>
        <option value="ai">AI Image Detection</option>
      </select>

      <button onClick={handleSubmit}>Run</button>

      <pre>{output}</pre>
    </div>
  )
}
