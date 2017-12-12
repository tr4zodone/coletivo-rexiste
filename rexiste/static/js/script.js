var popper = $("#popper");
var searchbar = $("#searchbar");

// for when the window is loaded small
if ($(window).width() < 1200)
{
    popper.addClass("ahide");
    popper.addClass("ahide");
    searchbar.removeClass("searchbar-expanded");
    searchbar.addClass("searchbar-minimized");
}

// for when the window changes after loading 
function widthWatch()
{
    var w = window.outerWidth; 
    console.log("Window width is:" + w);
    if (w < 1200)
    {
	// postagens
	popper.addClass("ahide");

	// search bar
	searchbar.removeClass("searchbar-expanded");
	searchbar.addClass("searchbar-minimized");
    }
    else if (w >= 1200)
    {
	// postagens
	popper.removeClass("ahide");

	// search bar
	searchbar.addClass("searchbar-expanded");
	searchbar.removeClass("searchbar-minimized");
    }
}

// back arrow hover "animation"
$("#back").hover(
  function() {
    $("#back_span").addClass( "hover" );
  }, function() {
    $("#back_span").removeClass( "hover" );
  }
);

