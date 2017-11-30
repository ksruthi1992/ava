
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

