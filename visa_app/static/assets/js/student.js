function showContent(name) {
  if (name == 'intro'){

    $('#eligibility').css('display', 'none');
    $('#process').css('display', 'none');
    $('#intro').slideToggle();

}

if (name == 'eligibility'){

  $('#intro').css('display', 'none');
  $('#process').css('display', 'none');
  $('#eligibility').slideToggle();

}

if (name == 'process'){

  $('#intro').css('display', 'none');
  $('#eligibility').css('display', 'none');
  $('#process').slideToggle();

}

}


// For Showing content to other page to particular section
//
// $("#federal1").click(function(){   //id of the link which is being clicked
//       $('html, body').animate({
//              scrollTop: $("#federal").offset().top   //id of div to be scrolled
//       }, 1000);
// });
