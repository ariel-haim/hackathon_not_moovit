import logo from './logo.svg';
import './App.css';
import * as React from 'react';
import 'react-select'
import Select from 'react-select/dist/declarations/src/Select';

function App() {

  const [selectedOptions, setSelectedOptions] = useState();

  const optionList = [
    { value: "red", label: "Red" },
    { value: "green", label: "Green" },
    { value: "yellow", label: "Yellow" },
    { value: "blue", label: "Blue" },
    { value: "white", label: "White" }
  ];

  function handleSelect(data) {
    setSelectedOptions(data);
  }

  return (
    <div className="Homepage">
      <h2>Choose your color</h2>
      <div className="dropdown-container">
        <Select
          options={optionList}
          placeholder="Select color"
          value={selectedOptions}
          onChange={handleSelect}
          isSearchable={true}
        />
    </div>
  </div>
  );
}

export default App;
