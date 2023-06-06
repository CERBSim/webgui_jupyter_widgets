#!/usr/bin/env python
# coding: utf-8

# Copyright (c) CERBSim.
# Distributed under the terms of the LGPLv2.1 License.

"""
TODO: Add module docstring
"""

from ipywidgets import DOMWidget
from traitlets import Unicode, Dict
from ._version import module_name, module_version
from . import html
import numpy as np
import os

#  from .webgui_js import version as webgui_version

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

class BaseWebGuiScene:
    def GenerateHTML(self, filename=None, template=None):
        self.encoding = 'b64'
        return html.GenerateHTML(self.GetData(), filename, template)

    def MakeScreenshot(self, filename, width=1200, height=600):
        self.encoding = 'b64'
        return html.MakeScreenshot(self.GetData(), filename, width, height)

    def Draw(self, width = None, height = None):
        from IPython.display import display
        from ipywidgets import Layout
        import os
        if width is None:
            width = "100%"
        if height is None:
            height = "500px" if "VSCODE_PID" in os.environ else "50vh"
        layout = Layout(width=width, height=height)
        self.widget = WebGuiWidget(layout=layout)
        self.encoding='binary'
        self.widget.value = self.GetData()
        display(self.widget)

    def Redraw(self):
        self.encoding='binary'
        self.widget.value = self.GetData(set_minmax=False)

    def __repr__(self):
        return "BaseWebGuiScene"


