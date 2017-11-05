(function($){
$(document).ready(function(){
var options = [];

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

$('#cssmenu li.active').addClass('open').children('ul').show();
	$('#cssmenu li.has-sub>a').on('click', function(){
		$(this).removeAttr('href');

		var element = $(this).parent('li');
		if (element.hasClass('open')) {
			element.removeClass('open');
			element.find('li').removeClass('open');
			element.find('ul').slideUp(200);
		}
		else {
			element.addClass('open');
			element.children('ul').slideDown(200);
			element.siblings('li').children('ul').slideUp(200);
			element.siblings('li').removeClass('open');
			element.siblings('li').find('li').removeClass('open');
			element.siblings('li').find('ul').slideUp(200);
		}
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


});
})(jQuery);