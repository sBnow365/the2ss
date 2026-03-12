import { useState } from "react";
import axios from "axios";
import LocationButton from "./components/LocationButton";
import SimpleMarkdown from "./components/SimpleMarkdown";

function App() {
  const [file, setFile] = useState(null);
  const [data, setData] = useState(null); // This will now hold { culture: "...", geo: "...", travel: "..." }
  const [location, setLocation] = useState(null);
  const [activeTab, setActiveTab] = useState("culture");
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      alert("Please select an image first");
      return;
    }
    
    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);

    if (location) {
      formData.append("lat", location.lat);
      formData.append("lon", location.lon);
    }

    try {
      const response = await axios.post("http://127.0.0.1:8000/analyze", formData);
      setData(response.data);
    } catch (error) {
      console.error("Analysis failed", error);
      alert("Error analyzing image.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px", maxWidth: "900px", margin: "0 auto", fontFamily: "sans-serif" }}>
      <h1>🌍 AI Travel Explorer</h1>

      <div style={{ marginBottom: "20px", border: "1px solid #ddd", padding: "15px", borderRadius: "8px" }}>
        <input type="file" onChange={(e) => setFile(e.target.files[0])} />
        <LocationButton setLocation={setLocation} />
        <button onClick={handleUpload} disabled={loading} style={{ marginLeft: "10px" }}>
          {loading ? "Analyzing..." : "Analyze Image"}
        </button>
      </div>

      {file && (
        <img 
          src={URL.createObjectURL(file)} 
          width="300" 
          alt="Preview" 
          style={{ borderRadius: "8px", marginBottom: "20px" }} 
        />
      )}

      {/* Tab Navigation */}
      <div style={{ display: "flex", gap: "10px", marginBottom: "20px" }}>
        {["culture", "geo", "travel"].map((tab) => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            style={{
              padding: "10px 20px",
              backgroundColor: activeTab === tab ? "#007bff" : "#eee",
              color: activeTab === tab ? "#fff" : "#000",
              border: "none",
              borderRadius: "4px",
              cursor: "pointer"
            }}
          >
            {tab.charAt(0).toUpperCase() + tab.slice(1)}
          </button>
        ))}
      </div>

      {/* Content Rendering */}
      {data && (
        <div style={{ border: "1px solid #eee", padding: "20px", borderRadius: "8px", backgroundColor: "#fff" }}>
          {activeTab === "culture" && <SimpleMarkdown content={data.culture} />}
          {activeTab === "geo" && <SimpleMarkdown content={data.geo} />}
          {activeTab === "travel" && <SimpleMarkdown content={data.travel} />}
        </div>
      )}

      {location && (
        <p style={{ fontSize: "12px", color: "#666" }}>
          📍 Search Origin: {location.lat}, {location.lon}
        </p>
      )}
    </div>
  );
}

export default App;