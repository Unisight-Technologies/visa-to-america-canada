var ctx = document.getElementById("myChart").getContext('2d');
var myChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["Language", "Education", "Work Experience", "Age", "Arranged Employment", "Adaptability"],
    datasets: [{
      backgroundColor: [
        "#2ecc71",
        "#3498db",
        "#95a5a6",
        "#9b59b6",
        "#f1c40f",
        "#e74c3c",
      ],
      data: [28, 25, 15, 12, 10, 10]
    }]
  }
});
//
var canvas = document.getElementById("myChart");

canvas.onclick = function(evt){
    var activePoints = myChart.getElementsAtEvent(evt);
    if (activePoints[0]) {
        var chartData = activePoints[0]['_chart'].config.data;
        var idx = activePoints[0]['_index'];

        var label = chartData.labels[idx];
        alert(label);
      }

    // => activePoints is an array of points on the canvas that are at the same position as the click event.
};
