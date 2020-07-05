import bpy

class BrushCollection(bpy.types.PropertyGroup):
    keep_color: bpy.props.BoolProperty(name="keep color", default=False)
    drones: bpy.props.StringProperty()
    brushes = bpy.props.StringProperty()

def register():
    bpy.utils.register_class(BrushCollection)

def unregister():
    bpy.utils.unregister_class(BrushCollection)
    