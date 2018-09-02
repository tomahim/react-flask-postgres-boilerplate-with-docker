import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { CONFIG } from './config.js';

class App extends Component {
  constructor() {
    super();
    this.state = {
        players: []
    };
  }

  componentDidMount() {
    fetch(CONFIG.API_BASE_URL)
        .then(results => results.json())
        .then(players => this.setState({players: players}));
  }

  render() {
    const players = this.state.players.map((player, index) => <li key={index}>{player.firstname} {player.lastname}</li>);

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React!</h1>
        </header>
        <div className="App-intro">
          <ul>
            {players}
          </ul>
        </div>
      </div>
    );
  }
}

export default App;