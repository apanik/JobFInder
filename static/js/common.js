function loadModal(id, title, url, callback) {
	if ($("#" + id).length == 0) {
		var html = '';
		html += '<div class="modal fade draggable-modal ui-draggable" id="'
				+ id
				+ '" tabindex="-1" role="basic" aria-hidden="true">';
		html += '    <div class="modal-dialog">';
		html += '        <div class="modal-content">';
		html += '            <div class="modal-header ui-draggable-handle">';
		html += '                <button type="button" class="close" data-dismiss="modal" aria-hidden="true"></button>';
		html += '                <h4 class="modal-title"></h4>';
		html += '            </div>';
		html += '            <div class="modal-body">Loading...</div>';
		html += '            <div class="modal-footer">';
		html += '            </div>';
		html += '        </div>';
		html += '    </div>';
		html += '</div>';
		$('body').append(html);
	} else {
		$("#" + id).find('.modal-body').html('Loading...');
	}

	$("#" + id).find('.modal-body').load(url, function() {
		$("#" + id).find(" .modal-title").text(title);
		$("#" + id).modal();
		if (callback) {
			callback();
		}
	});
}

function get(url, callback) {
    var access_token = getAceessToken();
    if(!callback) callback = () => {};
    if(typeof(callback) !== "function") callback = window[callback];
    $.ajax({
        type : 'get',
        url : url,
        beforeSend : function(xhr) {
            if(access_token) xhr.setRequestHeader("Authorization", 'Bearer '+access_token);
        },
        success : callback,
        error: function (httpObj, textStatus) {
            if(httpObj.status == 401){
                if(window.location.pathname.split("/")[1] == "company"){
                    goCompanySignIn();
                }else{
                    goSignIn();
                }
            }
        }
    });
}

function del(url, callback) {
    var csrf = getCsrfToken();
    var access_token = getAceessToken();
    $.ajax({
        url : url,
        beforeSend : function(xhr) {
            if(csrf) xhr.setRequestHeader(csrf.header, csrf.token);
            if(access_token) xhr.setRequestHeader("Authorization", 'Bearer '+access_token);
        },
        type : 'DELETE',
        cache : false,
        success : callback,
        error: function (httpObj, textStatus) {
            if(httpObj.status == 401){
                goSignIn();
            } else {
                callback(httpObj, textStatus);
            }
        }
    });
    return false;
}


function send(url, method, data, callback) {
    var csrf = getCsrfToken();
    var access_token = getAceessToken();
    if(!callback) callback = () => {};
    if(typeof(callback) !== "function") callback = window[callback];
    var request = {
        beforeSend : function(xhr) {
            if(csrf) xhr.setRequestHeader(csrf.header, csrf.token);
            if(access_token) xhr.setRequestHeader("Authorization", 'Bearer '+access_token);
        },
        type : method,
        contentType : 'application/json',
        url : url,
        data : data,
        async: true,        // Cross-domain requests and dataType: "jsonp" requests do not support synchronous operation
        cache: false,       // This will force requested pages not to be cached by the browser
        processData: false, // To avoid making query String instead of JSON
        complete : callback,
    };

    $.ajax(request);
}


function upload(url, formname, callback, errorcallback) {
    var form_data = new FormData($('#' + formname)[0]);
    var access_token = getAceessToken();
    if(!callback) callback = showToast;
    if(typeof(callback) !== "function") callback = window[callback];
    if(typeof(errorcallback) !== "function") errorcallback = window[errorcallback];
    $.ajax({
        beforeSend : function(xhr) {
            if(access_token) xhr.setRequestHeader("Authorization", 'Bearer '+access_token);
        },
        type: 'post',
        url: url,
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,
        success: callback,
        error : errorcallback,
    });
}


function getCsrfToken(){
    //  The html would contain somthing like below"
    //  <meta name="_csrf_header" content="X-CSRF-TOKEN"/>
    //  <meta name="X-CSRF-TOKEN" content="44f02902-3ac0-4d5a-86e2-da3d17430c26"/>
    var header = $("meta[name='_csrf_header']").attr("content");
    var token = $("meta[name='_csrf']").attr("content");
    if (header && token){
        return {
            header: header,
            token: token
        }
    }
}


function post(url, data, callback){
    send(url, "POST", data, callback);
}


function put(url, data, callback){
    send(url, "PUT", data, callback);
}


