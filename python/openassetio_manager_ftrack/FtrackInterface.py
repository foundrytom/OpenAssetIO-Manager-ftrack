# Copyright 2022 The Foundry Visionmongers Ltd
# SPDX-License-Identifier: Apache-2.0
"""
An implementation of the openassetio.managerApi.ManagerInterface that
bridges to the ftrack Python api.
"""

import os

from openassetio import constants, TraitsData
from openassetio.managerApi import ManagerInterface

# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments,unused-argument,invalid-name

REFERENCE_PREFIX = "ftrack://"

SETTINGS_KEY_SERVER = "server_url"
SETTINGS_KEY_API_KEY = "api_key"
SETTINGS_KEY_API_USER = "api_user"


class FtrackInterface(ManagerInterface):

    def __init__(self):
        super().__init__()
        self.__settings = {}
        self.__session = None

    def __del__(self):
        if self.__session:
            self.__session.close()

    def identifier(self):
        return "com.ftrack"

    def displayName(self):
        return "ftrack"

    def info(self):
        # As we use a simple prefix, allow the OpenAssetIO C++ layer to
        # short-circuit calls into Python for isEntityReferenceString
        # where possible.
        info = {constants.kInfoKey_EntityReferencesMatchPrefix: REFERENCE_PREFIX}
        # Add any relevant server info if we have a session.
        if self.__session:
            if "version" in self.__session.server_information:
                info["version"] = self.__session.server_information["version"]
        return info

    def settings(self, hostSession):
        # Settings should always be a copy to avoid accidental updates
        return self.__settings.copy()

    def initialize(self, managerSettings, hostSession):
        if self.__session:
            self.__session.close()
        self.__validate_settings(managerSettings)
        self.__settings.update(managerSettings)
        self.__session = self.__create_session(self.__settings, hostSession)

    def managementPolicy(self, traitSets, access, context, hostSession):
        # Ignore everything for now
        return [TraitsData() for _ in traitSets]

    def isEntityReferenceString(self, someString, hostSession):
        return someString.startswith(self.__reference_prefix)

    @staticmethod
    def __validate_settings(managerSettings):
        """
        Ensures settings only contain valid keys, raising if not.
        (required by OpenAssetIO API contract)
        """
        valid_keys = {SETTINGS_KEY_SERVER, SETTINGS_KEY_API_USER, SETTINGS_KEY_API_KEY}
        for key, value in managerSettings.items():
            if key not in valid_keys:
                raise KeyError(f"Unrecognised setting '{key}'")
            if not isinstance(value, str):
                raise ValueError(f"Invalid type for setting '{key}' must be a string")

    @staticmethod
    def __create_session(settings, hostSession):
        """
        Creates and returns a new ftrack API session, using
        configuration from the environment if specific values are
        missing from the supplied settings.
        """
        logger = hostSession.logger()

        # We defer this to avoid any heavy lifting when
        # the interface is constructed, but not yet
        # initialized (e.g. to present in a UI selector).
        # pylint: disable=import-outside-toplevel
        import ftrack_api

        server_url = settings.get(SETTINGS_KEY_SERVER, os.environ.get("FTRACK_SERVER"))
        api_key = settings.get(SETTINGS_KEY_API_KEY, os.environ.get("FTRACK_API_KEY"))
        api_user = settings.get(
            SETTINGS_KEY_API_USER, os.environ.get("FTRACK_API_USER")
        )

        logger.debug(f"Creating session for '{api_user}' on server '{server_url}'...")

        session = ftrack_api.Session(
            server_url=server_url, api_key=api_key, api_user=api_user
        )
        session.check_server_compatibility()

        logger.debug(
            "Session created sucessfully "
            f"[server version: {session.server_information['version']}]"
        )

        return session
