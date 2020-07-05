import bpy
from bpy.types import Menu


class WM_OT_Copy_To_Selected_Plus(bpy.types.Operator):
    bl_idname = "wm.copy_to_selected_plus"
    bl_label = "Copy To Selected+"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        active_strip = None
        other = []
            
        for o in bpy.data.objects:
            if o.animation_data:
                for track in o.animation_data.nla_tracks:
                    for strip in track.strips:
                        if strip.active:
                            active_strip = strip
                        elif strip.select:
                            other.append(strip)
                            
            if o.active_material and o.active_material.animation_data:
                for track in o.active_material.animation_data.nla_tracks:
                    for strip in track.strips:
                        if strip.active:
                            active_strip = strip
                        elif strip.select:
                            other.append(strip)

        if active_strip:
            for o in other:
                if context.button_prop.name == "Repeat":
                    o.repeat = active_strip.repeat
                elif context.button_prop.name == "Scale":
                    o.scale = active_strip.scale
                elif context.button_prop.name == "Action Start Frame":
                    o.action_frame_start = active_strip.action_frame_start
                elif context.button_prop.name == "Action End Frame":
                    o.action_frame_end = active_strip.action_frame_end


        return {'FINISHED'}


# This class has to be exactly named like that to insert an entry in the right click menu
class WM_MT_button_context(Menu):
    bl_label = "Unused"

    def draw(self, context):
        pass


def menu_func(self, context):
    if context.area.type == "NLA_EDITOR":
        
        if context.button_prop.name == "Repeat" or \
           context.button_prop.name == "Scale" or \
           context.button_prop.name == "Action Start Frame" or \
           context.button_prop.name == "Action End Frame":
            layout = self.layout
            layout.separator()
            layout.operator(WM_OT_Copy_To_Selected_Plus.bl_idname)
    


classes = (
    WM_OT_Copy_To_Selected_Plus,
    WM_MT_button_context,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.WM_MT_button_context.append(menu_func)


def unregister():
    bpy.types.WM_MT_button_context.remove(menu_func)
    for cls in classes:
        bpy.utils.unregister_class(cls)
    

