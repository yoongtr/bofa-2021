// import React, { Component } from 'react';
// import './App.css';
// import { Button, Form, FormGroup, Label } from 'react-bootstrap';
// import GTTForm from "./components/GTTForm"


// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <div>
//         BofA Hackathon 2021
//         </div>
//         <div>
//           <GTTForm />
//         </div>
//       </header>
//     </div>
//   );
// }

// export default App;

import * as React from "react";
import { GTTQuery } from "./components/GTTQuery/GTTQuery";

class App extends React.Component {
  public render() {
    return (
      <div className="mt-3">
        <GTTQuery />
      </div>
    );
  }
}

export default App;
