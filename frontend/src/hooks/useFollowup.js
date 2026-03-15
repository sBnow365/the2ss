import { useState } from "react";
import { askFollowup } from "../services/api";

export function useFollowup(sessionId, tab) {

  const [loading, setLoading] = useState(false);

  const [historyMap, setHistoryMap] = useState({
    culture: [],
    geo: [],
    travel: [],
    news: []
  });

  const history = historyMap[tab] || [];

  async function ask(question) {

    setLoading(true);

    try {

      // send previous history + new question
      const res = await askFollowup(sessionId, tab, question, history);

      const newEntry = {
        question,
        answer: res.answer
      };

      setHistoryMap(prev => ({
        ...prev,
        [tab]: [...prev[tab], newEntry]
      }));

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