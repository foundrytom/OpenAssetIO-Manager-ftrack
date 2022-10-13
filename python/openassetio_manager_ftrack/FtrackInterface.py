# Copyright 2022 The Foundry Visionmongers Ltd
# SPDX-License-Identifier: Apache-2.0
"""
An implementation of the openassetio.managerApi.ManagerInterface that
bridges to the ftrack Python api.
"""

from openassetio import constants, TraitsData
from openassetio.managerApi import ManagerInterface

# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments,unused-argument,invalid-name

REFERENCE_PREFIX = "ftrack://"


class FtrackInterface(ManagerInterface):
    def identifier(self):
        return "com.ftrack"

    def displayName(self):
        return "ftrack"

    def info(self):
        return {constants.kField_EntityReferencesMatchPrefix: REFERENCE_PREFIX}

    def initialize(self, managerSettings, hostSession):
        pass

    def managementPolicy(self, traitSets, context, hostSession):
        # Ignore everything for now
        return [TraitsData() for _ in traitSets]

    def isEntityReferenceString(self, someString, hostSession):
        return someString.startswith(self.__reference_prefix)
