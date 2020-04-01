# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Invenio-Record-Controller is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Module tests."""

from flask import Flask

from invenio_record_controller import InvenioRecordController


def test_version():
    """Test version import."""
    from invenio_record_controller import __version__
    assert __version__


def test_create():
    """Test extension initialization."""
    context = {
        "creator": 1,
    }
    controller.create(
        {"title": "authors"},
        **ctx
    )

def test_search():
    # linking ? prev/next/self
    controller.search(query="title:....", )

