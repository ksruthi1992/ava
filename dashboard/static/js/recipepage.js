$(document).ready(function() {
    //console.log("Hi");
    UIkit.modal('#modal-full').show();

});

$(document).on("click", "#modal-close", function (e) {
        e.preventDefault();
        console.log('sada');
        location.replace('/');
        console.log('asd')
        });