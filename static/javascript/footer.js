const searchbtn = document.getElementById("button-addon2");
const searchinput = document.querySelector(".form-control");


function youtube(value) {
  window.open("https://www.youtube.com/results?search_query=" + value);
  searchinput.value = "";
}
searchbtn.addEventListener("click", () => {
  const value = searchinput.value;
  youtube(value);
});
