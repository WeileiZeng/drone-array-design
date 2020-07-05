import bpy
from DroneLightShowAider import Aider
from DroneLightShowAider.BrushCollection import BrushCollection

class DroneLightShowAiderOperator(bpy.types.Operator):
    bl_description = "Apply"
    bl_idname = "object.drone_light_show_aider_operator"
    bl_label = "Operator"


    cmd: bpy.props.StringProperty()
    brush_collection_item_index: bpy.props.IntProperty(default=-1)

    aider = Aider.Instance()

    def execute(self, context):
        if self.cmd == "Initialize Matrix":
            self.aider.initializeMatrix(context, self)
        elif self.cmd == "Initialize Matrix From File":
            bpy.ops.import_file.csv_file('INVOKE_DEFAULT')
        elif self.cmd == "Clear Matrix":
            self.aider.clearMatrix(self)
        elif self.cmd == "Select Objects as Initial Matrix":
            self.aider.selectObjectsAsInitialMatrix(context, self)
        elif self.cmd == "Select Drones to Show":
            self.aider.selectDronesToShow(self)
        elif self.cmd == "Append Keyframe":
            self.aider.appendKeyframe(context, self)
        elif self.cmd == "Create Empty with Selected Obejcts Position":
            self.aider.createEmptyWithSelectedObejctsPosition(self)
        elif self.cmd == "Create Copy Location Constraint between Selected":
            self.aider.createCopyLocationConstraintBetweenSelected(self)
        elif self.cmd == "Insert Color Keyframe":
            self.aider.insertColorKeyframe(context, self)
        elif self.cmd == "Insert Keyframe":
            self.aider.insertKeyframe(context, self)
        elif self.cmd == "Insert Vertices Keyframe":
            self.aider.insertVerticesKeyframe(self)
        elif self.cmd == "Object Deform To":
            self.aider.objectDeformTo(self)
        elif self.cmd == "Add Drones to Curve":
            self.aider.addDronesToCurve(context.object, self)
        elif self.cmd == "Add Drones to Mesh":
            self.aider.addDronesToMesh(context.object)
        elif self.cmd == "Add Drones for Selected":
            for o in context.selected_objects:
                if o.type == "CURVE":
                    self.aider.addDronesToCurve(o, self)
                elif o.type == "MESH":
                    self.aider.addDronesToMesh(o)
        elif self.cmd == "Add Distance Constraint for Selected":
            self.aider.addLimitDistanceConstraint(self)
        elif self.cmd == "Remove Distance Constraint for Selected":
            self.aider.removeLimitDistanceConstraint(self)
        elif self.cmd == "Change Diffuse Color for Selected":
            self.aider.changeDiffuseColor()
        elif self.cmd == "Random Diffuse Color for Selected":
            self.aider.randomDiffuseColor()
        elif self.cmd == "Resolve Collision":
            self.aider.resolveCollision(self)
        elif self.cmd == 'Generate Mesh':
            self.aider.generateMesh()
        elif self.cmd == "Generate Mesh With Particles":
            self.aider.generateMeshWithParticles(self)
        elif self.cmd == "Scale Fit":
            self.aider.scaleFit(self)
        elif self.cmd == "Apply Color Full":
            self.aider.applyColorFull(self)
        elif self.cmd == "Apply Color Flicker":
            self.aider.applyColorFlicker(self)
        elif self.cmd == "Apply Color Switch":
            self.aider.applyColorSwitch(self)
        elif self.cmd == "Apply Color Switch And Recover":
            self.aider.applyColorSwitchAndRecover(self)
        elif self.cmd == "Check Distance":
            self.aider.checkDistance(self)
        elif self.cmd == "Check Velocity":
            self.aider.checkVelocity(self)
        elif self.cmd == "Check Horizontal Velocity":
            self.aider.checkHorizontalVelocity(self)
        elif self.cmd == "Check Vertical Velocity":
            self.aider.checkVerticalVelocity(self)
        elif self.cmd == "Check Acceleration":
            self.aider.checkAcceleration(self)
        elif self.cmd == "Export Path":
            bpy.ops.export.drone_light_show_path('INVOKE_DEFAULT')
        elif self.cmd == "Create Dynamic Parent":
            self.aider.createDynamicParent(self)
        elif self.cmd == "Disable Dynamic Parent":
            self.aider.disableDynamicParent(self)
        elif self.cmd == "Color Collection Add":
            collection = bpy.context.scene.DroneLightShowAiderGlobalProperty.color_collection_item
            index = bpy.context.scene.DroneLightShowAiderGlobalProperty.color_collection_item_index

            item = collection.add()
            if len(collection) > 0:
                pre = collection[index]
                item.color = pre.color
            index = len(collection)-1
            bpy.context.scene.DroneLightShowAiderGlobalProperty.color_collection_item_index = index
            
        elif self.cmd == "Color Collection Remove":
            collection = bpy.context.scene.DroneLightShowAiderGlobalProperty.color_collection_item
            index = bpy.context.scene.DroneLightShowAiderGlobalProperty.color_collection_item_index

            collection.remove(index)
            bpy.context.scene.DroneLightShowAiderGlobalProperty.color_collection_item_index -= 1
            if bpy.context.scene.DroneLightShowAiderGlobalProperty.color_collection_item_index < 0:
                bpy.context.scene.DroneLightShowAiderGlobalProperty.color_collection_item_index = 0
        elif self.cmd == "Apply Color Brush":
            self.aider.applyColorBrush(self)
        elif self.cmd == "Brush Collection Add":
            collection = bpy.context.scene.DroneLightShowAiderGlobalProperty.brush_collection
            index = bpy.context.scene.DroneLightShowAiderGlobalProperty.brush_collection_index

            item = collection.add()
            index = len(collection)-1
            bpy.context.scene.DroneLightShowAiderGlobalProperty.brush_collection_index = index
        elif self.cmd == "Brush Collection Remove":
            collection = bpy.context.scene.DroneLightShowAiderGlobalProperty.brush_collection
            index = bpy.context.scene.DroneLightShowAiderGlobalProperty.brush_collection_index

            collection.remove(index)
            bpy.context.scene.DroneLightShowAiderGlobalProperty.brush_collection_index -= 1
            if bpy.context.scene.DroneLightShowAiderGlobalProperty.brush_collection_index < 0:
                bpy.context.scene.DroneLightShowAiderGlobalProperty.brush_collection_index = 0
        elif self.cmd == "Apply Color Go Away":
            self.aider.applyColorGoAway(self)
        elif self.cmd == "Apply Color Strength Jitter":
            self.aider.applyColorStrengthJitter(self)
        elif self.cmd == "Apply Color Candlelight":
            self.aider.applyColorCandlelight(self)
        elif self.cmd == "Assign Drones":
            collection = bpy.context.scene.DroneLightShowAiderGlobalProperty.brush_collection
            item = collection[self.brush_collection_item_index]

            item.drones = ""
            for o in bpy.context.selected_objects:
                item.drones += o.name + ','
        elif self.cmd == "Show Drones":
            collection = bpy.context.scene.DroneLightShowAiderGlobalProperty.brush_collection
            item = collection[self.brush_collection_item_index]
            
            drones = []
            for name in item.drones.split(','):
                if name in bpy.data.objects:
                    drones.append(bpy.data.objects[name])
            for o in bpy.context.selected_objects:
                o.select_set(state=False)

            for d in drones:
                d.select_set(state=True)
        elif self.cmd == "Assign Brushes":
            collection = bpy.context.scene.DroneLightShowAiderGlobalProperty.brush_collection
            item = collection[self.brush_collection_item_index]

            item.brushes = ""
            for o in bpy.context.selected_objects:
                item.brushes += o.name + ','
        elif self.cmd == "Show Brushes":
            collection = bpy.context.scene.DroneLightShowAiderGlobalProperty.brush_collection
            item = collection[self.brush_collection_item_index]
            
            brushes = []
            for name in item.brushes.split(','):
                if name in bpy.data.objects:
                    brushes.append(bpy.data.objects[name])
            for o in bpy.context.selected_objects:
                o.select_set(state=False)

            for d in brushes:
                d.select_set(state=True)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(DroneLightShowAiderOperator)

def unregister():
    bpy.utils.unregister_class(DroneLightShowAiderOperator)