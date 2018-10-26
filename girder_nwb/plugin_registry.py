import importlib

import pluggy
import hookspecs


default_plugins = ("visual_behavior", "visual_coding")


def register_plugins(plugin_manager):
    plugin_manager.add_hookspecs(hookspecs)
    for i in default_plugins:
        plugin = importlib.import_module(".{}".format(i), package="girder_nwb.plugins")
        plugin_manager.register(plugin)
    plugin_manager.load_setuptools_entrypoints("girder_nwb")


def get_plugin_manager():
    plugin_manager = pluggy.PluginManager("girder_nwb")
    register_plugins(plugin_manager)
    return plugin_manager
