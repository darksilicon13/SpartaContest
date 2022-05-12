const APIKey = "AIzaSyBNNojaJ-hyukKmlBl2MGPLQMethTkO2uo";  //API 키인데, 타임아웃시 데이터베이스에서 하나씩 가져왔으면 함. 



//playlist.html 에서 #author에 아이콘사진과 이름을 localStorage에서 가져와 바꾸는데 그 과정에서 태그 추가과정이 있었음

$(document).ready(function () {
  const name = localStorage.getItem("youtube")
  const series = localStorage.getItem("series")
  document.getElementById("author").src = localStorage.getItem("icon");
   document.getElementById("authorName").innerHTML = name;
    bringData(name,series);
   });
function bringData(name,series){
    $.ajax({
      type: "GET",
      url: "https://www.googleapis.com/youtube/v3/search?",
      data: {
        part: "snippet",
        key: APIKey,
        type: "playlist",
        q: name+"+"+series,
        maxResults: 1,
      },
      success: function (response) {
        console.log("Bringdata")
        const listid = response.items[0].id.playlistId;
        bringVideoId(listid)
      },
    });
  }
 


// 위에서 재생목록Id를 가져와서 해당 재생목록 아래 비디오들을 가져와서 ifram 삽입까지 완료. 

  function bringVideoId(listid){

    $.ajax({
      type: "GET",
      url: "https://www.googleapis.com/youtube/v3/playlistItems?",
      data: {
        part: "snippet",
        key: APIKey,
        type: "playlist",
        playlistId: listid,
        maxResults: 20,
      },
      success: function (response) {
        console.log("Render videos")
        const carousel = document.getElementById("carousel-inner")
        let temp_html = ``;
        var data = response;
        let length = data.items.length;
        for (let i = length-1; i >= 0 ; i--){
         videoId = data.items[i].snippet.resourceId.videoId;
         if ( i === length-1){
          temp_html=`<div class="carousel-item active">
          <iframe src="https://www.youtube.com/embed/${videoId}" title="YouTube video player" frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
             allowfullscreen></iframe>
          </div>`;
          $(carousel).append(temp_html);
         }else
         {temp_html=`<div class="carousel-item">
           <iframe src="https://www.youtube.com/embed/${videoId}" title="YouTube video player" frameborder="0"
               allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen></iframe>
           </div>`;
           $(carousel).append(temp_html);}
        };
      },
    });
  }
