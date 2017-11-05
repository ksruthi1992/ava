(function($){
 $(document).ready(function(){
 var options = [];
        $mode = 0;
        $.ajax({
            type: "POST",
            url: "/respond/",
            data: {"title":$title.val()},
            success: function(data)
            {
                strings: data.response
                $mode = data.mode;
            }
        });
            $query.val('');
    }),
        $.ajax1({
            type: "POST",
            url: "/recipe/",
            data: {"description":$description.val()},
            success: function(data)
            {
                strings: data.response
                $mode = data.mode;
            }
        });
            $query.val('');
    }),
        $.ajax2({
            type: "POST",
            url: "/recipe/",
            data: {"time":$time.val()},
            success: function(data)
            {
                strings: data.response
                $mode = data.mode;
            }
        });
            $query.val('');
    }),
        $.ajax3({
            type: "POST",
            url: "/recipe/",
            data: {"serves":$serves.val()},
            success: function(data)
            {
                strings: data.response
                $mode = data.mode;
            }
        });
            $query.val('');
    }),
        $.ajax4({
            type: "POST",
            url: "/recipe/",
            data: {"ingredients":$ingredients.val()},
            success: function(data)
            {
                strings: data.response
                $mode = data.mode;
            }
        });
            $query.val('');
    }),
         $.ajax5({
            type: "POST",
            url: "/recipe/",
            data: {"directions":$directions.val()},
            success: function(data)
            {
                strings: data.response
                $mode = data.mode;
            }
        });
            $query.val('');
    });

    }
}