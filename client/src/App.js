import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  constructor() {
    this.state = {
        products: []
    };
  }

  componentDidMount() {
    fetch('http://192.168.99.100:5000/')
        .then(results => results.json())
        .then(products => this.state.setState({products}));
  }

  render() {
    const products = this.states.products.map((product, index) => <li key={index}>{product}</li>);

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