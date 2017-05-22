//
//  Global Javascript for Democracy Club website
//
var dClub = dClub || {};

// Mobile menu button: https://www.jamestease.co.uk/blether/add-remove-or-toggle-classes-using-vanilla-javascript
dClub.nav = (function() {
    function mobileMenuToggle() {

        document.querySelector('.js-nav-site-ctrl').addEventListener('click', function(e) {
            e.preventDefault();

            [].map.call(document.querySelectorAll('.js-nav-site'), function(el) {
                el.classList.toggle('nav-site--active');
            });
        });
    }

    return {
        mobileMenuToggle: mobileMenuToggle
    };
})();

// Check for Javscript support: https://www.jamestease.co.uk/blether/add-remove-or-toggle-classes-using-vanilla-javascript
dClub.helpers = (function() {
    function jsCheck() {

        var bodyClass = document.querySelector('html').classList;
        bodyClass.remove('no-js');
        bodyClass.add('js');
    }

    return {
        jsCheck: jsCheck
    };
})();


// Start functions
dClub.helpers.jsCheck();
dClub.nav.mobileMenuToggle();