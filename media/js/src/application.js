'use strict';

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

// Angular app init.
(function() {

    var root = this;

    // App definition.
    var app = angular.module('Snipt', [], function($locationProvider) {
        $locationProvider.html5Mode(true);
    });

    // Use non-Django-style interpolation.
    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    });

    root.app = app;

    if (root.user_id) {
      root.mixpanel.identify(root.user_id);
      root.mixpanel.alias(root.user);
      root.mixpanel.people.set({
        $username: root.user,
        $email: root.user_email,
        $ip: root.user_ip
      });
    }

    if (root.location.pathname === '/account/stats/') {
      root.mixpanel.track('Viewing stats page');
    }
    if (root.location.pathname === '/pro/') {
      root.mixpanel.track('Viewing Pro page');
    }
    if (root.location.pathname === '/pro/signup/') {
      root.mixpanel.track('Viewing Pro signup page');
    }
    if (root.location.pathname === '/jobs/') {
      root.mixpanel.track('Viewing jobs page');
    }

    root.mixpanel.track_links('#hate-ads', '"Hate ads" link clicked');
    root.mixpanel.track_links('#post-job', '"Post a job" link clicked');
    root.mixpanel.track_links('a.download', 'Downloading snipt');

}).call(this);
