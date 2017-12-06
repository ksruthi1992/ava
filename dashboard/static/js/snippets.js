
var simple_form = "<div>\n" +
                    "    <form id=\"simpleform\">\n" +
                    "        <span class=\"uk-search-icon-flip\" uk-search-icon></span>\n" +
                    "        <input  type=\"search\" placeholder=\"eg. spicy lasagne\" autofocus>\n" +
                    "    </form>\n" +
                    "</div>";
var search_form = "<div class=\"uk-margin-top horizontal uk-nav-center\">\n" +
            "    <form class=\"uk-search uk-search-default\" id=\"searchform\">\n" +
            "        <span class=\"uk-search-icon-flip\" uk-search-icon></span>\n" +
            "        <input class=\"uk-input\" type=\"search\" placeholder=\"eg. spicy lasagne\" id='user-query' autofocus>\n" +
            "    </form>\n" +
            "</div>";

var login_form = "<div class=\"horizontal uk-nav-center login-form\" >\n" +
    "    <h3 class=\"uk-card-title\"></h3>\n" +
    "    <form id=\"login-form\">\n" +
    "        <div class=\"uk-margin\">\n" +
    "            <div class=\"uk-inline\">\n" +
    "                <span class=\"uk-form-icon\" uk-icon=\"icon: user\"></span>\n" +
    "                <input id='email' class=\"uk-input\" type=\"email\" placeholder=\"Email\" autofocus>\n" +
    "            </div>\n" +
    "        </div>\n" +
    "\n" +
    "        <div class=\"uk-margin\">\n" +
    "            <div class=\"uk-inline\">\n" +
    "                <span class=\"uk-form-icon\" uk-icon=\"icon: lock\"></span>\n" +
    "                <input id='password' class=\"uk-input\" type=\"password\" placeholder=\"Password\">\n" +
    "            </div>\n" +
    "        </div>\n" +
    "\n" +
    "        <div class=\"uk-margin uk-nav-center\">\n" +
    "            <div class=\"uk-inline\">\n" +
    "                <button class=\"uk-button uk-button-default\">Login</button>\n" +
    "            </div>\n" +
    "        </div>\n" +
    "\n" +
    "    </form>\n" +
    "</div>";

var signup_form = "<div class=\"horizontal uk-nav-center login-form\" >\n" +
    "    <h3 class=\"uk-card-title\"></h3>\n" +
    "    <form id=\"signup-form\">\n" +
    "        <div class=\"uk-margin\">\n" +
    "            <div class=\"uk-inline\">\n" +
    "                <span class=\"uk-form-icon\" uk-icon=\"icon: user\"></span>\n" +
    "                <input id='email' class=\"uk-input\" type=\"email\" placeholder=\"Email\" autofocus>\n" +
    "            </div>\n" +
    "        </div>\n" +
    "\n" +
    "        <div class=\"uk-margin\">\n" +
    "            <div class=\"uk-inline\">\n" +
    "                <span class=\"uk-form-icon\" uk-icon=\"icon: lock\"></span>\n" +
    "                <input id='username' class=\"uk-input\" type=\"text\" placeholder=\"Username\">\n" +
    "            </div>\n" +
    "        </div>\n" +
    "\n" +
    "        <div class=\"uk-margin\">\n" +
    "            <div class=\"uk-inline\">\n" +
    "                <span class=\"uk-form-icon\" uk-icon=\"icon: lock\"></span>\n" +
    "                <input id='password' class=\"uk-input\" type=\"password\" placeholder=\"Password\">\n" +
    "            </div>\n" +
    "        </div>\n" +
    "\n" +
    "        <div class=\"uk-margin\">\n" +
    "            <div class=\"uk-inline\">\n" +
    "                <span class=\"uk-form-icon\" uk-icon=\"icon: lock\"></span>\n" +
    "                <input id='conf_password' class=\"uk-input\" type=\"password\" placeholder=\"Confirm Password\">\n" +
    "            </div>\n" +
    "        </div>\n" +
    "\n" +
    "        <div class=\"uk-margin uk-nav-center\">\n" +
    "            <div class=\"uk-inline\">\n" +
    "                <button id='btn_signup' class=\"uk-button uk-button-default\">Signup</button>\n" +
    "            </div>\n" +
    "        </div>\n" +
    "\n" +
    "    </form>\n" +
    "</div>";

var nav_user = "<a href=#><img src='"+ default_user_image +"' id='nav-user-image' class='uk-border-circle uk-responsive-width uk-responsive-height nav-user-image' alt='Cinque Terre'></a>\n" +
    "<div class='uk-navbar-dropdown nav-user-dropdown'>\n" +
    "    <ul class='uk-nav uk-navbar-dropdown-nav'>\n" +
    "        <li><a href='#' id='user_profile'>Profile</a></li>\n" +
    "        <li><a href='#' id='user_settings'>Settings</a></li>\n" +
    "        <li class='uk-nav-divider'></li>\n" +
    "        <li><a href='#' onclick='logout(); return false;' id='logout'>Logout</a></li>\n" +
    "    </ul>\n" +
    "</div>";

var ack_form = "<div class=\" horizontal uk-nav-center\">\n" +
    "    <button id='btn-ack' class=\"uk-button uk-button-default\" autofocus>Yes</button> \n" +
    "    <button id='btn-nack' class=\"uk-margin-left uk-button uk-button-default\">No</button>\n" +
    "</div>\n";