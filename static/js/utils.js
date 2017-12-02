
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
    var choices = options_1 + options_2 + options_3;
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