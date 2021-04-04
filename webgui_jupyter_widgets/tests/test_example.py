#!/usr/bin/env python
# coding: utf-8

# Copyright (c) CERBSim.
# Distributed under the terms of the LGPLv2.1 License.

import pytest

from ..example import ExampleWidget


def test_example_creation_blank():
    w = ExampleWidget()
    assert w.value == 'Hello World'
