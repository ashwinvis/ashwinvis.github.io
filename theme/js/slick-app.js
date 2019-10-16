$(document).ready(function(){
    $('.carousel').slick({
      dots: true,
      autoplay: true,
      autoplaySpeed: 5000,
      slidesToShow: 1,
      slidesToScroll: 1,

      fade: true,
      infinite: true,
      cssEase: 'linear',

      asNavFor: '.carousel-nav',
    });

    $('.carousel-nav').slick({
      arrows: false,  
      slidesToShow: 1,
      slidesToScroll: 1,
      fade: true,
      asNavFor: '.carousel',
      focusOnSelect: true
    });

    $('.lazy').slick({
      lazyLoad: 'ondemand'
    });

});
