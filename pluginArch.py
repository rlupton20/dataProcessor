import os
import sys

# Core

def findPlugins():
    folder = "/Plugins"
    path = os.path.dirname(os.path.realpath(__file__)) + folder
    pluginFiles = [p[:-3] for p in os.listdir(path) if p.endswith(".py")]
    sys.path.insert(0, path)
    for plugin in pluginFiles:
        print("Found plugin: ", __import__(plugin))

class MountPoint(type):
    def __init__(self, name, bases, attrs):
        if hasattr(self, 'plugins'):
            self.plugins.append(self)
        else:
             self.plugins = []

# Specific

class DataSetProcessor(metaclass=MountPoint):
    @classmethod
    def apply(cls, parent, dataset, **kwargs):
        if cls.signature == [True, True]:
            parent.addDataSet(cls.process(dataset))
        elif cls.signature == [False, True]:
            parent.addDataSet(cls.process())
        elif cls.signature == [True, False]:
            cls.process(dataset)
        elif cls.signature == [False, False]:
            cls.process()

class MenuItem(metaclass=MountPoint):
    pass
