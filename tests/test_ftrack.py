# Copyright 2022 The Foundry Visionmongers Ltd
# SPDX-License-Identifier: Apache-2.0
"""
Test cases for the ftrack manager plugin that make use of the OpenAssetIO
manager test harness.

Note that this file simply wraps the openassetio.test.manager harness in
a pytest test, so that it can be run as part of the project test suite.
It also serves as an example of how to programmatically execute the test
harness, by extending it with additional checks for ftrack's specific
business logic.

It is not required in order to make use of the test harness. The base
API compliance tests can simply be run from a command line with
openassetio available, and the target plugin on
$OPENASSETIO_PLUGIN_PATH:

  python -m openassetio.test.manager -f path/to/fixtures.py
"""

import os
import pytest

# pylint: disable=invalid-name,redefined-outer-name
# pylint: disable=missing-class-docstring,missing-function-docstring
# pylint: disable=too-few-public-methods

from openassetio.test.manager import harness, apiComplianceSuite


#
# Tests
#


class Test_ftrack_openassetio_plugin:
    def test_passes_apiComplianceSuite(self, harness_fixtures):
        assert harness.executeSuite(apiComplianceSuite, harness_fixtures)


@pytest.fixture(autouse=True)
def ftrack_plugin_env(base_dir, monkeypatch):
    """
    Provides a modified environment with the ftrack plugin on the
    OpenAssetIO search path.
    """
    plugin_dir = os.path.join(base_dir, "python")
    monkeypatch.setenv("OPENASSETIO_PLUGIN_PATH", plugin_dir)


@pytest.fixture
def harness_fixtures(base_dir):
    """
    Provides the fixtures dict for the ftrack plugin when used with the
    openassetio.test.manager.apiComplianceSuite.
    """
    fixtures_path = os.path.join(base_dir, "tests", "fixtures.py")
    return harness.fixturesFromPyFile(fixtures_path)


@pytest.fixture
def base_dir():
    """
    Provides the path to the base directory for the ftrack plugin
    codebase.
    """
    return os.path.dirname(os.path.dirname(__file__))
