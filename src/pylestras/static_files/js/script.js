/* Authors:
Fábio Cerqueira <cerqueirasfabio@gmail.com>
Italo Maia <italo.maia@gmail.com>
Mário Chaves <macndesign@gmail.com>
*/

$(document).ready(function(){

    // Foca no primeiro input de qualquer form.
    $("form").find("input:visible:first").focus();

    // Escondendo ID e Event do formset add presentation
    $('label[for$="event"]').hide();
    $('label[for$="id"]').hide();

});