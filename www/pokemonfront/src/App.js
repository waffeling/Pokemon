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
        <div style={{padding:"2em"}}>
          <div class="h4 pb-2 mb-4 border-bottom text-start">
            Your Decks
          </div>
          <div style={{width: "100%"}} class="object-fit-contain border rounded"><Carousel Carouselname = "HomeDecks"></Carousel></div>
        </div>
        <div style={{padding:"2em"}}>
          <div class="h4 pb-2 mb-4 border-bottom text-start">
            Popular Decks
          </div>
          <div style={{width: "100%"}} class="object-fit-contain border rounded"><Carousel Carouselname = "PopularDecks"></Carousel></div>
        </div>
      </body>
    </div>
  );
}

export default App;
