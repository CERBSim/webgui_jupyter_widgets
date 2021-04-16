#!/usr/bin/env python
# coding: utf-8

# Copyright (c) CERBSim.
# Distributed under the terms of the LGPLv2.1 License.

"""
TODO: Add module docstring
"""

from IPython.display import display
from ipywidgets import DOMWidget
from traitlets import Unicode, Dict
from ._version import module_name, module_version, webgui_version
import numpy as np
import os

try:
    __IPYTHON__
    _IN_IPYTHON = True
except NameError:
    _IN_IPYTHON = False

try:
    import google.colab
    _IN_GOOGLE_COLAB = True
except ImportError:
    _IN_GOOGLE_COLAB = False


class WebGuiWidget(DOMWidget):
    """TODO: Add docstring here
    """
    _model_name = Unicode('WebguiModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('WebguiView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    value = Dict({}).tag(sync=True)

class WebGuiDocuWidget(DOMWidget):
    """Widget for exported HTML files in documentation (actual 3d vis code and data is loaded after click on preview image)
    """
    _model_name = Unicode('WebguiModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('WebguiDocuView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    value = Dict({}).tag(sync=True)

def encodeData( array ):
    from base64 import b64encode
    values = np.array(array.flatten(), dtype=np.float32)
    res = b64encode(values).decode("ascii")
    return res

_html_template = """
<!DOCTYPE html>
<html>
    <head>
        <title>NGSolve WebGUI</title>
        <meta name='viewport' content='width=device-width, user-scalable=no'/>
        <style>
            body{
                margin:0;
                overflow:hidden;
            }
            canvas{
                cursor:grab;
                cursor:-webkit-grab;
                cursor:-moz-grab;
            }
            canvas:active{
                cursor:grabbing;
                cursor:-webkit-grabbing;
                cursor:-moz-grabbing;
            }
        </style>
    </head>
    <body>
          <script src="https://unpkg.com/webgui@{{webgui_version}}/dist/webgui.js"></script>
          <script>
            {render}

            const scene = new webgui.Scene();
            scene.init(document.body, render_data, {preserveDrawingBuffer: false});
          </script>
    </body>
</html>
""".replace("{{webgui_version}}", webgui_version)
_screenshot_html_template = _html_template.replace("preserveDrawingBuffer: false", "preserveDrawingBuffer: true")

class BaseWebGuiScene:
    def GenerateHTML(self, filename=None, template=_html_template):
        import json
        d = self.GetData()

        data = json.dumps(d)

        html = template.replace('{data}', data )
        jscode = "var render_data = {}\n".format(data)
        html = html.replace('{render}', jscode )

        if filename is not None:
            open(filename,'w').write( html )
        return html

    def MakeScreenshot(self, filename, width=1200, height=600):
        html_file = filename+".html"
        self.GenerateHTML(html_file, _screenshot_html_template)

        # start headless browser to render html
        from selenium import webdriver
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        # https://stackoverflow.com/questions/54297559/getting-cannot-activate-web-view
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-browser-side-navigation")
        #options.add_argument("--disable-gpu")
        options.add_argument("--disable-features=VizDisplayCompositor")

        options.add_argument('window-size=1200x600')


        driver = webdriver.Chrome(options=options)
        fpath = 'file://'+os.path.join(os.path.abspath('.'), html_file)
        driver.get(fpath)
        driver.implicitly_wait(10)

        import time
        time.sleep(2)
        driver.get_screenshot_as_file(filename)
        os.remove(html_file)


    def Draw(self):
        self.widget = WebGuiWidget()
        self.widget.value = self.GetData()
        display(self.widget)

    def Redraw(self):
        self.widget.value = self.GetData(set_minmax=False)

    def __repr__(self):
        return "BaseWebGuiScene"


