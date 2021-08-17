#!/usr/bin/env python
# coding: utf-8

# Copyright (c) CERBSim.
# Distributed under the terms of the LGPLv2.1 License.

import json, os
package = json.load(open(os.path.join(os.path.dirname(__file__), "labextension", "package.json")))

__version__ = package["version"]
version_major, version_minor, version_patch = map(int, __version__.split('.'))
version_info = (version_major, version_minor, version_patch)

module_name = "webgui_jupyter_widgets"
module_version = __version__
