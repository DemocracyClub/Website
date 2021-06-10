//
//  Global Javascript for Democracy Club website
//

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