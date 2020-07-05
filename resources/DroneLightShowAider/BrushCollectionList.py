import bpy

class BrushCollectionList(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        split = layout.split(factor=0.08)
        split.label(text=str(index))
        
        row = split.row(align=True)
        o = row.operator("object.drone_light_show_aider_operator", text="Assign Drones")
        o.cmd = "Assign Drones"
        o.brush_collection_item_index = index

        o = row.operator("object.drone_light_show_aider_operator", text="Show Drones")
        o.cmd = "Show Drones"
        o.brush_collection_item_index = index

        row = split.row(align=True)
        o = row.operator("object.drone_light_show_aider_operator", text="Assign Brushes")
        o.cmd = "Assign Brushes"
        o.brush_collection_item_index = index

        o = row.operator("object.drone_light_show_aider_operator", text="Show Brushes")
        o.cmd = "Show Brushes"
        o.brush_collection_item_index = index

        # split.prop(item, "keep_color")

def register():
    bpy.utils.register_class(BrushCollectionList)

def unregister():
    bpy.utils.unregister_class(BrushCollectionList)