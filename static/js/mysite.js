/**
 * Created by wangyong on 6/4/15.
 */
(function ($) {

    $(function () {

        $(".link-form").on('submit', function (event) {
            theForm = this;

            category = $(this).find("select[name='category']").val();

            AJAXSubmitLinkInfo = {
                url : '/mysite/submit/link',

                data : {
                    secret : $(this).find("input[name='secret']").val(),
                    category : category,
                    title : $(this).find("input[name='title']").val(),
                    link : $(this).find("input[name='link']").val(),
                    desc : $(this).find("textarea").val()
                },

                success : function (data) {
                    $(".link-group-" + category + " > ul").prepend(data);
                    theForm.reset();
                },

                dataType : null
            };

            $.post(AJAXSubmitLinkInfo.url,
                    AJAXSubmitLinkInfo.data,
                    AJAXSubmitLinkInfo.success,
                    AJAXSubmitLinkInfo.dataType);

            event.preventDefault();
        });


        $(".post-form").on('submit', function (event) {
            theForm = this;

            category = $(this).find("select[name='category']").val();

            AJAXSubmitMessageInfo = {
                url : '/mysite/submit/message',

                data : {
                    secret : $(this).find("input[name='secret']").val(),
                    category : category,
                    title : $(this).find("input[name='title']").val(),
                    message : $(this).find("textarea[name='message']").val()
                },

                success : function (data) {
                    $($(".post")[0]).before(data);
                    //theForm.reset();
                },

                dataType : null
            };

            $.post(AJAXSubmitMessageInfo.url,
                    AJAXSubmitMessageInfo.data,
                    AJAXSubmitMessageInfo.success,
                    AJAXSubmitMessageInfo.dataType);

            event.preventDefault();
        });
    });
} (jQuery));