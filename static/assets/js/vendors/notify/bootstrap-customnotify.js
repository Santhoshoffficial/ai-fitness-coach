! function() {
    "use strict";

    function n(n, o = "Example notify") {
        $.notify({
            title: "",
            message: o,
            icon: "",
            url: "",
            target: "_blank"
        }, {
            element: "body",
            type: n,
            showProgressbar: !1,
            placement: {
                from: "top",
                align: "right"
            },
            offset: 20,
            spacing: 10,
            z_index: 1031,
            delay: 3300,
            timer: 1e3,
            url_target: "_blank",
            mouse_over: null,
            animate: {
                enter: "animated fadeInDown",
                exit: "animated fadeOutRight"
            },
            onShow: null,
            onShown: null,
            onClose: null,
            onClosed: null,
            icon_type: "class"
        })
    }
    window.primarynotify = function() {
        n("primary")
    }, window.secondarynotify = function() {
        n("secondary")
    }, window.successnotify = function() {
        n("success")
    }, window.infonotify = function() {
        n("info")
    }, window.warningnotify = function() {
        n("warning")
    }, window.dangernotify = function() {
        n("danger")
    }
}();
//# sourceMappingURL=bootstrap-customnotify.js.map