function initAjaxForms() {
    $("form.ajax:not(.ajax-linked)").on('submit', function(event) {
        event.preventDefault();
        if ($(this).valid()){
            var url = $(this).prop('action');
            var formId = $(this).attr("id");
            var data = form2Json(formId);
            // Image uploading code start here
            var imagesrc = $(".image").attr('src');
            if(imagesrc){
                var stringLength = imagesrc.length - 'data:image/png;base64,'.length;
                var sizeInBytes = 4 * Math.ceil((stringLength / 3))*0.5624896334383812;
                var sizeInKb=sizeInBytes/1000;
            }
            if (imagesrc){
                var imagesrcPart = imagesrc.split(":");
                var jsonObj;
                if (imagesrcPart[0] === "data"){
                    jsonObj = JSON.parse(data);
                    jsonObj.image = imagesrc;
                    data = JSON.stringify(jsonObj);
                }else {
                    jsonObj = JSON.parse(data);
                    jsonObj.image = '';
                    data = JSON.stringify(jsonObj);
                }
            }

            // Image uploading code end here
            if(!imagesrc) {
                var method = $(this).attr('method');
                var callback = $(this).data("callback");  // $(this).attr("data-callback");
                send(url, method, data, callback);
            }
            else{
                if(sizeInKb<=2048){
                    var method = $(this).attr('method');
                    var callback = $(this).data("callback");  // $(this).attr("data-callback");
                    send(url, method, data, callback);
                }
                else{
                    $('.image').attr('src','/static/dashboard/images/user-1.jpg');
                }
            }
        }
        return false;
    }).addClass("ajax-linked");
}

function form2Json(id, includeEmpty){
    var skipEmpty = true;
    if(includeEmpty) skipEmpty = false;
    return JSON.stringify(form2js(id, null, skipEmpty));
}


function json2Form(data, id){
    for(key in data){
        var el = $("#" + id).find("[id='"+ key +"']");
        let elChild = el;
        let dataValue = data[key];
        if(el.hasClass("tinymce-editor")){
            if(data[key] != null){
                tinymce.get(key).setContent(data[key]);
            }
        }
        else if(el.data("parent")){
            setTimeout(function () {
                elChild.val(dataValue).change();
            },1000);
        }
        setTimeout(function () {
            elChild.val(dataValue).change();
        },500);

    }
}

function json2Div(data, container) {
    for (key in data) {
        // var el = $("#" + id).find("[name='"+ key +"']");
        var el = $(container).find("[id='" + key + "']");
        if (data[key]) {
            el.html(String(data[key]).replaceAll('&nbsp;', ' '));
        } else {
            el.parent().hide();
        }
    }
}

function json2DivPopulate(data, container){
    for(key in data) {
        // var el = $("#" + id).find("[name='"+ key +"']");
        var el = $(container).find("[id='" + key + "']");
        el.html(data[key]);

    }
}

function initAjaxSelects(container){
    if(!container) container = "body";
    $(container).find('select[data-src]').each(function() {
        var select = $(this);
        var parentSelector = $(this).attr("data-parent");
        var url = select.attr('data-src');
        if (parentSelector){
            var parent = $(parentSelector);
            parent.on("change", function(){
                var prev_url = url;
                var final_url = prev_url+ "/" + parent.val();
                populateSelect(select, final_url);
            });
        } else {
            populateSelect(select, url);
        }
    });
}

function populateSelect(select, url){
    var access_token = getAceessToken();
    select.find('option').remove();
    select.append('<option value="">' + select.attr('data-placeholder') + '</option>');
    $.ajax({
        url: url,
        beforeSend : function(xhr) {
            if(access_token) xhr.setRequestHeader("Authorization", 'Bearer '+access_token);
        },
        success: function(options) {
            options.map(function(item) {
                var option = $('<option>');
                option
                    .val( item[select.attr('data-value')])
                    .text( item[select.attr('data-text')]);
                select.append(option);
            });
        },
        error: function (httpObj, textStatus) {
            if(httpObj.status == 401){
                if(window.location.pathname.split("/")[1] == "company"){
                    goCompanySignIn();
                }else{
                    goSignIn();
                }
            }
        }
    });
}


function imageUPload(selector) {
    var imageUrl = $(selector).attr('src');
}

function showSuccess(title, msg) {
    Swal.fire({
        icon: 'success',
        title: title,
        text: msg
    })
}

function showError(title, msg) {
    Swal.fire({
        icon: 'error',
        title: title,
        text: msg
    })
}


function showQuestion(title, msg, yesCallback, noCallback) {
    Swal.fire({
        title: title,
        text: msg,
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes',
        cancelButtonText: 'No'
    }).then((result) => {
        if (result.value && typeof (yesCallback) ==='function') {
            yesCallback();
        } else if(result.dismiss=='cancel' && typeof(noCallback) ==='function'){
            noCallback();
        }
    })
}

$.validator.addMethod(
    "regex",
    function(value, element, regexp) {
        var re = new RegExp(regexp);
        return this.optional(element) || re.test(value);
    },
    "Please check your input."
);

