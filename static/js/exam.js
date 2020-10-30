$(function () {
    $('#search-questionnaire').on('click', function () {
        $.ajax({
            url: '/admin/exam/exam/search_questionnaire/',
            type: 'get',
            dataType: 'json',
            success: function (data) {
                $('#search-questionnaire-modal .modal-content').html(data.form);
                $("#search-questionnaire-modal").modal('show');
            }
        });
    });

    // image preview code start here
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('.preview-show').attr('src', e.target.result);
            }

            reader.readAsDataURL(input.files[0]);
        }
    }

    $(".img-preview").change(function () {
        readURL(this);
    });

    $('.preview-show').on('click', function () {
        $('.img-preview').click();
    });
    // image preview code start here

    function showQuestionnaire() {
        $("#template-list").addClass('d-none');
        $('#questionnaire-list').removeClass('d-none');
    }
    function showTemplate() {
        $("#questionnaire-list").addClass('d-none');
        $('#template-list').removeClass('d-none');
    }

    $('#questionnaire-table ').on('click','.removebutton',function () {
        $(this).parent().parent().remove()
    });
    $('#id_topics').text('');

    initAjaxSelects()
})
