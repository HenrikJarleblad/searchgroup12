import React, { Component } from 'react';
import Question from './Question'
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
        <h1 className="App-title">Chatbot</h1>
        </header>
        <div>
          <Question/>
        </div>
      </div>
    );
  }
}

export default App;
