
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
                    $('#ava_response').typeIt({strings:data.ava_response, speed:50});
                    if("options" in data.element){
                        $('#ava_board').html(carousel(data.element.options));
                        $('.slick_carousel').slick({
                            infinite: true,
                            slidesToShow: 3,
                            slidesToScroll: 3
                        });
                    }
                    else if("login" in data.element){

                        $('#ava_board').html(login_form);
                    }
                }
            });
        });

$(document).on("submit", "#signup-form", function (e) {
            e.preventDefault();
            var email = $('#email').val();
            var username = $('#username').val();
            var password = $('#password').val();
            var conf_password = $('#conf_password').val();
            if (password !== conf_password){
                var ava_response = "The two password fields do not match, try again!";
                $('#ava_response').typeIt({strings:ava_response, speed:50});
            }

            var request_data = {"email":email, "username":username, "password":password};
            console.log(request_data);
            $.ajax({
                type: "POST",
                url: "/signup/",
                data: request_data,
                success: function (data) {

                    console.log(data);
                    $('#ava_response').typeIt({strings:data.ava_response, speed:50});

                    if("search" in data.element){

                        $('#ava_board').html(search_form);
                    }
                }
            });
        });