$( document ).ready(function() {
    $('#id_topic').attr("data-text","name");
    $('#id_topic').attr("data-value","id");
    $('#id_topic').attr("data-src","/api/topic_populate");
    $('#id_topic').attr("data-parent","#id_subject");
    $('#id_topic').attr("data-placeholder","--------");
    $('#id_topic').text('')


    $('#id_sub_topic').attr("data-text","name");
    $('#id_sub_topic').attr("data-value","id");
    $('#id_sub_topic').attr("data-src","/api/sub_topic_populate");
    $('#id_sub_topic').attr("data-parent","#id_topic");
    $('#id_sub_topic').attr("data-placeholder","--------");
    $('#id_sub_topic').text('')




    initAjaxSelects()
});