import { useEffect, useState } from "react";
import api from "../services/api";

function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    api.get("history/").then(res => {
      if (res.data.length > 0) setData(res.data[0]);
    });
  }, []);

  if (!data) return null;

  return (
    <div className="card">
      <h3>Dataset Summary</h3>

      <div className="summary-grid">
        <div className="summary-item">
          Total<br />{data.total_count}
        </div>
        <div className="summary-item">
          Avg Flowrate<br />{data.avg_flowrate.toFixed(2)}
        </div>
        <div className="summary-item">
          Avg Pressure<br />{data.avg_pressure.toFixed(2)}
        </div>
        <div className="summary-item">
          Avg Temperature<br />{data.avg_temperature.toFixed(2)}
        </div>
      </div>

      <br />

      <button onClick={() => window.open("http://127.0.0.1:8000/api/report/")}>
        Download PDF Report
      </button>
    </div>
  );
}

export default Dashboard;
