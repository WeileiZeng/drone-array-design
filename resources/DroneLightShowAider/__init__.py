bl_info = {
    "name" : "DroneLightShowAider",
    "author" : "mannix",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

modulesNames = [
    'Copy_To_Selected_Plus',
    'translations',
    'ColorCollectionItem',
    'Color_UL_CollectionList',
    'BrushCollection',
    'BrushCollectionList',
    'OBJECT_PT_DroneLightShowAider',
    'DroneLightShowAiderOperator',
    'DroneLightShowAiderDefaultProperty',
    'DroneLightShowAiderGlobalProperty',
    'ExportPathOperator',
    'ImportFileOperator']

import importlib
import sys

modulesFullNames = {}

for currentModuleName in modulesNames:
    if 'DEBUG_MODE' in sys.argv:
        modulesFullNames[currentModuleName] = ('{}'.format(currentModuleName))
    else:
        modulesFullNames[currentModuleName] = ('{}.{}'.format(__name__, currentModuleName))

for currentModuleFullName in modulesFullNames.values():
    if currentModuleFullName in sys.modules:
        importlib.reload(sys.modules[currentModuleFullName])
    else:
        globals()[currentModuleFullName] = importlib.import_module(currentModuleFullName)
        setattr(globals()[currentModuleFullName], 'modulesNames', modulesFullNames)

def register():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'register'):
                sys.modules[currentModuleName].register()

def unregister():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'unregister'):
                sys.modules[currentModuleName].unregister()

if __name__ == "__main__":
    register()