#!/usr/bin/env python
# coding: utf-8

# Copyright (c) CERBSim.
# Distributed under the terms of the LGPLv2.1 License.

import json, os
package = json.load(open(os.path.join(os.path.dirname(__file__), "labextension", "package.json")))

__version__ = package["version"]
from packaging.version import parse as _parse
v = _parse(__version__)
version_major, version_minor, version_patch = v.major, v.minor, v.micro
version_info = (version_major, version_minor, version_patch)

module_name = "webgui_jupyter_widgets"
module_version = __version__