function makePagination(totalRecord, pageSize, url, startingIndex){
    if (startingIndex ==1){
        var paginationStringStart = '<nav class="navigation pagination"><div class="nav-links"><button disabled class="prev page-numbers cursor-pointer cursor-pointer" data-value="prev"><i class="fas fa-angle-left"></i></button>';
    }else {
        var paginationStringStart = '<nav class="navigation pagination"><div class="nav-links"><button class="prev page-numbers cursor-pointer cursor-pointer" data-value="prev"><i class="fas fa-angle-left"></i></button>';
    }
    var initialStartingIndex = startingIndex;

    startingIndex = parseInt(startingIndex);
    var numberOfPaginationIndex = totalRecord/pageSize;
    numberOfPaginationIndex = Math.ceil(numberOfPaginationIndex);
    var primaryNumberOfPaginationIndex = numberOfPaginationIndex;
    var paginationIndexString = '';
    if (numberOfPaginationIndex > 10){
        numberOfPaginationIndex=10;
    }

    var paginationPadding = startingIndex-6
    if (startingIndex<7){
        startingIndex=1;
    }else {
        startingIndex=startingIndex-5;
        numberOfPaginationIndex = numberOfPaginationIndex+paginationPadding;
        if (numberOfPaginationIndex > primaryNumberOfPaginationIndex){
            numberOfPaginationIndex = primaryNumberOfPaginationIndex;
            //startingIndex = startingIndex-paginationPadding;
            var paddingStartingIndex =10-(primaryNumberOfPaginationIndex-startingIndex);
            startingIndex = startingIndex-paddingStartingIndex;
        }
    }

    for (startingIndex; startingIndex <= numberOfPaginationIndex; startingIndex++){
        var full_url = url+ "&current_url="+url+"&page=" + startingIndex;
        var full_url_sanitized = encodeURIComponent(full_url);
        var full_url_with_current = url+ "&current_url="+full_url_sanitized+"&page=" + startingIndex;

        if (startingIndex==1 || startingIndex==numberOfPaginationIndex){
            var str ="<a class='page-numbers' href='javascript:void(0);' data-pazesize='"+ pageSize +"' data-value='"+ startingIndex +"' data-url='"+ full_url +"'>"+startingIndex+"</a>";
        }else {
            var str ="<a class='page-numbers' href='javascript:void(0);' data-pazesize='"+ pageSize +"' data-value='"+ startingIndex +"' data-url='"+ full_url +"'>"+startingIndex+"</a>";
        }
        paginationIndexString += str;
    }

    if ((initialStartingIndex*pageSize) > totalRecord){
        var paginationStringEnd = '<button disabled class="next page-numbers" data-value="next"><i class="fas fa-angle-right"></i></button></div></nav>';
    }else if (totalRecord>pageSize){
        var paginationStringEnd = '<button class="next page-numbers" data-value="next"><i class="fas fa-angle-right"></i></button></div></nav>';
    } else {
        var paginationStringEnd = '<button disabled class="next page-numbers" data-value="next"><i class="fas fa-angle-right"></i></button></div></nav>';
    }

    var paginationString = paginationStringStart + paginationIndexString + paginationStringEnd;
    $('.pagination-list').html(paginationString);
}


function goSignIn() {
    window.location.href = '/professional/sign-in/?next=' + window.location.pathname
}

function goCompanySignIn(){
    window.location.href = '/company/sign-in/?next=' + window.location.pathname
}

function favouriteJobAddRemove(id, url) {

    $("#"+id).on('click', '.favourite:not(.apply)', function (event) {
        event.preventDefault();
        var user = getCookie("user");
        var job = $(this).attr('href');
        if(isLoggedIn() && $(this).hasClass('active')){
            var data = {'user_id':user, 'job_id':job};
            favouriteUrl = url;
            post(favouriteUrl, JSON.stringify(data), loadFavouriteJob);
        }else if(isLoggedIn()){
            var data = {'user_id':user, 'job_id':job};
            favouriteUrl = url;
            post(favouriteUrl, JSON.stringify(data), loadFavouriteJob)
        }
        else {
            showQuestion("Sign In required!", "Do you want to sign in now?", goSignIn , 'no')

        }

    });

}

function isLoggedIn() {
    var access_token = getCookie("access");
    if(access_token){
        return true;
    }
    return false;
}

let isCompany = function() {
    var user_type = getCookie("user_type");
    return user_type == "company";
}

function loadFavouriteJob(data) {
    if(data.responseJSON.code == 200){

        var el = $("#jobs").find("[href='"+ data.responseJSON.result.user.job +"']");
        el.each(function () {
            if($(this).hasClass('active')){
                $(this).children().attr("fill", "none");
                $(this).removeClass('active');
                showError('Oopss!', 'Job removed.')
            }
            else if($(this).hasClass("favourite")){
                $(this).addClass('active');
                $(this).children().attr("fill", "#f5d91d");
                // $(".job-list .body .more .buttons .favourite svg").attr("fill", "#ff8fa6");
                showSuccess('Successful!', 'Job saved as a favorite.')

            }

        })
    }
}


