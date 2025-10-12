import { Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login";
import RegisterPanel from "./components/Register/Register"; // import your register component

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<RegisterPanel />} /> {/* New route */}
      <Route path="/" element={<LoginPanel />} /> {/* Optional: default to login */}
    </Routes>
  );
}

export default App;
