# Copyright 2022 The Foundry Visionmongers Ltd
# SPDX-License-Identifier: Apache-2.0
"""
An OpenAssetIO ManagerPlugin that binds ftrack to the API.
"""

# It is important to minimise imports here. This module will be loaded
# when the plugin system scans for plugins. Postpone importing any
# of the actual implementation until it is needed by the
# PythonPluginSystemManagerPlugin's implementation.

from openassetio.pluginSystem import PythonPluginSystemManagerPlugin


class FtrackManagerPlugin(PythonPluginSystemManagerPlugin):
    """
    The ManagerPlugin is responsible for constructing instances of the
    manager's implementation of the OpenAssetIO interfaces and
    returning them to the host.
    """

    # pylint: disable=missing-docstring

    @staticmethod
    def identifier():
        return "com.ftrack"

    @classmethod
    def interface(cls):
        # pylint: disable=import-outside-toplevel
        from .FtrackInterface import FtrackInterface

        return FtrackInterface()


# Set the plugin class as the public entrypoint for the plugin system.
# A plugin is only considered if it exposes a `plugin` variable at this
# level, holding a class derived from PythonPluginSystemManagerPlugin.

# pylint: disable=invalid-name
plugin = FtrackManagerPlugin
