const checkbox = document.getElementById("checkbox");
const toggleLable = document.querySelector(".label");
const toggleBall = document.querySelector(".ball");
const upperSide = document.getElementById("upperSide")

$(document).ready(function () {
  var date = new Date();
  var time = date.getHours();
  if (window.sessionStorage.getItem("darkmode") === null) window.sessionStorage.setItem("darkmode", "realtime");

  if (window.sessionStorage.getItem("darkmode") === 'realtime') time >= 18 || time < 7 ? getDark() : getBright();
  else if (window.sessionStorage.getItem("darkmode") === "true") getDark();
  else if (window.sessionStorage.getItem("darkmode") === "false") getBright();
 
});



checkbox.addEventListener('change', () => {
  if (toggleLable.classList.contains("toggleLable")) {
    window.sessionStorage.setItem("darkmode", "false");
    getBright();

  } else {
    window.sessionStorage.setItem("darkmode", "true");
    getDark();
  }
})

function getDark() {
  console.log("어둡게");
  var path = window.location.pathname;
  var page = path.split("/").pop();
  document.body.classList.add("dark");
  toggleLable.classList.add("toggleLable");
  toggleBall.classList.add("toggleBall");
  // if (document.getElementById('authorName')!== null) 
  if (page === "playlist") {
    document.getElementById('authorName').style.color = 'white';
    document.getElementById('authorName').style.fontWeight = 'bold';
  }
  else if (page === "") {
    $("#genre").css('background', 'linear-gradient( to top, #30343f, #171b26 )');
    $("#genre").css('border-bottom', '2px solid #30343f');
    $('#searchShop').css('color', '#30343f');
    $("#checkbox").css('background-color', "transparent");
  }
  else {
    if (page === "customer_request") {
      $('.youtuberLink').css('color', 'white');
      
    }
    document.body.classList.add("dark");
  }
  $('#post-button').css('background-color', '#f7c72a')
  $('#post-button').css("color", "#000000");
  $('#post-button').hover(function() {
    $(this).css("color", "#FFFFFF");
    $(this).css("background-color", "#000000");
  }, function(){
    $(this).css("color", "#000000");
    $(this).css('background-color', '#f7c72a')
  });
  $("#comment-section").css('color', '#e7e7e7');
  $('#sidebar').css('background-color', '#30343f');
  $('#prev-button').css('filter', 'none');
  $('#next-button').css('filter', 'none');
  $("#upperSide").css('background-color', '#171b26');
  $('.form-group').css('color', 'white');
  $("#checkbox").css('border','1px solid white');
}

function getBright() {
  console.log("밝게");
  var path = window.location.pathname;
  var page = path.split("/").pop();
  document.body.classList.remove("dark");
  toggleLable.classList.remove("toggleLable");
  toggleBall.classList.remove("toggleBall");
  // if (document.getElementById('authorName')!== null) 
  if (page === "playlist"){
    document.getElementById('authorName').style.color = 'black';
    document.getElementById('authorName').style.fontWeight = 'bold';
  }
  else if (page === "") {
    $("#genre").css('background', 'linear-gradient( to top, white, white )');
    $("#genre").css('border-bottom', '2px solid #f5f5f5');
    $('#searchShop').css('color', '#eb6383');
  }
  else if (page === "customer_request") {
    $('.youtuberLink').css('color', 'black');
  }

  else {
    document.body.classList.remove("dark");
  
  }
  $('#post-button').css('background-color', '#f7c72a')
  $('#post-button').css("color", "#000000");
  $('#post-button').hover(function() {
    $(this).css("color", "#FFFFFF");
    $(this).css("background-color", "#E2314B");
  }, function(){
    $(this).css("color", "#000000");
    $(this).css('background-color', '#f7c72a')
  });
  $("#comment-section").css('color', 'black');
  $('#sidebar').css('background-color', 'white');
  $('#prev-button').css('filter', 'invert(100%)');
  $('#next-button').css('filter', 'invert(100%)');
  $("#upperSide").css('background-color', '#E2314B');
  $('.form-group').css('color', 'black');
  $("#checkbox").css('background-color', "transparent");
} 