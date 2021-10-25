$(window).scroll(function() {
    // 100 = The point you would like to fade the nav in.
      
        if ($(window).scrollTop() > 100 ){
        
             $('.navbar').addClass('show');
        
      } else {
        
        $('.navbar').removeClass('show');
        
         };   	
    });
    
    $('.scroll').on('click', function(e){		
            e.preventDefault()
        
      $('html, body').animate({
          scrollTop : $(this.hash).offset().top
        }, 1500);
    });
    