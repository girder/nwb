import pytest

from girder.plugin import loadedPlugins


@pytest.mark.plugin('nwb')
def test_import(server):
    assert 'nwb' in loadedPlugins()
