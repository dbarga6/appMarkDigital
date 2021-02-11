$(function () {
 
  window.onload = lanzadera;
  function lanzadera(){   
    contarDocumentos(); 
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
    alert("dentro");
    
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