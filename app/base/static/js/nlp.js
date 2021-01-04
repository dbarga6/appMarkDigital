$(function () {
 
    window.onload = lanzadera2;
    function lanzadera2(){   
        print("hola");
        cargarTweets();   
    }
    function cargarTweets(){
      alert("hola");
      $.getJSON('/nlp/obtenerTweets',
      {},
      function(data){     
        $("#plotly-timeseries").text("hecho")     ;
      }
      );
    }
  
  });