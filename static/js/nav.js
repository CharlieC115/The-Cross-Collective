$(document).ready(function() {
    $('.navbar').removeClass('nav-bg-colour');
  });

$(window).scroll(function() {	
    
    if ($(window).scrollTop() >= 650 ){
        
        $('.navbar').addClass('show');
    
    } else {
    
        $('.navbar').removeClass('show');
    
    };   	
});

$('.scroll').on('click', function(e){		
        e.preventDefault()
});
    