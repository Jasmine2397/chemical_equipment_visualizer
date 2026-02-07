import { useEffect, useState } from "react";
import api from "../services/api";

function HistoryPage() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    api.get("history/").then(res => setHistory(res.data));
  }, []);

  return (
    <ul>
      {history.map((item, i) => (
        <li key={i}>
          {item.uploaded_at} - {item.total_count}
        </li>
      ))}
    </ul>
  );
}

export default HistoryPage;
