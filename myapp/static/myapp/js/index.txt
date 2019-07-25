window.onload = function(){

    var bar_data = [];
    var attendance = [63,78,92,86,90,85];
    console.log("Hello world");
    var ctx = document.getElementById("myChart").getContext('2d');
    var ctx1 = document.getElementById("myChart1").getContext('2d');
    function loadDoc() {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                var obj = JSON.parse(this.responseText);
                bar_data = [obj.web_students,obj.os_students,obj.ethics_students,obj.net_students,obj.business_students,obj.req_students]
                console.log(bar_data);
                createChart(bar_data,ctx,"Students","bar");
                createChart(attendance,ctx1,"Attendance","doughnut");
            }
            else{
                console.log("Response faild");
            }
        };
  xhttp.open("GET", "/serve_data", true);
  xhttp.send();
}
loadDoc();
let menu1 = document.getElementById("menu1");
let menu = document.getElementById("menu");
menu1.addEventListener("click",function(){
    console.log("clicked");
    menu.classList.remove("close");
    menu.classList.add("visible");

});
let bod = document.querySelector("#div");
bod.addEventListener("click",function(){
    menu.classList.remove("visible");
    menu.classList.add("close");
});
function createChart(data,ctx,type,graphType){
    console.log(type);
    var myChart = new Chart(ctx, {
        type: graphType,
        data: {
            labels: ["Web Development", "Operating System", "Professional Ethics", "Networking",
            "Business Writing", "Requirements Engineering"],
            datasets: [{
                label: `${type} of each department`,
                data: data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.5)',
                    'rgba(54, 162, 235, 0.5)',
                    'rgba(255, 206, 86, 0.5)',
                    'rgba(75, 192, 192, 0.5)',
                    'rgba(153, 102, 255, 0.5)',
                    'rgba(255, 159, 64, 0.5)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
}



};
