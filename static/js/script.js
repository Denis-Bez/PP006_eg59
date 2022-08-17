/**
* Template Name: Green - v4.8.0
* Template URL: https://bootstrapmade.com/green-free-one-page-bootstrap-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {
  "use strict";


  /**
   * Clients Slider
   */
  new Swiper('.clients-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 3000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 2,
        spaceBetween: 40
      },
      480: {
        slidesPerView: 3,
        spaceBetween: 60
      },
      640: {
        slidesPerView: 4,
        spaceBetween: 80
      },
      992: {
        slidesPerView: 6,
        spaceBetween: 120
      }
    }
  });

  
// Gallery in Product Card

  /**
   * Clients Slider
   */
  new Swiper('.recent-photos-slider', {
    // speed: 400,
    // loop: true,
    // autoplay: {
    //   delay: 5000,
    //   disableOnInteraction: false
    // },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },
      640: {
        slidesPerView: 2,
        spaceBetween: 20
      },
      992: {
        slidesPerView: 3,
        spaceBetween: 20
      },
      1200: {
        slidesPerView: 5,
        spaceBetween: 20
      }
    }
  });

  
  /**
   * Initiate glightbox 
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });


})()