// Favourite job common Api

function applyOnlineJobAddRemove(id, url) {


    $("#"+id).on('click', '.apply:not(.applied)', function (event) {
        event.preventDefault();
        var user = getCookie("user");
        var job = $(this).attr('href');

        if(isLoggedIn() && $(this).hasClass('applied')){
            var data = {'user_id':user, 'job_id':job};
            applyonlineUrl = url;
            post(applyonlineUrl, JSON.stringify(data), loadApplyonlineJob);
        }else if(isLoggedIn()){
            showQuestion("Do you want to apply for this job?", "", function () {
                var data = {'user_id':user, 'job_id':job};
                applyonlineUrl = url;
                post(applyonlineUrl, JSON.stringify(data), loadApplyonlineJob);
            });
        }
        else {
            showQuestion("Sign In required!", "Do you want to sign in now?", goSignIn , 'no')
        }

    });

}

// $('.account-button, .account-card').hover( function(e) {
//     e.preventDefault();
//     $('.account-card').css('display', 'block');
// },function(e) {
//     e.preventDefault();
//     $('.account-card').css('display', 'none');
// })

function loadApplyonlineJob(data) {
    if(data.status == 200){
        var el = $("#jobs").find("[href='"+ data.responseJSON.job +"']");
        el.each(function () {
            if($(this).hasClass("apply")){
                $(this).addClass('applied');
                showSuccess('Successful!', 'Job applied successfully.')
                $(this).text('Applied');
                $(this).removeAttr('href').css({"cursor":"default","color":"#ffffff"});
            }
        })
    }
}

function getAceessToken() {
    var access_token = getCookie("access");
    var refresh_token = getCookie("refresh");
    var access_lifetime_hr = getCookie("access_lifetime_hr");
    if (!access_token && refresh_token) {
        $.ajax({
            type : 'POST',
            contentType : 'application/json',
            url : "/api/token/refresh/",
            data : JSON.stringify({
                "refresh": refresh_token
            }),
            async: false,        // Cross-domain requests and dataType: "jsonp" requests do not support synchronous operation
            cache: false,       // This will force requested pages not to be cached by the browser
            processData: false, // To avoid making query String instead of JSON
            complete : ev => {
                access_token = ev.responseJSON.access;
                setCookie('access', access_token, access_lifetime_hr)
            },
        });
    }
    return access_token;
}

function setCookie(cName, cValue, expHours) {
    var d = new Date();
    d.setTime(d.getTime() + (expHours * 60 * 60 * 1000));
    var expires = "expires=" + d.toUTCString();
    document.cookie = cName + "=" + cValue + ";" + expires + ";path=/";
}

function editCookie(cookieName, cookieValue){
    var expireDate = getCookie("refresh_expires_at");
    document.cookie = cookieName + '=' + cookieValue + ';expires=' + expireDate + ";path=/";
}

function getCookie(cName) {
    var name = cName + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function makePaginator(container, data, callback) {
    var links = data.pages.page_links;
    var html = '<ul class="pagination pagination-lg justify-content-center">';
    html += '' +
        '<li class="page-item ' + (data.pages.previous_url ? '' : 'disabled') + '">' +
        '    <a class="page-link" href="javascript:;" onclick="get(\'' + data.pages.previous_url + '\',' + callback + ');" aria-label="Previous">' +
        '        <span aria-hidden="true"><i class="fa fa-arrow-left"></i></span>' +
        '    </a>' +
        '</li>';

    for (i = 0; i < links.length; i++) {
        let link = links[i][0];
        html += '' +
            '<li class="page-item ' + (links[i][2] ? 'active' : '') + '"' + '" >' +
            '    <a class="page-link" href="javascript:;" onclick="get(\'' + link + '\',' + callback + ');">' +
                    (links[i][3] ? '..' : links[i][1]) + '</a>' +
            '</li>';
    }
    html += '' +
        '<li class="page-item ' + (data.pages.next_url ? '' : 'disabled') + '">' +
        '    <a class="page-link" href="javascript:;" onclick="get(\'' + data.pages.next_url + '\',' + callback + ');" aria-label="Next">' +
        '        <span aria-hidden="true"><i class="fa fa-arrow-right"></i></span>' +
        '    </a>' +
        '</li>';

    html += '</ul>';
    $(container).html(html);
}

getAceessToken();

$(document).ready(function () {
    $(document).click(function (event) {
        var click = $(event.target);
        $(".navbar-collapse").each((i, item) => {
            var open = $(item).hasClass("show");
            if (open === true && !click.hasClass("navbar-toggler")) {
                $(item).prev(".navbar-toggler").click();
            }
        });
    });
});
