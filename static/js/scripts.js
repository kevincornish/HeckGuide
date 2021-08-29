// Expirementing (Don't delete)
/*
var $mobMenu = $('.close-ico');

$mobMenu.click(function () {
  $mobMenu.removeClass('mob-show');
  $(this).addClass('mob-show');
});

$(function () {
  $(".mob-menu-ico").click(function () {
    $(this).toggleClass("mob-show");
  });
});
*/

$('#mob-ico, #mob-exit').click( function() {
  $(".mob-panel").toggleClass("mob-show");
} );

$('#calc-expand-link').click( function() {
  $(".mob-sub").toggleClass("mob-sub-show");
} );

$('#realm-expand-link').click( function() {
  $(".mob-sub-realm").toggleClass("mob-sub-show");
} );

$('#main-sub-link, .main-nav-sub').hover( function() {
  $(".main-nav-sub").toggleClass("ms-show");
} );

$('#realm-sub-link, .realm-nav-sub').hover( function() {
  $(".realm-nav-sub").toggleClass("ms-show");
} );

$('#account-btn, .main-account-sub').hover( function() {
  $(".main-account-sub").toggleClass("ms-show");
} );

$('#closebtn').click( function() {
  $(".message-wrapper").toggleClass("closemessage");
} );