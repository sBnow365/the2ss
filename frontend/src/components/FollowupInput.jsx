import { useState } from "react";

export default function FollowupInput({ onAsk, loading }) {

  const [question, setQuestion] = useState("");

  const submit = () => {
    if (!question.trim()) return;

    onAsk(question);
    setQuestion("");
  };

  return (
    <div style={{ marginTop: 20 }}>

      <input
        placeholder="Ask something more about this..."
        value={question}
        onChange={e => setQuestion(e.target.value)}
        style={{
          width: "75%",
          padding: "10px",
          borderRadius: "6px",
          border: "1px solid #ccc"
        }}
      />

      <button
        onClick={submit}
        disabled={loading}
        style={{
          marginLeft: 10,
          padding: "10px 16px"
        }}
      >
        {loading ? "..." : "Ask"}
      </button>

    </div>
  );
}