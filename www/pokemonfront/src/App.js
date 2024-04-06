import logo from './logo.svg';
import './App.css';
import Header from './header.js';
import LoginModal from './modal.js'


function MyButton() {
  return (
    <button>
      I'm a button
    </button>
  );
}



function App() {
  return (
    
    <div className="App">
      
      <Header></Header>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />

        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn To
        </a>
      </header>
    </div>
  );
}

export default App;
