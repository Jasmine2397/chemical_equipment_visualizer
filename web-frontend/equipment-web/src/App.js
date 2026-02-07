import "./App.css";
import UploadPage from "./pages/UploadPage";
import Dashboard from "./pages/Dashboard";
import HistoryPage from "./pages/HistoryPage";

function App() {
  return (
    <div className="container">
      <div className="header">
        Chemical Equipment Parameter Visualizer
      </div>

      <UploadPage />
      <Dashboard />
      <HistoryPage />
    </div>
  );
}

export default App;
