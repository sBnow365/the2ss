export async function processImage(file, task) {
  const form = new FormData()
  form.append("file", file)
  form.append("task", task)

  const res = await fetch("http://localhost:8000/image/process", {
    method: "POST",
    body: form
  })

  return res.json()
}
