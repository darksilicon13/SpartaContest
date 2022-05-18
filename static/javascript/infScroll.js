let movieList = $('#movielist')
let items = $('.videoBox')
let clones = [];
let disableScroll = false;
let scrollheight = 0;
let scrollpos = 0;
let clonesHeight = 0;

function getScrollPos(){
    return movieList.scrollTop; // Amount window scrolled
}

function setScrollPos(pos){
    movieList.scrollTop = pos
}

function getClonesHeight(){
    clonesHeight = 0;

    clones.forEach(clone => {
        clonesHeight += close.offsetHeight; // offsetHeight returns heigh of element
    })
    return clonesHeight
}

//recalculate dimensions when screen is resized
function reCalc(){
    scrollpos = getScrollPos()
    scrollheight = movieList.scrollHeight
    clonesHeight = getClonesHeight()
    if(scrollpos <= 0){
        setScrollPos(1)
    }
}

function scrollUpdate(){
    if(!disableScroll){
        scrollpos = getScrollPos();
        if(clonesHeight + scrollpos >= scrollheight){
            setScrollPos(1)
            disableScroll = true
        }else if(scrollpos <= 0){
            setScrollPos(scrollheight - clonesHeight)
            disableScroll = true
        }
    }
    if(disableScroll){
        window.setTimeout(()=>{
            disableScroll = false
        },40)
    }
}

function onLoad(){
    items.forEach(item => {
        const clone = item.cloneNode(true)
        movieList.appendChild(clone)
        clone.classList.add('js-clone')
    })
    clones = movieList.querySelectorAll('.js-clone')

    reCalc();

    movieList.addEventListener('scroll', () => {
        window.requestAnimationFrame(scrollUpdate)
    }, false)
    window.addEventListener('resize', () => {
        window.requestAnimationFrame(reCalc)
    }, false)
}
window.onload = onLoad()