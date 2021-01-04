$(function () {
 
  window.onload = lanzadera;
  function lanzadera(){   
    contarDocumentos(); 
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
  function contarDocumentos(){
  
    $.getJSON('/mongodb/contarDocumentos',
    {},
    function(data){     
      $("#countAparcamiento").text(data.result)     ;
    }
    );
  }

  $("button#CargarTweets").bind("click", function () {
    
    $.getJSON(
       "/twitter/cargarTweetsTweepy",
      {
        search: $('input[name="search"]').val(),
        maximo: $('input[name="maximo"]').val(),
        fecha_hasta: $('input[name="fecha_hasta"]').val()
      },
      function (data) { 
        $("#msg").text(data.result);
        $("input[type=button]").removeAttr("disabled"); 
      }
    );
    $("input[type=button]").attr("disabled"); 
    return false;
  });
    
});