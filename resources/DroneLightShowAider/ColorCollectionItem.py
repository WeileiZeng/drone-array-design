import bpy

class ColorCollectionItem(bpy.types.PropertyGroup):
    color: bpy.props.FloatVectorProperty(name="", default=(1.0, 1.0, 1.0), subtype="COLOR", min=0.0, max=1.0)

def register():
    bpy.utils.register_class(ColorCollectionItem)

def unregister():
    bpy.utils.unregister_class(ColorCollectionItem)
    