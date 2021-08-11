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