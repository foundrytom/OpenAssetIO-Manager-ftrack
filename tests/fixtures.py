# Copyright 2022 The Foundry Visionmongers Ltd
# SPDX-License-Identifier: Apache-2.0
"""
Manager test harness test case fixtures for the ftrack manager plugin.
"""
from openassetio.constants import kField_EntityReferencesMatchPrefix


IDENTIFIER = "com.ftrack"

fixtures = {
    "identifier": IDENTIFIER,
    "Test_identifier": {"test_matches_fixture": {"identifier": IDENTIFIER}},
    "Test_displayName": {"test_matches_fixture": {"display_name": "ftrack"}},
    "Test_info": {
        "test_matches_fixture": {"info": {kField_EntityReferencesMatchPrefix: "ftrack://"}}
    },
}
