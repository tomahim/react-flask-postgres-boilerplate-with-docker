import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { CONFIG } from './config.js';

class App extends Component {
  constructor() {
    super();
    this.state = {
        products: []
    };
  }

  componentDidMount() {
    fetch(CONFIG.API_BASE_URL)
        .then(results => results.json())
        .then(results => this.setState({products: results.products}));
  }

  render() {
    const products = this.state.products.map((product, index) => <li key={index}>{product}</li>);

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React!</h1>
        </header>
        <div className="App-intro">
          <ul>
            {products}
          </ul>
        </div>
      </div>
    );
  }
}

export default App;