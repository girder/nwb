from girder import plugin
from girder import events

from girder_nwb.plugin_registry import get_plugin_manager


def nwb_handler(event):
    extensions = [i.lower() for i in event.info["file"]["exts"]]
    if "nwb" in extensions:
        plugin_manager = get_plugin_manager()
        plugin_manager.hook.get_metadata(path="foobar")
        plugin_manager.hook.get_thumbnail(path="foobar")
    return event


class GirderPlugin(plugin.GirderPlugin):
    DISPLAY_NAME = "NWB Viewer"
    CLIENT_SOURCE_PATH = "web_client"

    def load(self, info):
        events.bind(
            "model.file.finalizeUpload.after", "nwb_handler", nwb_handler
        )
