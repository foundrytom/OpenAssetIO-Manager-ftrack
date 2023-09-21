# Copyright 2022 The Foundry Visionmongers Ltd
# SPDX-License-Identifier: Apache-2.0
"""
A manager test harness test case suite that validates that the
Ftrack plugin behaves with the correct business logic.
"""

# pylint: disable=invalid-name, missing-function-docstring

from unittest import mock

from openassetio.test.manager import harness

import ftrack_api

__all__ = []


class Test_initialize_credentials(harness.FixtureAugmentedTestCase):
    """
    Test the handling of settings .vs. env vars for session
    initialization.
    """

    def test_when_settings_not_set_then_uses_env_values(self):
        expected_url = "env_SERVER"
        expected_key = "env_API_KEY"
        expected_user = "env_API_USER"
        with mock.patch.dict(
            "os.environ",
            {
                "FTRACK_SERVER": expected_url,
                "FTRACK_API_USER": expected_user,
                "FTRACK_API_KEY": expected_key,
            },
        ):

            with mock.patch.object(ftrack_api, "Session") as mocked_session:
                self._manager.initialize({})
                mocked_session.assert_called_once_with(
                    server_url=expected_url,
                    api_key=expected_key,
                    api_user=expected_user,
                )

    def test_when_settings_set_then_uses_settings_values(self):
        expected_url = "settings_SERVER"
        expected_key = "settings_API_KEY"
        expected_user = "settings_API_USER"
        with mock.patch.object(ftrack_api, "Session") as mocked_session:
            self._manager.initialize(
                {
                    "server_url": expected_url,
                    "api_key": expected_key,
                    "api_user": expected_user,
                }
            )
            mocked_session.assert_called_once_with(
                server_url=expected_url, api_key=expected_key, api_user=expected_user
            )
