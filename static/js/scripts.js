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

$('#mob-ico, #mob-exit').click(function () {
  $(".mob-panel").toggleClass("mob-show");
});

$('#calc-expand-link').click(function () {
  $(".mob-sub").toggleClass("mob-sub-show");
});

$('#realm-expand-link').click(function () {
  $(".realm-mob-sub").toggleClass("mob-sub-show");
});

$('#main-sub-link, .main-nav-sub').hover(function () {
  $(".main-nav-sub").toggleClass("ms-show");
});

$('#ally-sub-link, .ally-nav-sub').hover(function () {
  $(".ally-nav-sub").toggleClass("ms-show");
});

$('#realm-sub-link, .realm-nav-sub').hover(function () {
  $(".realm-nav-sub").toggleClass("ms-show");
});

$('#account-btn, .main-account-sub').hover(function () {
  $(".main-account-sub").toggleClass("ms-show");
});

$('#closebtn').click(function () {
  $(".message-wrapper").toggleClass("closemessage");
});

// Modal Windows

$(function () {
  $("#modalHelp, #modalOverlay").on("click", function (e) {
    $(".helpModal").addClass("helpModal-open");
    /* Activate modal background */
    $(".modalBg").addClass("modalActive");
    e.stopPropagation()
  });
  $(document).on("click", function (e) {
    if ($(e.target).is(".helpModal") === false) {
      $(".helpModal").removeClass("helpModal-open");
      /* Deativate modal background */
      $(".modalBg").removeClass("modalActive");
    }
  });
});

// Tabbed content 
// Prices

function rudrSwitchTab(rudr_tab_id, rudr_tab_content) {
  var x = document.getElementsByClassName("tabContent");
  var i;
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  document.getElementById(rudr_tab_content).style.display = "block";

  var x = document.getElementsByClassName("tabmenu");
  var i;
  for (i = 0; i < x.length; i++) {
    x[i].className = "tabmenu";
  }
  document.getElementById(rudr_tab_id).className = "tabmenu active";
}