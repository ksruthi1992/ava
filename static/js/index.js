$(document).ready(function(){
        $mode = 0;
        $('.type-it').typeIt({
        strings: 'Hey there!'
        });

        $('#searchform').submit(function (event){
            event.preventDefault();
            $query = $('.field');
            $('.display').html($query.val());
            $('.type-it').typeIt({strings:'...', loop:true});

            $.ajax({
                type: "POST",
                url: "/respond/",
                data: {"query":$query.val(), "mode": $mode},
                success: function(data)
                {
                    $('.type-it').typeIt({
                        strings: data.response, speed:30,
                    });
                    $mode = data.mode;
                }
            });
            $query.val('');
        });
    });