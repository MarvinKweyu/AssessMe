

// $(window).on('load', function() {
document.addEventListener('DOMContentLoaded', function(){
// Set the date we're counting down to
//var countDownDate = new Date("Jan 5, 2021 15:37:25").getTime();
// Get today's date and time
let timer = '2:34:00'; // {{ quiz.duration }}
let [h,m,s] = timer.split(':');

let hourtoMin = h * 60;
let min = parseInt(hourtoMin) + parseInt(m);

let oldDateObj = new Date();
let newDateObj = new Date();
newDateObj.setTime(oldDateObj.getTime() + (min * 60 * 1000));

// Update the count down every 1 second
let x = setInterval(function() {
    let now = new Date();

    // Find the distance between now and the count down date
    let distance = newDateObj - now;

    // Time calculations for days, hours, minutes and seconds
    let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Output the result in an element with id="demo"
    document.getElementById("timer").innerHTML = hours + "h " + minutes + "m " + seconds + "s ";

    // If the count down is over, write some text
    if (distance < 0) {
        clearInterval(x);
        document.getElementById("demo").innerHTML = "EXPIRED";
    }
}, 1000);

}, false);
// });
