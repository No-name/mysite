/**
 * Created by wangyong on 6/4/15.
 */
(function ($) {

    $(function () {

        $(".link-form").on('submit', function (event) {
            console.log('hello submit link');

            AJAXSubmitLinkInfo = {
                url : 'http://127.0.0.1:8000/mysite/default/submit.json?type=link',

                data : {
                    secret : $(this).find("input[name='secret']").val(),
                    category : $(this).find("select[name='category']").val(),
                    title : $(this).find("input[name='title']").val(),
                    link : $(this).find("input[name='link']").val(),
                    desc : $(this).find("textarea").val()
                },

                success : function () {
                    console.log('post form success');
                },

                dataType : 'json'
            };

            $.post(AJAXSubmitLinkInfo.url,
                    AJAXSubmitLinkInfo.data,
                    AJAXSubmitLinkInfo.success,
                    AJAXSubmitLinkInfo.dataType);

            event.preventDefault();
        });


        $(".post-form").on('submit', function (event) {
            console.log("hello post");

            event.preventDefault();
        });
    });
} (jQuery));