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


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = InvenioRecordController(app)
    assert 'invenio-record-controller' in app.extensions

    app = Flask('testapp')
    ext = InvenioRecordController()
    assert 'invenio-record-controller' not in app.extensions
    ext.init_app(app)
    assert 'invenio-record-controller' in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert 'Welcome to Invenio-Record-Controller' in str(res.data)
