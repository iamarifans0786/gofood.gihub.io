
// slider section  

var flag = 0;
// passing 1,-1 through the x and increse & decrese vale of slide
function conlroler(x) {
    flag = flag + x;
    slideShow(flag);
}
slideShow(flag);

function slideShow(num) {
    var slide = document.getElementsByClassName("slider");
    // right btn
    if (num == slide.length) {
        flag = 0;
        num = 0;
    }
    // left btn
    if (num < 0) {
        flag = slide.length - 1;
        num = slide.length - 1;
    }
    //before show we are display none
    for (let y of slide) {
        y.style.display = "none";
    }
    //then display block
    slide[num].style.display = "block";

}

// testimonial section 

var flag = 0;
// passing 1,-1 through the x and increse & decrese vale of slide
function btn(x) {
    flag = flag + x;
    slideShoww(flag);
}
slideShoww(flag);

function slideShoww(num) {
    var slide = document.getElementsByClassName("testimonial");
    // right btn
    if (num == slide.length) {
        flag = 0;
        num = 0;
    }
    // left btn
    if (num < 0) {
        flag = slide.length - 1;
        num = slide.length - 1;
    }
    //before show we are display none
    for (let y of slide) {
        y.style.display = "none";
    }
    //then display block
    slide[num].style.display = "block";

}
