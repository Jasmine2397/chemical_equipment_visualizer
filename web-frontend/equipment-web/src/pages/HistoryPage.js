import { useEffect, useState } from "react";
import api from "../services/api";

function HistoryPage() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    api.get("history/").then(res => setHistory(res.data));
  }, []);

  return (
    <div className="card">
      <h3>Upload History (Last 5)</h3>
      <ul>
        {history.map((item, i) => (
          <li key={i}>
            {new Date(item.uploaded_at).toLocaleString()} — Total: {item.total_count}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default HistoryPage;
