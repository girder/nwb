import pluggy

hookspec = pluggy.HookspecMarker("girder_nwb")


@hookspec
def get_metadata(path):
    """Get metadata from an nwb file

    :param path: Path to an nwb file
    :return: Metadata in dictionary form
    """


@hookspec
def get_thumbnail(path):
    """Get a thumbnail for an nwb file

    :param path: Path to an nwb file
    :return: Thumbnail in png format
    """
