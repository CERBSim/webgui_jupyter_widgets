#!/usr/bin/env python
# coding: utf-8

# Copyright (c) CERBSim.
# Distributed under the terms of the LGPLv2.1 License.

"""
Information about the frontend package of the widgets.
"""

module_name = "webgui_jupyter_widgets"
module_version = "^0.0.1"

import json, os
webgui_version = json.load(open(os.path.join(os.path.dirname(__file__), "labextension", "package.json")))['dependencies']['webgui']
