import logo from "./logo.svg";
import "./App.css";
import React, { useState, useEffect } from "react";

import { w3cwebsocket as W3CWebSocket } from "websocket";

function App() {
  const [response, setResponse] = useState("");
  const client = new W3CWebSocket("ws://localhost:3000");

  useEffect(() => {
    client.onopen = () => {
      console.log("WebSocket Client Connected");
    };
    client.onmessage = (message) => {
      console.log(message);
      setResponse(message);
    };
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <p>It's {response}</p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
