import Card from "./card";
import './index.css';

export default function Carousel (props) {
    return (
<div id = {props.Carouselname} class="carousel slide">
  <div class="carousel-inner ">
    <div class="carousel-item active" > 
      <div class="Carouselcontainer">
        <Card/>
        <Card/>
        <Card/>
        <Card/>
      </div>
    </div>
    <div class="carousel-item">
      <div class="Carouselcontainer">
        <Card/>
        <Card/>
        <Card/>
        <Card/>
      </div>
    </div>
    <div class="carousel-item">
      <div class="Carouselcontainer">
        <Card/>
        <Card/>
        <Card/>
        <Card/>
      </div>
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target={"#"+props.Carouselname} data-bs-slide="prev" style={{backgroundColor:"grey", width: "5%"}}>
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target={"#"+props.Carouselname} data-bs-slide="next" style={{backgroundColor:"grey", width: "5%"}}>
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
    )
}