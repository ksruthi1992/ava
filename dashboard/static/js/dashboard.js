$(document).ready(function () {
        var options = [];

        $mode = 0;
        var user_info;
        var request_data;
        var request_count=0;


        var session_data = JSON.parse(localStorage.getItem('session'));

        if(!session_data){
        //    do nothing, no user data, guest user
            user_info = "guest";
        }
        else{
        //    logged in user
            user_info = 'registered'
        }


        request_data = {"user_info": user_info, "request_count":request_count};
        console.log('hy');
        $.ajax({
            type: "POST",
            url: "/query/",
            data: request_data,
            success: function (data) {

                console.log(data);
                console.log(data.ava_response);

                // if check for server session key
                if (!("session_key" in data)){
                    console.log("No session key in response");
                }
                else{
                    localStorage.setItem('session_key',JSON.stringify(data.session_key));
                }

                if("request_count" in data){
                    request_count = data.request_count;
                }

                $('#spinner').hide();
                $('#ava_response').typeIt({strings:data.ava_response, speed:50});
                if("search" in data.element){
                    $('#ava_board').html(search_form);
                }
                else if("login" in data.element){
                    $('#ava_board').html(signup_form);
                }

            }
        });


});



