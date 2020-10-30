$( document ).ready(function() {
    $('#id_topics').attr("data-text","name");
    $('#id_topics').attr("data-value","id");
    $('#id_topics').attr("data-placeholder","--------");
    $('#id_topics').attr("data-src","/api/topic_populate");
    $('#id_topics').attr("data-parent","#id_subject");
    $('#id_topics').text('')

    initAjaxSelects();



});