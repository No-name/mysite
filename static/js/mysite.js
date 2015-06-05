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
                    secret : 'abc',
                    category : '1',
                    title : 'hello',
                    link : 'http',
                    desc : 'this'
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