import bpy

class DroneLightShowAiderDefaultProperty(bpy.types.PropertyGroup):
    number_drone: bpy.props.IntProperty(name="Number Of Drone", min=1, soft_min=1, default=10)

    diffuse_color: bpy.props.StringProperty(default='')
    vertices_location: bpy.props.StringProperty(default='')

def register():
    bpy.utils.register_class(DroneLightShowAiderDefaultProperty)

    bpy.types.Object.DroneLightShowAiderDefaultProperty = bpy.props.PointerProperty(type=DroneLightShowAiderDefaultProperty)

def unregister():
    bpy.utils.unregister_class(DroneLightShowAiderDefaultProperty)

    del bpy.types.Object.DroneLightShowAiderDefaultProperty