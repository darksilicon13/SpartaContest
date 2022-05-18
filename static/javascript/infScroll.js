// let intersectionObserver = new IntersectionObserver(function(entries){
//     if(entries[0].intersectionRatio <= 0) return
//
//     loadItems(10);
//     console.log('Loaded new items')
// })
// intersectionObserver.observe((document.querySelector('.scrollFooter')))

const io = new IntersectionObserver((entries, observer)=>{
    entries.forEach(entry => {
        if (!entry.isIntersecting) return;

        if(page._scrollchk) return;

        observer.observe(document.getElementById('sentinel'));
        page._page += 1;
        page.list.search();
    })
})

io.observe(document.getElementById('sentinel'));

$.ajax({
    url: url,
    data: param,
    method: "GET",
    dataType: "json",
    success: function (result){
        console.log(result);
    },
    error: function (err){
        console.log(err);
    },
    beforeSend: function (){
        _scrollchk = true;
        //데이터가 로드 중임을 나타내는 flag입니다
        document.getElementById('list').appendChild(skeleton.show())
        //skeleton을 그리는 함수를 이용해 DOM에 추가
        $('loading').show();
        //loading animation을 가진 요소를 보여줍니다.
    },
    complete: function (){
        _scrollchk = false;

        $('.loading').hide();
        skeleton.hide();
    }
})