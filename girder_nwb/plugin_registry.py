import pluggy
import hookspecs


from girder_nwb.plugins import visual_behavior
from girder_nwb.plugins import visual_coding


def register_plugins(plugin_manager):
    plugin_manager.add_hookspecs(hookspecs)
    plugin_manager.register(visual_behavior)
    plugin_manager.register(visual_coding)
    plugin_manager.load_setuptools_entrypoints("girder_nwb")


def get_plugin_manager():
    plugin_manager = pluggy.PluginManager("girder_nwb")
    register_plugins(plugin_manager)
    return plugin_manager
