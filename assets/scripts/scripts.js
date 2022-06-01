/* Home Page Slider */
setInterval(
    function () {
        $('.SlideMyImg').shape('flip left');
},3500);
$('.ui.embed').embed();

/* Projects Page Flip Images */
function flip_me_left() {
    $('.shape').shape('flip left');
}
function flip_me_right() {
    $('.shape').shape('flip right');
}

/* Child Development Page Accordion */
$('.ui.accordion').accordion();

/* NavBar Account Logout - Account Page */
$('.Account_DropDown').dropdown();
