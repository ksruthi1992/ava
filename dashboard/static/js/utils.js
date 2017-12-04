
function logout(){
    console.log('logout');
    localStorage.clear();
    location.reload();
}

function set_request_count(request_count){
    localStorage.setItem('request_count', request_count);
}

function get_request_count() {
    return localStorage.getItem('request_count');
}

function set_user_token(user_token){
    localStorage.setItem('user_token', user_token);
}

function set_user_id(user_id) {
    localStorage.setItem('user_id', user_id);
}

function get_user_id() {
    return localStorage.getItem('user_id');
}

function get_user_token() {
    return localStorage.getItem('user_token');
}
function get_user_image() {
    return localStorage.getItem('user_image');
}

function set_user_image(user_image) {
    localStorage.setItem('user_image', user_image);
}

function is_user_logged_in() {
    user_token = localStorage.getItem('user_token');
    if(user_token){
        return true;
    }else {
        return false;
    }
}

function set_ava_response(ava_response) {
    $('#ava_response').typeIt({strings:ava_response, speed:30});
}

function set_user_image_dashboard(user_image) {
    remove_login();
    $('#nav-user').html(nav_user);
    if(user_image){
        $('#nav-user-image').attr("src",user_image);
    }
}

function set_user_items(element){
    var user_token = element.user_token;
    set_user_token(user_token);
    var user_id = element.user_id;
    set_user_id(user_id);
    var user_image = element.user_image;
    set_user_image(user_image);
}

function get_action_on(ack){
    if(ack){
        return localStorage.getItem('action_on_ack');
    }
    else {
        return localStorage.getItem('action_on_nack');
    }
}

function get_response_on(ack){
    if(ack){
        return localStorage.getItem('response_on_ack');
    }
    else {
        return localStorage.getItem('response_on_nack');
    }
}

function set_action_on(ack,value){
    if(ack){
        localStorage.setItem('action_on_ack', value);
    }
    else {
        localStorage.setItem('action_on_nack', value);
    }
}
function set_response_on(ack, value){
    if(ack){
        localStorage.setItem('response_on_ack', value);
    }
    else {
        localStorage.setItem('response_on_nack', value);
    }
}

function handle_ack(ack) {
    var action = get_action_on(ack);
    var ava_response = get_response_on(ack);

    set_ava_response(ava_response);
    var element = {"action":action}
    set_ava_board(element);
}

function set_ack_items(ack) {
    set_action_on(true, ack.action);
    set_response_on(true, ack.response);
}

function set_nack_items(nack) {
    set_action_on(false, nack.action);
    set_response_on(false, nack.response);
}

