const API_BASE = (import.meta.env.VITE_API_URL || "http://localhost:8000").replace(/\/$/, "");
console.log("API_BASE =", API_BASE);
// -------- ANALYZE IMAGE --------
export async function analyzeImage(imageFile, location) {

  const formData = new FormData();

  // Backend expects field name "file"
  formData.append("file", imageFile);

  // Backend expects lat and lon
  if (location) {
    formData.append("lat", location.lat);
    formData.append("lon", location.lon);
  }

  const res = await fetch(`${API_BASE}/analyze`, {
    method: "POST",
    body: formData
  });

  if (!res.ok) {
    throw new Error("Analyze failed");
  }

  return res.json();
}


// -------- FOLLOWUP QUESTION --------
export async function askFollowup(sessionId, tab, question, history) {

  const res = await fetch(`${API_BASE}/followup`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      session_id: sessionId,
      tab: tab,
      question: question,
      history: history
    })
  });

  if (!res.ok) {
    throw new Error("Followup failed");
  }

  return res.json();
}