from girder_nwb import hookimpl


@hookimpl
def get_metadata(path):
    print("I am the visual coding metadata")


@hookimpl
def get_thumbnail(path):
    print("I am the visual coding thumbnail")
