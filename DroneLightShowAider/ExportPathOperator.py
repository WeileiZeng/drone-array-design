import bpy
from bpy_extras.io_utils import ExportHelper
from DroneLightShowAider import Aider

class ExportPathOperator(bpy.types.Operator, ExportHelper):
    bl_idname = 'export.drone_light_show_path'
    bl_label = 'Export'

    filename_ext = ".PATH"
    aider = Aider.Instance()

    def execute(self, context):
        self.aider.exportPath(self)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(ExportPathOperator)

def unregister():
    bpy.utils.unregister_class(ExportPathOperator)