import { useState } from "react";

function App() {
  const [url, setUrl] = useState("");
  const [data, setData] = useState(null);

  const fetchRecipe = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/extract", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });

      const result = await response.json();
      setData(result);
    } catch (error) {
      setData({
        title: "Error",
        message: "Backend not connected",
      });
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>🍲 Recipe Extractor</h1>

      <input
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Enter recipe URL"
        style={{ width: "400px", padding: "10px" }}
      />

      <br /><br />

      <button onClick={fetchRecipe} style={{ padding: "10px 20px" }}>
        Extract Recipe
      </button>

      {data && (
        <div style={{ marginTop: "20px", border: "1px solid #ccc", padding: "15px" }}>
          <h2>{data.title}</h2>
          <p>{data.message}</p>

          <h3>Ingredients</h3>
          <ul>
            {data.ingredients?.map((item, i) => (
              <li key={i}>{item}</li>
            ))}
          </ul>

          <h3>Steps</h3>
          <ol>
            {data.steps?.map((step, i) => (
              <li key={i}>{step}</li>
            ))}
          </ol>
        </div>
      )}
    </div>
  );
}

export default App;
