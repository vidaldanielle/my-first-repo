import { useState } from "react";
import Header from "./components/Header";
import PolicyCard from "./components/PolicyCard";
import { policies } from "./data/policies";
import "./App.css";
import { searchPolicies } from "./utils/searchPolicies";

function App() {
  const [query, setQuery] = useState("");
  const results = searchPolicies(policies, query);

  return (
    <main className="app">
      <Header  total = {policies.length} count = {results.length} />
    <div className="search-row">
      <input
        type="text"
        className="search-box"
        placeholder="Hanapin ang polisiya..."
        value={query}
        onChange={(event) => setQuery(event.target.value)}
      />
      <button type="button" onClick={() => setQuery("")}>
        Burahin
      </button>
    </div>
      {results.length === 0 ? (
        <p>Walang nahanap na polisiya.</p>
      ) : (
        <ul className="policy-list">
          {results.map((policy) => (
            <PolicyCard
              key={policy.id}
              title={policy.title}
              category={policy.category}
              effectiveDate={policy.effectiveDate}
            />
          ))}
        </ul>
      )}
    </main>
  );
}

export default App;