import bpy

class Color_UL_CollectionList(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.label(text=str(index))
        layout.prop(item, "color")

def register():
    bpy.utils.register_class(Color_UL_CollectionList)

def unregister():
    bpy.utils.unregister_class(Color_UL_CollectionList)