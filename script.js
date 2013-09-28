$(document).ready(function(){

	$('.panels').css('visibility','hidden');
	var map1;

	function initializeMap() {
      var mapOptions = {
      	zoom: 2,
      	center: new google.maps.LatLng(35,38),
     	mapTypeId: google.maps.MapTypeId.ROADMAP
      	};
      	map1 = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
  }

  function initialize() {
    initializeMap();
}

  initialize();


  $("#about,#news,#trend,#map").click(function(){
  	$('.panels').children().each(function(){
  		$(this).css('visibility','hidden');
  	})

  	$(".tabs").children().each(function(){
  		$(this).css('border-bottom-width','0px');
  	});
  	$(this).css('border-bottom-width','2px');
  	// $("#about").css('color','#fff');
  });

  $("#map").click(function(){
  	$('#map-canvas').css('visibility','visible');
  	// $("#about").css('color','#fff');
  });

  $("#about").click(function(){
  	$("#about_text").css('visibility','visible');
  });

  $('#news').click(function(){
  	$('#news_text').css('visibility','visible');
  });
  

}); //document ready