function set_options_on_board(options) {
    console.log(options);
    var options_1 = '<div class="uk-flex uk-flex-center">';
    var options_2 = '';
    for(i=0;i<options.length; i++){
        if(i === 0){
        options_2 += '<div class="uk-card uk-card-large uk-card-body tile">'+options[i].title+'</div>';
        }else {
        options_2 += '<div class="uk-card uk-card-large uk-card-body uk-margin-left tile">'+options[i].title+'</div>';
        }
    }
    var options_3 = '</div>';
    var image_1 = "<img class='recipe_option' src=\"data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/PjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQwMCIgdmlld0JveD0iMCAwIDYwMCA0MDAiIHByZXNlcnZlQXNwZWN0UmF0aW89Im5vbmUiPjwhLS0KU291cmNlIFVSTDogaG9sZGVyLmpzLzYwMHg0MDAvc2t5L2F1dG8vdGV4dDoxL3NpemU6MTAwCkNyZWF0ZWQgd2l0aCBIb2xkZXIuanMgMi41LjIuCkxlYXJuIG1vcmUgYXQgaHR0cDovL2hvbGRlcmpzLmNvbQooYykgMjAxMi0yMDE1IEl2YW4gTWFsb3BpbnNreSAtIGh0dHA6Ly9pbXNreS5jbwotLT48ZGVmcy8+PHJlY3Qgd2lkdGg9IjYwMCIgaGVpZ2h0PSI0MDAiIGZpbGw9IiMwRDhGREIiLz48Zz48dGV4dCB4PSIyNjIuOTI5Njg3NSIgeT0iMjQ0LjciIHN0eWxlPSJmaWxsOiNGRkZGRkY7Zm9udC13ZWlnaHQ6Ym9sZDtmb250LWZhbWlseTpBcmlhbCwgSGVsdmV0aWNhLCBPcGVuIFNhbnMsIHNhbnMtc2VyaWYsIG1vbm9zcGFjZTtmb250LXNpemU6MTAwcHQiPjE8L3RleHQ+PC9nPjwvc3ZnPg==\" width=\"600\" height=\"400\" alt=\"1 [600x400]\" draggable=\"false\" data-src=\"holder.js/600x400/sky/auto/text:1/size:100\" data-holder-rendered=\"true\">";
    var image_2 = "<img class='recipe_option' src=\"data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/PjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQwMCIgdmlld0JveD0iMCAwIDYwMCA0MDAiIHByZXNlcnZlQXNwZWN0UmF0aW89Im5vbmUiPjwhLS0KU291cmNlIFVSTDogaG9sZGVyLmpzLzYwMHg0MDAvdmluZS9hdXRvL3RleHQ6Mi9zaXplOjEwMApDcmVhdGVkIHdpdGggSG9sZGVyLmpzIDIuNS4yLgpMZWFybiBtb3JlIGF0IGh0dHA6Ly9ob2xkZXJqcy5jb20KKGMpIDIwMTItMjAxNSBJdmFuIE1hbG9waW5za3kgLSBodHRwOi8vaW1za3kuY28KLS0+PGRlZnMvPjxyZWN0IHdpZHRoPSI2MDAiIGhlaWdodD0iNDAwIiBmaWxsPSIjMzlEQkFDIi8+PGc+PHRleHQgeD0iMjYyLjkyOTY4NzUiIHk9IjI0NC43IiBzdHlsZT0iZmlsbDojMUUyOTJDO2ZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1mYW1pbHk6QXJpYWwsIEhlbHZldGljYSwgT3BlbiBTYW5zLCBzYW5zLXNlcmlmLCBtb25vc3BhY2U7Zm9udC1zaXplOjEwMHB0Ij4yPC90ZXh0PjwvZz48L3N2Zz4=\" width=\"600\" height=\"400\" alt=\"2 [600x400]\" draggable=\"false\" data-src=\"holder.js/600x400/vine/auto/text:2/size:100\" data-holder-rendered=\"true\">";
    var image_3 = "<img class='recipe_option' src=\"data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/PjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQwMCIgdmlld0JveD0iMCAwIDYwMCA0MDAiIHByZXNlcnZlQXNwZWN0UmF0aW89Im5vbmUiPjwhLS0KU291cmNlIFVSTDogaG9sZGVyLmpzLzYwMHg0MDAvbGF2YS9hdXRvL3RleHQ6My9zaXplOjEwMApDcmVhdGVkIHdpdGggSG9sZGVyLmpzIDIuNS4yLgpMZWFybiBtb3JlIGF0IGh0dHA6Ly9ob2xkZXJqcy5jb20KKGMpIDIwMTItMjAxNSBJdmFuIE1hbG9waW5za3kgLSBodHRwOi8vaW1za3kuY28KLS0+PGRlZnMvPjxyZWN0IHdpZHRoPSI2MDAiIGhlaWdodD0iNDAwIiBmaWxsPSIjRjg1OTFBIi8+PGc+PHRleHQgeD0iMjYyLjkyOTY4NzUiIHk9IjI0NC43IiBzdHlsZT0iZmlsbDojMUMyODQ2O2ZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1mYW1pbHk6QXJpYWwsIEhlbHZldGljYSwgT3BlbiBTYW5zLCBzYW5zLXNlcmlmLCBtb25vc3BhY2U7Zm9udC1zaXplOjEwMHB0Ij4zPC90ZXh0PjwvZz48L3N2Zz4=\" width=\"600\" height=\"400\" alt=\"3 [600x400]\" draggable=\"false\" data-src=\"holder.js/600x400/lava/auto/text:3/size:100\" data-holder-rendered=\"true\">";

    var choices = options_1 + options_2 + options_3;
    choices = "</div><div data-uk-slider='{center:true}'>\n" +
        "\n" +
        "    <div class=\"uk-slider-container\">\n" +
        "        <ul class=\"uk-slider\">\n" +
        "            <li>"+image_1+"</li>\n" +
        "            <li>"+image_2+"</li>\n" +
        "            <li>"+image_3+"</li>\n" +
        "        </ul>\n" +
        "    </div></div>\n" +
        "<a href=\"#\" class=\"uk-slidenav uk-slidenav-contrast uk-slidenav-previous\" data-uk-slider-item=\"previous\" draggable=\"false\"></a>" +
        "<a href=\"#\" class=\"uk-slidenav uk-slidenav-contrast uk-slidenav-previous\" data-uk-slider-item=\"previous\" draggable=\"false\"></a> \n" +
        "</div>\n";
    // choices = "<div data-uk-slider='{center:true}'>" +
    //     "<div class='uk-slider-container uk-flex-center'>" +
    //     "   <ul class='uk-slider uk-tile-small'>" +
    //     "       <li>"+ image_1+"</li>" +
    //     "       <li>"+ image_2+"</li>" +
    //     "   </ul>" +
    //     "</div></div>";
    $('#ava_board').html(choices);
}

function set_user_query(query) {
    $('#user-query').html(query);
}

function remove_login() {
    $('#btn-login').hide();
}
function set_ava_board(element){
    var action = element.action;
    switch (action){
        case 'login':
            $('#ava_board').html(login_form);
            break;
        case 'signup':
            $('#ava_board').html(signup_form);
            break;
        case 'ack':
            $('#ava_board').html(ack_form);
            set_ack_items(element.ack);
            set_nack_items(element.nack);
            break;
        case 'search_result':
            set_options_on_board(element.options);
            set_user_query(element.user_query);
            break;
        default:
            $('#ava_board').html(search_form);
            break;
    }
}