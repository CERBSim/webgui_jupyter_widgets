from . import code, widget_code
if __name__ == '__main__':
    import sys, os
    open(os.path.join(sys.argv[1], 'webgui.js'), 'w').write(code)
    open(os.path.join(sys.argv[1], 'webgui_jupyter_widgets.js'), 'w').write(widget_code)
