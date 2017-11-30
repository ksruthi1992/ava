$(document).ready(function() {
    //console.log("Hi");
    //alert("hello");
    $("#pantry").click(function()  {

        //alert('here in');
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
                   $.ajax({
        url: '/pantry/',
        type: 'GET',

        success: function (msg) {
            for ( i = 0;i<msg.length;i++) {
                alert(msg[i].ingredient_id)
            }
             //var inn = msg.names;
             //alert(inn);
             //$((inn)).prop('checked', true);
             //document.getElementById().prop('checked', true);
             //$($inn).prop('checked', true);
             //$('#onion').prop('checked', true);
        }
    })
        });
        $checkbox.on('change', function () {
            updateDisplay();
            $.ajax({
            url: '/pantry/',
            type: 'GET',

            success: function (msg) {
            var i;
            for ( i = 0;i<(msg).length;i++) {
                alert(msg[i].ingredient_id)
            }
             //var inn = msg.names;
             //alert(inn);
             //$((inn)).prop('checked', true);
             //document.getElementById().prop('checked', true);
             //$($inn).prop('checked', true);
             //$('#onion').prop('checked', true);
        }
    })
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
        });

var current_location = window.location.href ;

if(console.log(current_location)=="http://localhost:8000/ava-admin/");
     //alert("party");
     $(document).ready(function() {

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
      });

function getSelectedChbox(frm) {

  var selchbox = [];

  var inpfields = frm.getElementsByTagName('input');
  var nr_inpfields = inpfields.length;


  for(var i=0; i<nr_inpfields; i++) {
    if(inpfields[i].type == 'checkbox' && inpfields[i].checked == true) selchbox.push(inpfields[i].value);
  }
  return selchbox;
}

window.onload = function(){
    // your code

document.getElementById('btntest').onclick = function(e) {
    e.preventDefault();
    var selchb = getSelectedChbox(this.form);     // gets the array returned by getSelectedChbox()
      //alert(selchb)


    $.ajax({
        url: '/pantry/',
        type: 'POST',
        data: {
            //vegetable: $('#tomato').val(),
            pantry_items : selchb
        },
        success: function (msg) {
            alert(msg);

        }
    })
}
};
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
