import React from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Landing from "./pages/Landing";
import CalculatorPage from "./pages/CalculatorPage";
import "./index.css";

function App(){
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-gray-50 text-gray-800">
        <header className="p-4 border-b">
          <div className="container mx-auto flex justify-between">
            <h1 className="font-bold">OmniCalc Pro</h1>
            <nav className="space-x-4">
              <Link to="/">Home</Link>
            </nav>
          </div>
        </header>
        <main className="container mx-auto p-6">
          <Routes>
            <Route path="/" element={<Landing/>} />
            <Route path="/calculator/:module" element={<CalculatorPage/>} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

createRoot(document.getElementById("root")!).render(<App />);
