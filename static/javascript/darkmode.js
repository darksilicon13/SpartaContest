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
    $('#post-button2').css('background-color', '#f7c72a');
    $('#post-button2').css("color", "#000000");
    $('#post-button2').hover(function () {
      $(this).css("color", "#FFFFFF");
      $(this).css("background-color", "#000000");
    }, function () {
      $(this).css("color", "#000000");
      $(this).css('background-color', '#f7c72a')
    });
    $("#comment-section").css('color', '#e7e7e7');
    $('#prev-button').css('filter', 'none');
    $('#next-button').css('filter', 'none');
    $('#youtuber-div').css('background', 'linear-gradient(to top, #30343f, #171b26)');
    $('#downside').css('background-color', '#30343f');
  }
  else if (page === "") {
    $("#genre").css('background', 'linear-gradient( to top, #30343f, #171b26 )');
    $("#genre").css('border-bottom', '2px solid #30343f');
    $('#searchShop').css('color', '#30343f');
    $("#checkbox").css('background-color', "transparent");
    $('body').css("background","#30343f")
  }
  else if (page === "feedback"){
    $('body').css("background","#4b652f");
    $('.about-btn>button').css("background-color", "#6b9042");
  }
  else {
    if (page === "customer_request") {
      $('.youtuberLink').css('color', 'white');
    }
    document.body.classList.add("dark");
    
  }
  $('#sidebar').css('background-color', '#30343f');
  $("#upperSide").css('background-color', '#171b26');
  $('.form-group').css('color', 'white');
  $("#checkbox").css('border', '1px solid white');
  $("button.submit").css('background-color', '#222c37');
  $(".modal-content").removeClass('modal-content-color');
  $(".modal-content").addClass('modal-content-color2');

  $('.txt_field>input').css('background-color', '#dbdfe4')
}

function getBright() {
  console.log("밝게");
  var path = window.location.pathname;
  var page = path.split("/").pop();
  document.body.classList.remove("dark");
  toggleLable.classList.remove("toggleLable");
  toggleBall.classList.remove("toggleBall");
  // if (document.getElementById('authorName')!== null) 
  if (page === "playlist") {
    document.getElementById('authorName').style.color = 'black';
    document.getElementById('authorName').style.fontWeight = 'bold';
    $('#post-button2').css('background-color', '#f7c72a')
    $('#post-button2').css("color", "#000000");
    $('#post-button2').hover(function () {
      $(this).css("color", "#FFFFFF");
      $(this).css("background-color", "#E2314B");
    }, function () {
      $(this).css("color", "#000000");
      $(this).css('background-color', '#f7c72a');
    });
    $("#comment-section").css('color', 'black');
    $('#prev-button').css('filter', 'invert(100%)');
    $('#next-button').css('filter', 'invert(100%)');
    $('#youtuber-div').css('background', 'linear-gradient(to top, #ffffff, #E2314B)');
    $('#downside').css('background-color', '#ffffff');
  }
  else if (page === "") {
    $("#genre").css('background', 'linear-gradient( to top, white, white )');
    $("#genre").css('border-bottom', '2px solid #f5f5f5');
    $('#searchShop').css('color', '#eb6383');
    $('body').css("background","white")
  }
  else if (page === "customer_request") {
    $('.youtuberLink').css('color', 'black');
    $('body').css("background","white");
  }
  else if (page === "feedback"){
    $('body').css("background","#6a9141")
    $('.about-btn>button').css("background-color", "#4b652e")
    
  }
  else {
    document.body.classList.remove("dark");
    $('body').css("background","white");
  }
  $('#sidebar').css('background-color', '#f7c72a');
  $("#upperSide").css('background-color', '#E2314B');
  $('.form-group').css('color', 'black');
  $("#checkbox").css('background-color', "transparent");
  $("button.submit").css('background-color', 'red');
  $(".modal-content").removeClass('modal-content-color2');
  $(".modal-content").addClass('modal-content-color');
  $('.txt_field>input').css('background-color', 'white')
} 