(function($){
 $(document).ready(function(){
 var options = [];
        $mode = 0;
        var response = {
            "title":"Pasta",
            "ingredients":["tomatoes", "cheese"],
            "serves":4,
            "directions":{
                "1":"boil pasta",
                "2":"cook tomatoes"
            },

        };
        $.ajax({
            type: "GET",
            url: "/getRecipe/",
            data: {"recipe_id":12},
            success: function(data)
            {
                $('.title').html(response.title);
                $('.image').html(response.image);
                $('.description').html(response.description);
                $('.time').html(response.time);
                $('.serves').html(response.serves);
                $('.ingredients').html(response.ingredients);
                $('.directions').html(response.directions);
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

     })


}