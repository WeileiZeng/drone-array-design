import bpy
from bpy_extras.io_utils import ImportHelper
from DroneLightShowAider import Aider

class ImportFileOperator(bpy.types.Operator, ImportHelper):
    bl_idname = 'import_file.csv_file'
    bl_label = 'Import'

    filename_ext = ".csv"
    aider = Aider.Instance()

    def execute(self, context):
        self.aider.initializeMatrixFromFile(self)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(ImportFileOperator)

def unregister():
    bpy.utils.unregister_class(ImportFileOperator)