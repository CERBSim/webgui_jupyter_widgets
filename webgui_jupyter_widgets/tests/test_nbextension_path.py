#!/usr/bin/env python
# coding: utf-8

# Copyright (c) CERBSim.
# Distributed under the terms of the LGPLv2.1 License.


def test_nbextension_path():
    # Check that magic function can be imported from package root:
    from webgui_jupyter_widgets import _jupyter_nbextension_paths
    # Ensure that it can be called without incident:
    path = _jupyter_nbextension_paths()
    # Some sanity checks:
    assert len(path) == 1
    assert isinstance(path[0], dict)
