$(function () {
 
    window.onload = lanzadera;
    function lanzadera(){   
       
        cargarTweets();   
    }

    function cargarTweets(){
    
      $.getJSON('/nlp/obtenerTweets',
      {},
      function(data){     
        var graphs = JSON.parse(data.table_json);
        Plotly.plot('plotly-timeseries',graphs, {});  
      }
      );
    }
    
  
  });