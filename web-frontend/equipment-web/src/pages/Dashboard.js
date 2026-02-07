import { useEffect, useState } from "react";
import api from "../services/api";
import { Bar } from "react-chartjs-2";

function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    api.get("history/").then(res => setData(res.data[0]));
  }, []);

  if (!data) return null;

  return (
    <div>
      <p>Total Count: {data.total_count}</p>
      <p>Avg Flowrate: {data.avg_flowrate}</p>
      <p>Avg Pressure: {data.avg_pressure}</p>
      <p>Avg Temperature: {data.avg_temperature}</p>
    </div>
  );
}

export default Dashboard;
