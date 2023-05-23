// Entry point for the notebook bundle containing custom model definitions.
//
define(function() {
    "use strict";

    window['requirejs'].config({
        map: {
            '*': {
                'webgui_jupyter_widgets': 'nbextensions/webgui_jupyter_widgets/index',
                'webgui': 'nbextensions/webgui_jupyter_widgets/webgui',
            },
        }
    });
    // Export the required load_ipython_extension function
    return {
        load_ipython_extension : function() {}
    };
});
