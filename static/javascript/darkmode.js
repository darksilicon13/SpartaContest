const checkbox = document.getElementById("checkbox");
const toggleLable = document.querySelector(".label");
const toggleBall = document.querySelector(".ball");
const names = document.querySelectorAll(".videoText")





checkbox.addEventListener('change', ()=>{
    if( toggleLable.classList.contains("toggleLable") ){
        window.sessionStorage.setItem("darkmode", "false");
        getBright()
    }else{
      window.sessionStorage.setItem("darkmode", "true");
      getDark()
    }
})

function getDark(){
  console.log("어둡게");
  document.body.classList.add("dark");
  toggleLable.classList.add("toggleLable");
  toggleBall.classList.add("toggleBall");
  document.querySelectorAll(".videoText > a > span").forEach((el) => {
    console.log(el);
    el.classList.add('toggleWhite');
});
document.getElementById('authorName').style.color='white';
}

function getBright(){
  console.log("밝게");
    document.body.classList.remove("dark");
    toggleLable.classList.remove("toggleLable");
    toggleBall.classList.remove("toggleBall");
    console.log(document.querySelector(".youtuber > a"));
    document.querySelectorAll(".videoText > a > span").forEach((el) => {
      console.log(el);
      el.classList.remove('toggleWhite');
  });
  document.getElementById('authorName').style.color='black';
}