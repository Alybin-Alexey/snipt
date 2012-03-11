var snipt = {
    module: function() {
        var modules = {};

        return function(name) {
            if (modules[name]) {
                return modules[name];
            }

            return modules[name] = {};
        };
    }()
};

jQuery(function($) {

    var SiteView = snipt.module('site').SiteView;
    window.site = new SiteView();

});
