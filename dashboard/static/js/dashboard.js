$(document).ready(function () {
        var options = [];

        $mode = 0;
        var user_info;
        var request_data;

        var user_token = get_user_token();
        var request_count = get_request_count();

        if(!user_token){
        //    do nothing, no user data, guest user
            user_info = 0;
            $('#nav-user').html('<a href="javascript:login()">Login</a>');
        }
        else{
        //    logged in user
            user_info = 1;
        }

        if(!request_count){
        //    first request
            request_count = 0;
            set_request_count(request_count)
        }

        request_data = {"user_info": user_info, "request_count":request_count};

        $.ajax({
            type: "POST",
            url: "/query/",
            data: request_data,
            success: function (data) {

                console.log(data);
                console.log(data.ava_response);


                if ("request_count" in data){
                    set_request_count(request_count);
                }

                // if check for server session key
                if (user_info === 1){
                    set_user_image_dashboard(get_user_image());
                }
                else{
                    console.log("No user_token in response");
                }

                $('#spinner').hide();
                set_ava_response(data.ava_response);
                console.log(data.element.action);
                set_ava_board(data.element);

            }
        });


});



