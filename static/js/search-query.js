
function carousel(items) {
    var result = "<div class=\"uk-flex uk-flex-center\">\n" +
                "<div class='slick_carousel'>" ;

    items.forEach(function (item) {
     result += '<div>'+item.title+'</div>';
        console.log(item.title);
    });


    result += "</div></div>";

    return result;

}
$(document).on("submit", "#searchform", function (e) {
            e.preventDefault();
            var user_query = $('#user-query').val();
            var request_data = {"user_query":user_query};
            $.ajax({
                type: "POST",
                url: "/query/",
                data: request_data,
                success: function (data) {
                    console.log(data);
                    set_ava_response(data.ava_response);
                    set_ava_board(data.element);
                }
            });
        });

$(document).on("submit", "#signup-form", function (e) {
            e.preventDefault();
            var email = $('#email').val();
            var username = $('#username').val();
            var password = $('#password').val();
            var conf_password = $('#conf_password').val();
            var request_count  = localStorage.getItem('request_count');
            if (password !== conf_password){
                var ava_response = "The two password fields do not match, try again!";
                $('#ava_response').typeIt({strings:ava_response, speed:50});
            }

            var request_data = {"email":email, "username":username, "password":password, "request_count":request_count};
            console.log(request_data);
            $.ajax({
                type: "POST",
                url: "signup/",
                data: request_data,
                success: function (data) {

                    console.log(data);
                    set_ava_response(data.ava_response);
                    set_ava_board(data.element);
                }
            });
        });

$(document).on("submit", "#login-form", function (e) {
            e.preventDefault();
            var email = $('#email').val();
            var password = $('#password').val();
            var request_count  = localStorage.getItem('request_count');

            var request_data = {"email":email, "password":password, "request_count":request_count};
            console.log(request_data);
            $.ajax({
                type: "POST",
                url: "login/",
                data: request_data,
                success: function (data) {
                    console.log(data);
                    set_ava_response(data.ava_response);
                    set_ava_board(data.element);
                    if("user_id" in data.element){
                        set_user_items(data.element);
                        set_user_image_dashboard(get_user_image());
                    }

                }
            });
        });


$(document).on("click", "#btn-ack", function (e) {
        handle_ack(true);
        });

$(document).on("click", "#btn-nack", function (e) {
        handle_ack(false);
        });

$(document).on("click", "#search", function (e) {
        location.reload();
        });

$(document).on("click", "#btn-login", function (e) {
        UIkit.offcanvas('#offcanvas-primary-nav').hide();
        login()
        });

$(document).on("click", "#btn-signup", function (e) {
        UIkit.offcanvas('#offcanvas-primary-nav').hide();
        var ava_response = "Signup!";
        var element = {"action":"signup"};
        set_ava_response(ava_response);
        set_ava_board(element);
        });

$(document).on("click", "#btn_add_ingredient", function (e) {
    event.preventDefault();
    console.log('dawd');

});

