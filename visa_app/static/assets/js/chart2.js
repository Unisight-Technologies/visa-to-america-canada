var ctx = document.getElementById("myChart2").getContext('2d');
var myChart2 = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["Language", "Education", "Work Experience", "Arranged Employment", "Adaptability"],
    datasets: [{
      backgroundColor: [
        "#2ecc71",
        "#3498db",
        "#95a5a6",
        "#9b59b6",
        "#f1c40f",
        "#e74c3c",
      ],
      data: [28, 25, 15, 10, 10]
    }]
  },
  weight: 150
});
//
var canvas = document.getElementById("myChart2");


canvas.onclick = function(evt){
    var activePoints = myChart2.getElementsAtEvent(evt);
    if (activePoints[0]) {
        var chartData = activePoints[0]['_chart'].config.data;
        var idx = activePoints[0]['_index'];

        var label = chartData.labels[idx];
        if(label == "Language"){

          $('#edu').css('display', 'none');
          $('#work').css('display', 'none');
          $('#adapt').css('display', 'none');
          $('#emp').css('display', 'none');
          $('#age').css('display', 'none');
          $('#lang').slideToggle();

        }

        if(label == "Education"){

          $('#lang').css('display', 'none');
          $('#work').css('display', 'none');
          $('#adapt').css('display', 'none');
          $('#emp').css('display', 'none');
          $('#age').css('display', 'none');
          $('#edu').slideToggle();

        }

        if(label == "Work Experience"){

          $('#lang').css('display', 'none');
          $('#edu').css('display', 'none');
          $('#adapt').css('display', 'none');
          $('#emp').css('display', 'none');
          $('#age').css('display', 'none');
          $('#work').slideToggle();

        }

        if(label == "Age"){

          $('#lang').css('display', 'none');
          $('#work').css('display', 'none');
          $('#adapt').css('display', 'none');
          $('#emp').css('display', 'none');
          $('#edu').css('display', 'none');
          $('#age').slideToggle();

        }

        if(label == "Arranged Employment"){

          $('#lang').css('display', 'none');
          $('#work').css('display', 'none');
          $('#adapt').css('display', 'none');
          $('#edu').css('display', 'none');
          $('#age').css('display', 'none');
          $('#emp').slideToggle();

        }

        if(label == "Adaptability"){

          $('#lang').css('display', 'none');
          $('#work').css('display', 'none');
          $('#edu').css('display', 'none');
          $('#emp').css('display', 'none');
          $('#age').css('display', 'none');
          $('#adapt').slideToggle();

        }
      }

    // => activePoints is an array of points on the canvas that are at the same position as the click event.
};



var scored = 0;


var ctx = document.getElementById("newChart2").getContext('2d');
var newChart2 = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: [],
    datasets: [{
      backgroundColor: [
        "#06DB5E",
        "#E74C3C"
      ],
      data: []
    }]
  }
});

function calculateScore2(){
  var language = document.forms["score-form2"]["language"].value;
  var work = document.forms["score-form2"]["work"].value;
  var education = document.forms["score-form2"]["education"].value;
  var family = document.forms["score-form2"]["family"].value;

  console.log(language, work, education, family, emp);



  var score = (Number(language)+Number(work)+Number(education)+Number(family))
  scored = score;
  console.log(score)


  newChart2.data.labels.push("Your Marks ");
  newChart2.data.datasets[0].data.push(scored);
  newChart2.data.labels.push(" ");
  newChart2.data.datasets[0].data.push(100-scored);
  newChart2.update()

    $('#main_modal2').modal('hide');
    $('.insert-here2-1').text("YOUR SCORE: "+score+" pts");
    $('.insert-here2-2').text("CONGRATULATIONS, YOU HAVE PASSED THE TEST!");
    $('.insert-here2-1').css('background', '#06DB5E');




  // else{
  //   $('.insert-here-1').text("YOUR SCORE: "+score+" pts");
  //   $('.insert-here-2').text("SORRY, YOU DID NOT PASS THE TEST.");
  //   $('.insert-here-1').css('background', '#E74C3C');
  //   $('.insert-here-1').css('color', 'white');
  //
  // }

  $('.express-btn2').css('display', 'none');
  $('.performance2').css('display', 'inherit');

}
