import Globals
import os.path

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())


from Products.ZenUtils.Utils import monkeypatch
from AccessControl import Permissions as permissions

@monkeypatch('Products.ZenModel.Device.Device')
def getTitle(self):
    return self.title
