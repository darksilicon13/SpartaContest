// 페이지 로드 시 메인페이지에서 넣었던 로컬스토리지 search 키워드 가져와서 타이틀에 innerHTML 
const APIKey = "AIzaSyAtomZUsi95t4r5idc9RBkJZjIjKJdi8U0";
const keyword = document.getElementById("videolist-keyword");
const temp_keyword = localStorage.getItem("search")
const inssaName = ["숏박스","너덜트","우왁굳의 게임방송","침착맨"];


function changeKeyword(){
  keyword.innerHTML = "# " + temp_keyword;
  console.log("들어옴")
  if (temp_keyword === "인싸")
    {console.log("시작")
    bringData(inssaName, APIKey)}
  else console.log("실패")
}

function bringData(name, APIKey){
  for(let i=0 ; i < name.length;i++){
  $.ajax({
    type: "GET",
    url: "https://www.googleapis.com/youtube/v3/search?",
    data: {
      part: "snippet",
      key: APIKey,
      type: "channel",
      q: name[i],
      maxResults: 1,
    },
    success: function (response) {
      console.log("in")
        let channelId = response.items[0].snippet.channelId;
        let channelName = response.items[0].snippet.channelTitle;
        let  channelThum = response.items[0].snippet.thumbnails.medium.url;
        localStorage.setItem("channelId" +i, channelId);
        localStorage.setItem("channelName"+i,channelName );
        localStorage.setItem("channelThum"+i,channelThum );
    },
  });
}  renderYoutuberDiv(name);

}

function renderYoutuberDiv(name){
  for ( let i =0; i < name.length; i++){
  const youtuber_box = document.getElementById("youtuber_list")
  // console.log(localStorage.getItem("channelName"+i));
  //  console.log(localStorage.getItem("channelThum"+i));
    let channelName = localStorage.getItem("channelName"+i);
    let thumurl = localStorage.getItem("channelThum"+i);
  let temp_html =
    `<div class="youtuber_box">
    <img class="youtuber_img"
    src="${thumurl}"/>
    <div class="youtuber_text">
    <h3>${channelName}</h3>
    </div>
      </div>`
  $(youtuber_box).append(temp_html);
  }
}


window.onload = changeKeyword;