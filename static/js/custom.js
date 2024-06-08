
  (function ($) {
  
  "use strict";

    // MENU
    $('#sidebarMenu .nav-link').on('click',function(){
      $("#sidebarMenu").collapse('hide');
    });
    
    // CUSTOM LINK
    $('.smoothscroll').click(function(){
      var el = $(this).attr('href');
      var elWrapped = $(el);
      var header_height = $('.navbar').height();
  
      scrollToDiv(elWrapped,header_height);
      return false;
  
      function scrollToDiv(element,navheight){
        var offset = element.offset();
        var offsetTop = offset.top;
        var totalScroll = offsetTop-navheight;
  
        $('body,html').animate({
        scrollTop: totalScroll
        }, 300);
      }
    });
  
  })(window.jQuery);

// for form submission
 function submitForm(event) {
        event.preventDefault();

        // Assuming the form submission is successful
        // You can add your own form submission logic here if needed

        // Show the success message
        var successMessage = document.getElementById("success-message");
        successMessage.innerText = "Sent successfully!";
        successMessage.style.display = "block";

        // Set a timeout to hide the success message after 5 seconds
        setTimeout(function () {
          successMessage.style.display = "none";
        }, 5000);

        // Reset the form fields (optional)
        event.target.reset();

        return false;
      }
