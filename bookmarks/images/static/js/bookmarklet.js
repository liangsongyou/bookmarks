(function(){
    var jquery_version = '3.3.1';
    var site_url = 'http://127.0.0.1:8000/';
    var static_url = site_url + 'static/';
    var min_width = 100;
    var min_height = 100;

    function bookmarklet(msg) {

    }

    if (typeof window.jQuery != 'undefined') {
        bookmarklet();
    } else {
        var conflict = typeof windon.$ != 'undefined';
        var script = document.createElement('script');
        script.src = '//ajax.googleapis.com/ajax/libs/jquery/' +
                     jquery_version + '/jquery.min.js';
        document.head.appendChild(script);
        var attempts = 15;
        (function() {
            if (typeof window.jQuery == 'undefined') {
                if (--attempts > 0) {
                    window.setTimeout(arguments.callee, 250)
                } else {
                    alert('An error ocurred while loading jQuery')
                }
            } else {
                bookmarklet();
            }
        })();
    }
})()