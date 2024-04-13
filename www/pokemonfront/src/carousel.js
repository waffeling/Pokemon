import Card from "./card"

export default function Carousel () {
    return (
        <div id="carouselExample" class="carousel slide">
  <div class="carousel-inner position-relative start-50">
    <div class="carousel-item active">
      <Card/>
    </div>
    <div class="carousel-item">
    <Card/>
    </div>
    <div class="carousel-item">
    <Card/>
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
    )
}