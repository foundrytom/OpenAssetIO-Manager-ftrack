# Copyright 2022 The Foundry Visionmongers Ltd
# SPDX-License-Identifier: Apache-2.0
"""
Manager test harness test case fixtures for the ftrack manager plugin.
"""
from openassetio import constants

import ftrack_api

IDENTIFIER = "com.ftrack"

# For now, we assume tests use the env vars to determine which
# server to test against. Determine the server versions so we
# can correctly validate the `info` response.
session = ftrack_api.Session()
server_version = session.server_information["version"]
session.close()

fixtures = {
    "identifier": IDENTIFIER,
    "Test_identifier": {"test_matches_fixture": {"identifier": IDENTIFIER}},
    "Test_displayName": {"test_matches_fixture": {"display_name": "ftrack"}},
    "Test_info": {
        "test_matches_fixture": {
            "info": {
                constants.kInfoKey_EntityReferencesMatchPrefix: "ftrack://",
                "version": server_version,
            }
        }
    },
    "Test_initialize": {
        "shared": {
            "some_settings_with_new_values_and_invalid_keys": {
                "server_url": "",
                "cat": True,
            }
        },
        "test_when_settings_expanded_then_manager_settings_updated": {
            "some_settings_with_all_keys": {
                "api_key": "a key",
                "api_user": "a user",
                "server_url": "https://server",
            }
        },
        "test_when_subset_of_settings_modified_then_other_settings_unchanged": {
            "some_settings_with_a_subset_of_keys": {"api_user": "a user"}
        },
    },
}
