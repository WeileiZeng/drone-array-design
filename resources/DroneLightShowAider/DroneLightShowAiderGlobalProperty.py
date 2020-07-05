import bpy
from DroneLightShowAider.ColorCollectionItem import ColorCollectionItem
from DroneLightShowAider.BrushCollection import BrushCollection
from DroneLightShowAider import Aider
from bpy.app.handlers import persistent

def update_hiden_material_fcurves(self, context):
    Aider.update_hiden_material_fcurves(self, context)

def update_light_strength(self, context):
    Aider.update_light_strength(self, context)

def update_drone_radius(self, context):
    Aider.update_drone_radius(self, context)

@persistent
def load_post_handler(arg):
    Aider.Instance().load_post()

@persistent
def save_pre_handler(arg):
    Aider.Instance().save_pre()


class DroneLightShowAiderGlobalProperty(bpy.types.PropertyGroup):
    drone_radius: bpy.props.FloatProperty(name="Drone Radius", min=0, soft_min=0, default=0.2, precision=2, step=10, update=update_drone_radius)
    min_distance: bpy.props.FloatProperty(name="Minimal Distance", min=0, soft_min=0, default=1.5, precision=2, step=10)
    max_velocity: bpy.props.FloatProperty(name="Maximal Velocity", min=0, soft_min=0, default=5, precision=2)
    max_horizontal_velocity: bpy.props.FloatProperty(name="Horizontal Velocity", min=0, soft_min=0, default=5, precision=2)
    max_vertical_up_velocity: bpy.props.FloatProperty(name="Up", min=0, soft_min=0, default=5, precision=2)
    max_vertical_down_velocity: bpy.props.FloatProperty(name="Down", min=0, soft_min=0, default=5, precision=2)
    max_x_acceleration: bpy.props.FloatProperty(name="X", min=0, soft_min=0, default=5, precision=2)
    max_y_acceleration: bpy.props.FloatProperty(name="Y", min=0, soft_min=0, default=5, precision=2)
    max_z_acceleration: bpy.props.FloatProperty(name="Z", min=0, soft_min=0, default=5, precision=2)

    num_x: bpy.props.IntProperty(name="drones for x", min=1, soft_min=1, default=10)
    num_y: bpy.props.IntProperty(name="drones for y", min=1, soft_min=1, default=10)
    spacing: bpy.props.FloatProperty(name="spacing", min=0, soft_min=0, default=2, precision=2)

    color: bpy.props.FloatVectorProperty(name="", default=(1.0, 1.0, 1.0), subtype="COLOR", min=0.0, max=1.0)

    image: bpy.props.PointerProperty(name="", type=bpy.types.Image)

    color_start_frame: bpy.props.IntProperty(name="start frame", min=1, default=1)
    color_end_frame: bpy.props.IntProperty(name="end frame", min=1, default=250)
    color_full: bpy.props.FloatVectorProperty(name="", default=(1.0, 1.0, 1.0), subtype="COLOR", min=0.0, max=1.0)

    color_flicker_duration: bpy.props.IntProperty(name="duration", min=1, default=10, description="持续时间")
    color_flicker_random: bpy.props.IntProperty(name="random", min=0, default=10)
    
    color_switch_color1: bpy.props.FloatVectorProperty(name="", default=(1.0, 1.0, 1.0), subtype="COLOR", min=0.0, max=1.0, description="选中的无人机灯光颜色")
    color_switch_color2: bpy.props.FloatVectorProperty(name="", default=(1.0, 1.0, 1.0), subtype="COLOR", min=0.0, max=1.0, description="未选中无人机灯光颜色")
    color_switch_duration1: bpy.props.IntProperty(name="duration", min=1, default=10, description="持续时间")
    color_switch_duration2: bpy.props.IntProperty(name="duration", min=1, default=10)
    color_switch_number: bpy.props.IntProperty(name="number", min=1, default=10, description="随机选取无人机个数")

    color_collection_item: bpy.props.CollectionProperty(type=ColorCollectionItem)
    color_collection_item_index: bpy.props.IntProperty(default=0)

    color_goaway_color: bpy.props.FloatVectorProperty(name="", default=(1.0, 1.0, 1.0), subtype="COLOR", min=0.0, max=1.0)
    color_goaway_number: bpy.props.IntProperty(name="number", min=1, default=10)
    color_goaway_interval: bpy.props.IntProperty(name="interval", min=1, default=10)

    checking_start_frame: bpy.props.IntProperty(name="start frame", min=1, default=1)
    checking_end_frame: bpy.props.IntProperty(name="end frame", min=1, default=250)

    color_switch_recover_color: bpy.props.FloatVectorProperty(name="", default=(1.0, 1.0, 1.0), subtype="COLOR", min=0.0, max=1.0, description="选中的无人机灯光颜色")
    color_switch_recover_duration: bpy.props.IntProperty(name="duration", min=1, default=10, description="持续时间")
    color_switch_recover_interval: bpy.props.IntProperty(name="interval", min=1, default=10, description="时间间隔")
    color_switch_recover_number: bpy.props.IntProperty(name="number", min=1, default=10, description="随机选取无人机个数")

    use_height: bpy.props.BoolProperty(name="use height", default=False)
    use_sphere: bpy.props.BoolProperty(name="use sphere", default=False)

    hiden_material_fcurves: bpy.props.BoolProperty(name="hiden material fcurves", default=False, update=update_hiden_material_fcurves)


    drones_color_json_string: bpy.props.StringProperty(default='{}')

    keep_color: bpy.props.BoolProperty(name="keep color", default=False)

    scale_distance: bpy.props.FloatProperty(name="Scale Distance", min=0, soft_min=0, default=2, precision=2)

    leader_name: bpy.props.StringProperty(name="leader")
    follow_distance: bpy.props.FloatProperty(name="distance", min=0, soft_min=0, default=5, precision=2)

    jitter: bpy.props.FloatProperty(name="jitter", min=0, max=1, default=0.2, precision=1, step=10)
    jitter_interval: bpy.props.IntProperty(name="interval", min=1, default=1)

    light_strength: bpy.props.IntProperty(name="Light Strength", min=1, default=10, update=update_light_strength)

    avoid_collision: bpy.props.BoolProperty(name="avoid collision", default=True)
    insert_inverted: bpy.props.BoolProperty(name="inverted", default=False)
    set_parent: bpy.props.BoolProperty(name="set parent", default=True)

    export_inverted: bpy.props.BoolProperty(name="inverted", default=False)

    brush_collection: bpy.props.CollectionProperty(type=BrushCollection)
    brush_collection_index: bpy.props.IntProperty(default=0)

    create_empty_name: bpy.props.StringProperty(name="", default="")

    # tips
    tips_color_full: bpy.props.BoolProperty(set=lambda a,b:None, description='''1. 从起始帧到结束帧\n2. 始终为设置的灯光颜色''')
    tips_color_flicker: bpy.props.BoolProperty(set=lambda a,b:None, description='''1. 从起始帧到结束帧\n2. 可添加或删除候选色\n3. 如果没有候选色则从全颜色中选取\n4. 为每个无人机，从候选色中随机选取一种颜色，持续设定的帧数，如此循环直到结束帧''')
    tips_color_switch: bpy.props.BoolProperty(set=lambda a,b:None, description='''1. 从起始帧到结束帧\n2. 每次从所有无人机中，随机选取设定数量的无人机，设置为选中色，\n未选中的设置为未选中色，持续设定的帧数，如此循环直到结束帧''')
    tips_color_switch_and_recover: bpy.props.BoolProperty(set=lambda a,b:None, description='''1. 从起始帧到结束帧\n2. 每次从所有无人机中，随机选取设定数量的无人机，设置为选中色，\n持续设定的帧数，再跳过设定的间隔，如此循环直到结束帧''')
    tips_color_go_away: bpy.props.BoolProperty(set=lambda a,b:None, description='''1. 从起始帧到结束帧\n2. 每隔设定的间隔时间，从剩余无人机中随机选取设定的数量，设置为选中色，\n持续到结束帧，如此循环直到结束帧''')
    tips_color_strength_jitter: bpy.props.BoolProperty(set=lambda a,b:None, description='''1. 从起始帧到结束帧\n2. 每隔设定的间隔时间，使当前的颜色按设定的系数进行上下浮动，持续到结束帧''')
    tips_color_candlelight:  bpy.props.BoolProperty(set=lambda a,b:None, description='''1. 从起始帧到结束帧\n2. 使无人机灯光像蜡烛燃烧跳跃的效果''')
    tips_color_brush:  bpy.props.BoolProperty(set=lambda a,b:None, description='''1. 从起始帧到结束帧\n2. 创建一个任意形状的物体，定义为刷子\n3. 为刷子添加材质，取消使用节点\n4. 刷子本身可以有任意动画\n5. 保留灯光效果可以使刷过的颜色得以保留\n6. 某时刻无人机在刷子内部时，此无人机的灯光被赋予此时刷子的颜色''')

def register():
    bpy.utils.register_class(DroneLightShowAiderGlobalProperty)

    bpy.types.Scene.DroneLightShowAiderGlobalProperty = bpy.props.PointerProperty(type=DroneLightShowAiderGlobalProperty)

    if load_post_handler not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(load_post_handler)

    if save_pre_handler not in bpy.app.handlers.save_pre:
        bpy.app.handlers.save_pre.append(save_pre_handler)

def unregister():
    bpy.utils.unregister_class(DroneLightShowAiderGlobalProperty)

    del bpy.types.Scene.DroneLightShowAiderGlobalProperty

    if load_post_handler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(load_post_handler)

    if save_pre_handler in bpy.app.handlers.save_pre:
        bpy.app.handlers.save_pre.remove(save_pre_handler)