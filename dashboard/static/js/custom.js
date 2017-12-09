$(document).ready(function() {
    //console.log("Hi");
    //alert("hello");
    $("#pantry").click(function () {
     // alert('here in');
        var user_id = get_user_id();
        var user_token = get_user_token();
        if(is_user_logged_in()) {
            $.ajax({
                type: 'GET',
                url: '/pantry/' + user_id + '/',
                beforeSend: function (req) {
                req.setRequestHeader('Authorization','Token '+ user_token);
            },

                success: function (msg) {
                    //alert(msg);
                    //code here to display items from pantry on screen
                    //alert((msg.element.ingredients));

                    var count = (msg.element.ingredients).length;
                   if(count>=0)
                   {

                       do
                       {
                       //alert(msg.element.ingredients);
                        //alert(count)
                       $("#"+msg.element.ingredients[count]).removeClass("btn-default");
                       $("#"+msg.element.ingredients[count]).addClass("btn-success active");
                       $("#"+msg.element.ingredients[count]).find('.state-icon').removeClass("glyphicon-unchecked");
                       $("#"+msg.element.ingredients[count]).find('.state-icon').addClass("glyphicon-check");
                        count--;
                       }while (count>=0)
                   }
                   else
                   {
                       alert("no elements present in user pantry");
                   }



                },
                error: function (req, status, error) {
                    console.log(req, status, error);
                }
            })
        }
        else
        {
            alert("I am in else");
        }

        $(function () {
            $('.button-checkbox').each(function () {
                //Do stuff when clicked
                // Settings

                var $widget = $(this),
                    $button = $widget.find('button'),
                    $checkbox = $widget.find('input:checkbox'),
                    color = $button.data('color'),
                    settings = {
                        on: {
                            icon: 'glyphicon glyphicon-check'
                        },
                        off: {
                            icon: 'glyphicon glyphicon-unchecked'
                        }
                    };


                    // Event Handlers
                    $button.on('click', function () {

                              $checkbox.prop('checked', !$checkbox.is(':checked'));
                              $checkbox.triggerHandler('change');
                              updateDisplay();



                    });

                $checkbox.on('change', function () {
                    updateDisplay();

                });

                // Actions
                function updateDisplay() {
                    var isChecked = $checkbox.is(':checked');

                    // Set the button's state
                    $button.data('state', (isChecked) ? "on" : "off");

                    // Set the button's icon
                    $button.find('.state-icon')
                        .removeClass()
                        .addClass('state-icon ' + settings[$button.data('state')].icon);

                    // Update the button's color
                    if (isChecked) {
                        $button
                            .removeClass('btn-default')
                            .addClass('btn-' + color + ' active');
                    }
                    else {
                        $button
                            .removeClass('btn-' + color + ' active')
                            .addClass('btn-default');
                    }
                }

        // Initialization
        function init() {

            updateDisplay();

            // Inject the icon if applicable
            if ($button.find('.state-icon').length == 0) {
                $button.prepend('<i class="state-icon ' + settings[$button.data('state')].icon + '"></i> ');
            }
        }

        init();


            });
        });



    // your code

document.getElementById('btntest').onclick = function(e) {
    e.preventDefault();

    var selchb = getSelectedChbox(this.form);     // gets the array returned by getSelectedChbox()
    console.log(selchb);
    var wrapper1= $("#parent");
        wrapper1.empty();
    if (is_user_logged_in()) {
        var user_id = get_user_id();
        var user_token = get_user_token();

        $.ajax({
            type: 'POST',
            beforeSend: function (req) {
                req.setRequestHeader('Authorization','Token '+ user_token);
            },
            url: '/pantry/' + user_id + '/',
            data:JSON.stringify({'ingredients': selchb}),
            success: function (msg) {
                //alert(msg);
            },
            error: function (req,status, error){
                console.log(req, status, error);
            }
        })
    }

}


function getSelectedChbox(frm) {

  var selchbox = [];

  //var inpfields = frm.getElementsByTagName('input');
  //var nr_inpfields = inpfields.length;

  // $.each($("button[type='button']"), function(){
  //               selchbox.push($(this).val());
  //
  //           });

    $.each($("input[type='checkbox']:checked"), function(){
                selchbox.push($(this).val());

            });


  // for(var i=0; i<nr_inpfields; i++) {
  //   if(inpfields[i].type == 'checkbox' && inpfields[i].checked == true) selchbox.push(inpfields[i].val());
  //
  // }
  return selchbox;
}





    });


      });



/*$(document).on('btntest','#pantry',function (e) {
    e.preventDefault();
    var selchb = getSelectedChbox(this.form);     // gets the array returned by getSelectedChbox()
    alert(selchb)
    $.ajax({
        url: '/pantry/',
        type: 'POST',
        data: {
            vegetable: $('#tomato').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),

        },
        success: function () {
            alert("Hello Anand");

        }
    })
}) */


//$('#onion').prop('checked', true);

