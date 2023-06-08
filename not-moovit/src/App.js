import React, { useState } from "react";
import "./styles.css";
import Select from "react-select";

export default function App() {
  // React state to manage selected options
  const [selectedLine, setSelectedLine] = useState();
  const [selectedStation, setSelectedStation] = useState();
  // Array of all options
  const lines = [
    { value: "171", label: "171" },
    { value: "271", label: "271" },
    { value: "129", label: "129" },
    { value: "506", label: "506" },
    { value: "71", label: "71" }
  ];

  const station = [
    {value:"reading - brodetsky", label:"reading - brodetsky"},
    {value:"eistein", label:"einstein"},
    {value:"namir",label:"namir"}
  ];

  // Function triggered on selection
  function handleSelect(data) {
    setSelectedLine(data);
  }

  function handleSelectSt(data) {
    setSelectedStation(data);
  }
  return (
    <div className="app">
      <h2>Choose Line</h2>
      <div className="dropdown-container">
        <Select
          options={lines}
          placeholder="Select Line"
          value={selectedLine}
          onChange={handleSelect}
          isSearchable={true}
        />
        <h2>Choose Station</h2>
        <Select
          options={station}
          placeholder="Select station"
          value={selectedStation}
          onChange={handleSelectSt}
          isSearchable={true}
        />
      </div>
    </div>
  );
}