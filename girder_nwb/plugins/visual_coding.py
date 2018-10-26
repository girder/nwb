from girder_nwb.config import hookimpl


@hookimpl
def get_metadata(path):
    print("I am the visual coding metadata")


@hookimpl
def get_thumbnail(path):
    print("I am the visual coding thumbnail")
