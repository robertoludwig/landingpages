$(document).ready(function(){
   $("#elemento_outro").change(function(evento){
      if ($("#elemento_outro").is(":checked"))
          $("#elemento_textarea").show();
      else
         $("#elemento_textarea").hide();
   });
});