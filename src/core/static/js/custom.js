$(document).ready(function(){
   $("input[name=assuntos]").change(function(evento){
      if ($(this).is(":checked") && $(this).val() == 8)
          $("textarea[name=quais_assuntos]").show();
      else
         $("textarea[name=quais_assuntos]").hide();
   });

   if ( $('#id_ja_fez_compras').length ) {
      var primeiro_option = $('#id_ja_fez_compras option:first-child');
      primeiro_option.text('Já fez compras no Paraguai?');
      primeiro_option.attr('disabled', 'disabled');
   }
});