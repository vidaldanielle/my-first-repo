import Header from "./components/Header";
import PolicyCard from "./components/PolicyCard";
import { policies } from "./data/policies";
import "./App.css";

function App() {
  return (
    <main className="app">
      <Header count={policies.length} />

      {policies.length === 0 ? (
        <p>Walang polisiya.</p>
      ) : (
        <ul className="policy-list">
          {policies.map((policy) => (
            <PolicyCard
              key={policy.id}
              title={policy.title}
              category={policy.category}
            />
          ))}
        </ul>
      )}
    </main>
  );
}

export default App;