const API_BASE = "http://localhost:8000/api";

export async function analyzeImage(imageFile, location) {
  const formData = new FormData();

  formData.append("image", imageFile);
  if (location) formData.append("location", location);

  const res = await fetch(`${API_BASE}/analyze`, {
    method: "POST",
    body: formData
  });

  if (!res.ok) throw new Error("Analyze failed");

  return res.json();
}


export async function askFollowup(sessionId, tab, question, history) {

  const res = await fetch(`${API_BASE}/followup`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      session_id: sessionId,
      tab,
      question,
      history
    })
  });

  if (!res.ok) throw new Error("Followup failed");

  return res.json();
}