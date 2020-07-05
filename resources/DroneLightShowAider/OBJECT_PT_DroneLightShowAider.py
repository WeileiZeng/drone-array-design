import bpy

class OBJECT_PT_DroneLightShowAider(bpy.types.Panel):
    bl_label = "Drone Light Show Aider"
    bl_idname = "OBJECT_PT_DroneLightShowAider"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"
    
    def draw(self, context):
        props = context.object.DroneLightShowAiderDefaultProperty
        props_g = context.scene.DroneLightShowAiderGlobalProperty
        
        layout = self.layout

        # global properties
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        if context.scene.showGlobalPropertiesPanel:
            row.prop(context.scene, "showGlobalPropertiesPanel", icon="DISCLOSURE_TRI_DOWN", text="", emboss=False)
        else:
            row.prop(context.scene, "showGlobalPropertiesPanel", icon="DISCLOSURE_TRI_RIGHT", text="", emboss=False)
        row.label(text="global properties")

        if context.scene.showGlobalPropertiesPanel:
            col.prop(props_g, "drone_radius")
            col.prop(props_g, "min_distance")
            # col.prop(props_g, "max_velocity")
            col.prop(props_g, "light_strength")

        # initialize matrix
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        if context.scene.showInitializeMatrixPanel:
            row.prop(context.scene, "showInitializeMatrixPanel", icon="DISCLOSURE_TRI_DOWN", text="", emboss=False)
        else:
            row.prop(context.scene, "showInitializeMatrixPanel", icon="DISCLOSURE_TRI_RIGHT", text="", emboss=False)
        row.label(text="initialize matrix")

        if context.scene.showInitializeMatrixPanel:
            row = col.row(align=True)
            row.prop(props_g, "num_x")
            row.prop(props_g, "num_y")
            row.prop(props_g, "spacing")
            split = col.split(factor=0.3)
            split.prop(props_g, "use_sphere")
            split.operator("object.drone_light_show_aider_operator", text="Generate Matrix").cmd = "Initialize Matrix"
            split = col.split(factor=0.3)
            split.prop(props_g, "use_height")
            split.operator("object.drone_light_show_aider_operator", text="Generate Matrix From File").cmd = "Initialize Matrix From File"
            # col.operator("object.drone_light_show_aider_operator", text="Clear Matrix").cmd = "Clear Matrix"
            col.operator("object.drone_light_show_aider_operator", text="Select Objects as Initial Matrix").cmd = "Select Objects as Initial Matrix"
            col.operator("object.drone_light_show_aider_operator", text="Select Drones to Show").cmd = "Select Drones to Show"


        

        # auto add drones to curve
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        if context.scene.showAutoAddDronesToCurvePanel:
            row.prop(context.scene, "showAutoAddDronesToCurvePanel", icon="DISCLOSURE_TRI_DOWN", text="", emboss=False)
        else:
            row.prop(context.scene, "showAutoAddDronesToCurvePanel", icon="DISCLOSURE_TRI_RIGHT", text="", emboss=False)
        row.label(text="auto add drones to curve")

        if context.scene.showAutoAddDronesToCurvePanel:
            row = col.row()
            row.prop(props, "number_drone")
            row.operator("object.drone_light_show_aider_operator", text="Apply").cmd = "Add Drones to Curve"
        
        # auto add drones to mesh
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        if context.scene.showAutoAddDronesToMeshPanel:
            row.prop(context.scene, "showAutoAddDronesToMeshPanel", icon="DISCLOSURE_TRI_DOWN", text="", emboss=False)
        else:
            row.prop(context.scene, "showAutoAddDronesToMeshPanel", icon="DISCLOSURE_TRI_RIGHT", text="", emboss=False)
        row.label(text="auto add drones to mesh")

        if context.scene.showAutoAddDronesToMeshPanel:
            row = col.row()
            row.prop(props_g, "set_parent")
            row.operator("object.drone_light_show_aider_operator", text="Apply").cmd = "Add Drones to Mesh"
        
        # operator
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        if context.scene.showOperatorPanel:
            row.prop(context.scene, "showOperatorPanel", icon="DISCLOSURE_TRI_DOWN", text="", emboss=False)
        else:
            row.prop(context.scene, "showOperatorPanel", icon="DISCLOSURE_TRI_RIGHT", text="", emboss=False)
        row.label(text="operator")

        if context.scene.showOperatorPanel:
            col.operator("object.drone_light_show_aider_operator", text="Add Drones for Selected").cmd = "Add Drones for Selected"

            # row = col.row()
            # row.prop_search(props_g, "leader_name", context.scene, "objects")
            # row.prop(props_g, "follow_distance")
            row = col.row()
            row.prop(props_g, "avoid_collision")
            row.prop(props_g, "insert_inverted")
            col.operator("object.drone_light_show_aider_operator", text="Append Keyframe for Selected at Current Frame").cmd = "Append Keyframe"
            split = col.split(factor=0.3)
            split.prop(props_g, "create_empty_name")
            split.operator("object.drone_light_show_aider_operator", text="Create Empty with Selected Obejcts Position").cmd = "Create Empty with Selected Obejcts Position"
            col.operator("object.drone_light_show_aider_operator", text="Create Copy Location Constraint between Selected").cmd = "Create Copy Location Constraint between Selected"
            # col.operator("object.drone_light_show_aider_operator", text="Insert Color Keyframe for Selected at Current Frame").cmd = "Insert Color Keyframe"
            # col.operator("object.drone_light_show_aider_operator", text="Insert Keyframe for Selected at Current Frame").cmd = "Insert Keyframe"
            col.operator("object.drone_light_show_aider_operator", text="Insert Vertices Keyframe at Current Frame").cmd = "Insert Vertices Keyframe"
            # col.operator("object.drone_light_show_aider_operator", text="Object Deform To at Current Frame").cmd = "Object Deform To"
            # col.operator("object.drone_light_show_aider_operator", text="Add Distance Constraint for Selected").cmd = "Add Distance Constraint for Selected"
            # col.operator("object.drone_light_show_aider_operator", text="Remove Distance Constraint for Selected").cmd = "Remove Distance Constraint for Selected"

            # row = col.row()
            # split = row.split(factor=0.2)
            # split.prop(props_g, "color")
            # split.operator("object.drone_light_show_aider_operator", text="Change Diffuse Color for Selected").cmd = "Change Diffuse Color for Selected"

            # col.operator("object.drone_light_show_aider_operator", text="Random Diffuse Color for Selected").cmd = "Random Diffuse Color for Selected"

            # col.operator("object.drone_light_show_aider_operator", text="Resolve Collision").cmd = "Resolve Collision"

            row = col.row()
            row.template_ID(props_g, 'image', open="image.open")
            row.operator("object.drone_light_show_aider_operator", text="Generate Mesh").cmd = "Generate Mesh"

            col.operator("object.drone_light_show_aider_operator", text="Generate Mesh With Particles for Selected").cmd = "Generate Mesh With Particles"

            row = col.row()
            row.prop(props_g, "scale_distance")
            row.operator("object.drone_light_show_aider_operator", text="Scale Fit for Selected").cmd = "Scale Fit"

            # col.prop(props_g, 'hiden_material_fcurves')



        # dynamic parent
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        if context.scene.showDynamicParentPanel:
            row.prop(context.scene, "showDynamicParentPanel", icon="DISCLOSURE_TRI_DOWN", text="", emboss=False)
        else:
            row.prop(context.scene, "showDynamicParentPanel", icon="DISCLOSURE_TRI_RIGHT", text="", emboss=False)
        row.label(text="dynamic parent")

        if context.scene.showDynamicParentPanel:
            row = col.row()
            row.operator("object.drone_light_show_aider_operator", text="Create").cmd = "Create Dynamic Parent"
            row.operator("object.drone_light_show_aider_operator", text="Disable").cmd = "Disable Dynamic Parent"


        # color
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        if context.scene.showColorPanel:
            row.prop(context.scene, "showColorPanel", icon="DISCLOSURE_TRI_DOWN", text="", emboss=False)
        else:
            row.prop(context.scene, "showColorPanel", icon="DISCLOSURE_TRI_RIGHT", text="", emboss=False)
        row.label(text="color")

        if context.scene.showColorPanel:
            row = col.row(align=True)
            row.prop(props_g, "color_start_frame")
            row.prop(props_g, "color_end_frame")
        
            box = col.box()
            row = box.row()
            row.label(text="1. full")
            row.prop(props_g, "tips_color_full", emboss=False, icon="QUESTION", icon_only=True)
            row = box.row()
            split = row.split(factor=0.2)
            split.prop(props_g, "color_full")
            split.operator("object.drone_light_show_aider_operator", text="Apply").cmd = "Apply Color Full"
        
            row = box.row()
            row.label(text="2. flicker")
            row.prop(props_g, "tips_color_flicker", emboss=False, icon="QUESTION", icon_only=True)
            row = box.row()
            row.template_list("Color_UL_CollectionList", "", props_g, "color_collection_item", props_g, "color_collection_item_index", rows=1, type='DEFAULT')
            col = row.column(align=True)
            col.operator("object.drone_light_show_aider_operator", icon='ADD', text="").cmd = 'Color Collection Add'
            col.operator("object.drone_light_show_aider_operator", icon='REMOVE', text="").cmd = 'Color Collection Remove'
            row = box.row()
            row.prop(props_g, "color_flicker_duration")
            # row.prop(props_g, "color_flicker_random")
            row.operator("object.drone_light_show_aider_operator", text="Apply").cmd = "Apply Color Flicker"
        
            row = box.row()
            row.label(text="3. switch")
            row.prop(props_g, "tips_color_switch", emboss=False, icon="QUESTION", icon_only=True)
            row = box.row()
            split = row.split(factor=0.2)
            subrow = split.row(align=True)
            subrow.prop(props_g, "color_switch_color1")
            subrow.prop(props_g, "color_switch_color2")
            subrow = split.row(align=True)
            subrow.prop(props_g, "color_switch_duration1")
            subrow.prop(props_g, "color_switch_number")
            box.operator("object.drone_light_show_aider_operator", text="Apply").cmd = "Apply Color Switch"

            row = box.row()
            row.label(text="4. switch and recover")
            row.prop(props_g, "tips_color_switch_and_recover", emboss=False, icon="QUESTION", icon_only=True)
            row = box.row()
            split = row.split(factor=0.2)
            split.prop(props_g, "color_switch_recover_color")
            subrow = split.row(align=True)
            subrow.prop(props_g, "color_switch_recover_duration")
            subrow.prop(props_g, "color_switch_recover_interval")
            subrow.prop(props_g, "color_switch_recover_number")
            box.operator("object.drone_light_show_aider_operator", text="Apply").cmd = "Apply Color Switch And Recover"

            row = box.row()
            row.label(text="5. go away")
            row.prop(props_g, "tips_color_go_away", emboss=False, icon="QUESTION", icon_only=True)
            row = box.row()
            split = row.split(factor=0.2)
            split.prop(props_g, "color_goaway_color")
            subrow = split.row(align=True)
            subrow.prop(props_g, "color_goaway_interval")
            subrow.prop(props_g, "color_goaway_number")
            box.operator("object.drone_light_show_aider_operator", text="Apply").cmd = "Apply Color Go Away"

            row = box.row()
            row.label(text="6. strength jitter")
            row.prop(props_g, "tips_color_strength_jitter", emboss=False, icon="QUESTION", icon_only=True)
            row = box.row(align=True)
            row.prop(props_g, "jitter")
            row.prop(props_g, "jitter_interval")
            box.operator("object.drone_light_show_aider_operator", text="Apply").cmd = "Apply Color Strength Jitter"

            row = box.row()
            row.label(text="7. candlelight")
            row.prop(props_g, "tips_color_candlelight", emboss=False, icon="QUESTION", icon_only=True)
            box.operator("object.drone_light_show_aider_operator", text="Apply").cmd = "Apply Color Candlelight"

            row = box.row()
            row.label(text="8. brush")
            row.prop(props_g, "tips_color_brush", emboss=False, icon="QUESTION", icon_only=True)
            
            row = box.row()
            row.template_list("BrushCollectionList", "", props_g, "brush_collection", props_g, "brush_collection_index", rows=1, type='DEFAULT')
            col = row.column(align=True)
            col.operator("object.drone_light_show_aider_operator", icon='ADD', text="").cmd = 'Brush Collection Add'
            col.operator("object.drone_light_show_aider_operator", icon='REMOVE', text="").cmd = 'Brush Collection Remove'
            
            split = box.split(factor=0.3)
            split.prop(props_g, "keep_color")
            split.operator("object.drone_light_show_aider_operator", text="Apply").cmd = "Apply Color Brush"

        # checking
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        if context.scene.showCheckingPanel:
            row.prop(context.scene, "showCheckingPanel", icon="DISCLOSURE_TRI_DOWN", text="", emboss=False)
        else:
            row.prop(context.scene, "showCheckingPanel", icon="DISCLOSURE_TRI_RIGHT", text="", emboss=False)
        row.label(text="checking")

        if context.scene.showCheckingPanel:
            row = col.row()
            row.prop(props_g, "checking_start_frame")
            row.prop(props_g, "checking_end_frame")
            row = col.row()
            row.prop(props_g, "min_distance")
            row.operator("object.drone_light_show_aider_operator", text="Check").cmd = "Check Distance"
            row = col.row()
            row.prop(props_g, "max_velocity")
            row.operator("object.drone_light_show_aider_operator", text="Check").cmd = "Check Velocity"
            row = col.row()
            row.prop(props_g, "max_horizontal_velocity")
            row.operator("object.drone_light_show_aider_operator", text="Check").cmd = "Check Horizontal Velocity"
            box = col.box()
            box.label(text="vertical velocity")
            row = box.row()
            row.prop(props_g, "max_vertical_up_velocity")
            row.prop(props_g, "max_vertical_down_velocity")
            box.operator("object.drone_light_show_aider_operator", text="Check").cmd = "Check Vertical Velocity"
            box = col.box()
            box.label(text="acceleration")
            row = box.row()
            row.prop(props_g, "max_x_acceleration")
            row.prop(props_g, "max_y_acceleration")
            row.prop(props_g, "max_z_acceleration")
            box.operator("object.drone_light_show_aider_operator", text="Check").cmd = "Check Acceleration"
            # col.operator("object.drone_light_show_aider_operator", text="Check Range").cmd = "Check Range"

        # export
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        if context.scene.showExportPanel:
            row.prop(context.scene, "showExportPanel", icon="DISCLOSURE_TRI_DOWN", text="", emboss=False)
        else:
            row.prop(context.scene, "showExportPanel", icon="DISCLOSURE_TRI_RIGHT", text="", emboss=False)
        row.label(text="export")

        if context.scene.showExportPanel:
            split = col.split(factor=0.3)
            split.prop(props_g, "export_inverted")
            split.operator("object.drone_light_show_aider_operator", text="Export Path").cmd = "Export Path"

def register():
    bpy.utils.register_class(OBJECT_PT_DroneLightShowAider)

    bpy.types.Scene.showGlobalPropertiesPanel = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.showInitializeMatrixPanel = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.showAutoAddDronesToCurvePanel = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.showAutoAddDronesToMeshPanel = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.showOperatorPanel = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.showDynamicParentPanel = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.showColorPanel = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.showCheckingPanel = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.showExportPanel = bpy.props.BoolProperty(default=False)

def unregister():
    bpy.utils.unregister_class(OBJECT_PT_DroneLightShowAider)
    
    del bpy.types.Scene.showGlobalPropertiesPanel
    del bpy.types.Scene.showInitializeMatrixPanel
    del bpy.types.Scene.showAutoAddDronesToCurvePanel
    del bpy.types.Scene.showAutoAddDronesToMeshPanel
    del bpy.types.Scene.showOperatorPanel
    del bpy.types.Scene.showDynamicParentPanel
    del bpy.types.Scene.showColorPanel
    del bpy.types.Scene.showCheckingPanel
    del bpy.types.Scene.showExportPanel