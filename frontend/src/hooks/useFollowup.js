import { useState } from "react";
import { askFollowup } from "../services/api";

export function useFollowup(sessionId, tab) {

  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);

  async function ask(question) {

    setLoading(true);

    try {
      const res = await askFollowup(sessionId, tab, question);

      setHistory(prev => [
        ...prev,
        {
          question,
          answer: res.answer
        }
      ]);

    } finally {
      setLoading(false);
    }
  }

  return {
    ask,
    history,
    loading
  };
}