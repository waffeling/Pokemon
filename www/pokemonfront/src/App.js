import logo from './logo.svg';
import './App.css';
import Header from './header.js';
import LoginModal from './modal.js'
import Card from './card.js';
import Carousel from './carousel.js';

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
      <body>
        <div style={{background: "red", width: "70%"}} class="object-fit-contain border rounded"><Carousel></Carousel></div>
        <div style={{background: "red", width: "70%"}} class="object-fit-contain border rounded"><Carousel></Carousel></div>
      </body>
    </div>
  );
}

export default App;
