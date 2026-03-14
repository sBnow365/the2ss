import { useState } from "react";
import { askFollowup } from "../services/api";

export function useFollowup(sessionId, tab) {

  const [loading, setLoading] = useState(false);

  // store history per tab
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

      const res = await askFollowup(sessionId, tab, question);

      setHistoryMap(prev => ({
        ...prev,
        [tab]: [
          ...prev[tab],
          {
            question,
            answer: res.answer
          }
        ]
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