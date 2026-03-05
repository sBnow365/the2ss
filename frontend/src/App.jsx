import { useState } from "react";
import axios from "axios";
import LocationButton from "./components/LocationButton"
import Section from "./components/Section"
import BulletList from "./components/BulletList"
import CardGrid from "./components/CardGrid"

function App() {
  const [file, setFile] = useState(null);
  const [data, setData] = useState(null);
  const [location, setLocation] = useState(null);
  const [activeTab, setActiveTab] = useState("culture");


  const handleUpload = async () => {
  if (!file) {
    alert("Please select an image first");
    return;
  }
    const formData = new FormData();
    formData.append("file", file);

      if (location) {
    formData.append("lat", location.lat);
    formData.append("lon", location.lon);
  }

    const response = await axios.post(
      "http://127.0.0.1:8000/analyze",
      formData
    );

    setData(response.data);
  };

  return (
    <div>
      <h1>What's on your mind?</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <LocationButton setLocation={setLocation} />

      <button onClick={handleUpload}>Analyze</button>
      {file && (
        <img
          src={URL.createObjectURL(file)}
          width="300"
        />
      )}
    <div style={{ marginTop: "20px" }}> 
      <button onClick={() => setActiveTab("culture")}>
        Culture
      </button>

      <button onClick={() => setActiveTab("geo")}>
        Geography
      </button>

      <button onClick={() => setActiveTab("travel")}>
        Travel
      </button>
    </div>
        {data && (
          <div style={{ marginTop: "20px" }}>
            
  {activeTab === "culture" && data.culture && (

    <div>

      <Section title="Cultural Significance">
        <BulletList items={data.culture.cultural_significance} />
      </Section>

      <Section title="Important People">
        <CardGrid items={data.culture.important_people} />
      </Section>

      <Section title="Food & Fun Facts">
        <BulletList items={data.culture.food_and_fun_facts} />
      </Section>

    </div>

  )}
 {activeTab === "geo" && data.geo && (

    <div>

      <Section title="landforms">
        <BulletList items={data.geo.landforms} />
      </Section>
      <Section title="Weather around the Year">
        <CardGrid items={data.geo.weather_info} />
      </Section>
      <Section title="Rain and Natural Resources">
        <BulletList items={data.geo.rain_natural_resources} />
      </Section>

      <Section title="Flora and Fauna">
        <BulletList items={data.geo.flora_fauna} />
      </Section>

      <Section title="Population data">
        <BulletList items={data.geo.population_facts} />
      </Section>
    </div>

  )}
{/* {activeTab === "travel" && data.travel && (

    <div>

      <Section title="Distance">
        <BulletList items={data.geo.distance} />
      </Section>
      <Section title="Ways to reach">
        <BulletList items={data.travel.suggested_transport} />
      </Section>
      <Section title="Helpful Information">
        <BulletList items={data.travel.tips} />
      </Section>

    </div>

  )} */}
            {activeTab === "travel" && (
              <pre>{JSON.stringify(data.travel, null, 2)}</pre>
            )}

          </div>
        )}
      {location && (
      <p>
        Your location: {location.lat}, {location.lon}
      </p>
    )}
    </div>
  );
}

export default App;