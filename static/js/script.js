// menu items
var $page = $('.page');

$('.menu_toggle').on('click', function () {
  $page.toggleClass('shazam');
});
$('.content').on('click', function () {
  $page.removeClass('shazam');
});

// search box
function searchToggle(obj, evt) {
  var container = $(obj).closest('.search-wrapper');
  if (!container.hasClass('active')) {
    container.addClass('active');
    evt.preventDefault();
  } else if (
    container.hasClass('active') &&
    $(obj).closest('.input-holder').length == 0
  ) {
    container.removeClass('active');
    container.removeClass('');
    // clear input
    container.find('.search-input').val('');
  }
}

// make stylish text disappear on clicking search box
const searchBoxNode = document.querySelector('.search-icon');
const stylishTextNode = document.querySelector('.arrow-style');
const closeSearchNode = document.querySelector('.close');
const searchTextWrapperNode = document.querySelector('.search-text-wrapper');

searchBoxNode.addEventListener('click', () => {
  stylishTextNode.classList.add('toggle-opacity');

  // hack for making searchbox center after click
  searchTextWrapperNode.style.width = 'auto';
  searchTextWrapperNode.style.alignItems = 'center';
  searchTextWrapperNode.style.marginLeft = 0;

  // show close-search button
  closeSearchNode.style.opacity = 1;
});

closeSearchNode.addEventListener('click', () => {
  stylishTextNode.classList.remove('toggle-opacity');

  // hack for making search box center after click
  searchTextWrapperNode.style.width = '50vw';
  searchTextWrapperNode.style.alignItems = 'flex-start';
  searchTextWrapperNode.style.marginLeft = '50%';

  // hide close-search button
  closeSearchNode.style.opacity = 0;
});