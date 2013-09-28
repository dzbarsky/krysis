$(document).ready(function(){

   $('.panels').css('visibility','hidden');
   var map1,
        point,
        places = [],
        keywords = [];

   function initializeMap() {
      var mapOptions = {
         zoom: 2,
      	 center: new google.maps.LatLng(35,38),
     	 mapTypeId: google.maps.MapTypeId.ROADMAP
      };
      map1 = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
   }

   function retrieveTexts() {
      $.post('/retrieveTexts/', function(response) {
          var resp = $.parseJSON(response),
             texts = $.parseJSON(resp[0]),
             words = $.parseJSON(resp[1]);
          for (var text in texts) {
             if ($('div[data-id="2-' + texts[text]['pk'] + '"]').length == 0) {
                 var date = texts[text]['fields']['date'].substring(0,10);
                 $('#news_text').append('<div class="reports" data-date="' + date + '" data-id="2-' + texts[text]['pk'] + '">' + texts[text]['fields']['text'] + '</div>');
             }
             var loc = texts[text]['fields']['location'];
             if ($.inArray(loc,places) < 0) {
                places.push(loc);
                plot();
             }
             var existing = [];
             for (var exists in keywords) existing.push(keywords[exists][0]);
             for (var word in words) {
                if ($.inArray(word,existing) < 0) {
                   keywords.push([word, words[word]]);
                }
             }
             generateCloud();
          }
         setTimeout(retrieveTexts, 30000);
      });
   }

   var generateCloud = function() {
      WordCloud(document.getElementById('canvas'), { 'list': keywords, 
              'backgroundColor': 'rgba(255, 255, 255, 0)',
              'gridSize': 25,
              'weightFactor': 25 } );
   }

   function plot() {
      geocoder = new google.maps.Geocoder();
      for (var i = 0; i<places.length;i++){
        var ad = places[i];
        //console.log(ad);
        geocoder.geocode( {'address': ad}, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
          point = results[0].geometry.location;
          var marker = new google.maps.Marker( {
            map: map1,
            position: point,
          });
        } else {
          //alert('Geocode for ' + ad + ' was not successful for the following reason: '+ status);
        }
      });
      }
      
    } //function plot

   function initialize() {
      initializeMap();
      retrieveTexts();
      plot();
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

   $('#trend').click(function(){
  	$('#trend_text').css('visibility','visible');
   });

   $('#news').click(function(){
  	$('#news_text').css('visibility','visible');
   });
  
}); //document ready
