import bpy

# This block can be automatically generated by UI translations addon, which also handles conversion with PO format.
# See also https://wiki.blender.org/index.php/Dev:Doc/Process/Translate_Blender#Translating_non-official_addons
# It can (should) also be put in a different, specific py file.

# ##### BEGIN AUTOGENERATED I18N SECTION #####
# NOTE: You can safely move around this auto-generated block (with the begin/end markers!),
#       and edit the translations by hand.
#       Just carefully respect the format of the tuple!

# Tuple of tuples ((msgctxt, msgid), (sources, gen_comments), (lang, translation, (is_fuzzy, comments)), ...)
translations_tuple = (
    (("*", "Drone Light Show Aider"),
     ((), ()),
     ("zh_CN", "无人机灯光秀动画制作辅助",
     (False, ()))
    ),

    (("*", "global properties"),
     ((), ()),
     ("zh_CN", "全局参数",
     (False, ()))
    ),
    (("*", "Drone Radius"),
     ((), ()),
     ("zh_CN", "无人机半径",
     (False, ()))
    ),
    (("*", "Minimal Distance"),
     ((), ()),
     ("zh_CN", "最小距离",
     (False, ()))
    ),
    (("*", "Light Strength"),
     ((), ()),
     ("zh_CN", "灯光强度",
     (False, ()))
    ),

    (("*", "initialize matrix"),
     ((), ()),
     ("zh_CN", "初始矩阵设置",
     (False, ()))
    ),
    (("*", "drones for x"),
     ((), ()),
     ("zh_CN", "X 方向个数",
     (False, ()))
    ),
    (("*", "drones for y"),
     ((), ()),
     ("zh_CN", "Y 方向个数",
     (False, ()))
    ),
    (("*", "spacing"),
     ((), ()),
     ("zh_CN", "间距",
     (False, ()))
    ),
    (("*", "use sphere"),
     ((), ()),
     ("zh_CN", "使用球模型",
     (False, ()))
    ),
    (("Operator", "Generate Matrix"),
     ((), ()),
     ("zh_CN", "生成初始矩阵",
     (False, ()))
    ),
    (("*", "use height"),
     ((), ()),
     ("zh_CN", "保留高度",
     (False, ()))
    ),
    (("Operator", "Generate Matrix From File"),
     ((), ()),
     ("zh_CN", "从文件生成初始矩阵",
     (False, ()))
    ),
    (("Operator", "Select Objects as Initial Matrix"),
     ((), ()),
     ("zh_CN", "将选中的物体作为无人机",
     (False, ()))
    ),
    (("Operator", "Select Drones to Show"),
     ((), ()),
     ("zh_CN", "将当前的无人机选中以显示",
     (False, ()))
    ),

    (("*", "auto add drones to curve"),
     ((), ()),
     ("zh_CN", "自动分布无人机到曲线",
     (False, ()))
    ),
    (("*", "Number Of Drone"),
     ((), ()),
     ("zh_CN", "无人机个数",
     (False, ()))
    ),

    (("*", "auto add drones to mesh"),
     ((), ()),
     ("zh_CN", "自动分布无人机到模型",
     (False, ()))
    ),
    (("*", "set parent"),
     ((), ()),
     ("zh_CN", "设置父级",
     (False, ()))
    ),

    (("*", "operator"),
     ((), ()),
     ("zh_CN", "通用操作",
     (False, ()))
    ),

    (("Operator", "Add Drones for Selected"),
     ((), ()),
     ("zh_CN", "自动分布无人机到选中的物体上",
     (False, ()))
    ),
    (("*", "avoid collision"),
     ((), ()),
     ("zh_CN", "防碰撞",
     (False, ()))
    ),
    (("Operator", "Append Keyframe for Selected at Current Frame"),
     ((), ()),
     ("zh_CN", "在当前帧位置自动添加关键帧到选中的物体",
     (False, ()))
    ),
    (("Operator", "Insert Vertices Keyframe at Current Frame"),
     ((), ()),
     ("zh_CN", "在当前帧位置自动添加选中物体的顶点关键帧",
     (False, ()))
    ),
    (("Operator", "Generate Mesh"),
     ((), ()),
     ("zh_CN", "生成模型",
     (False, ()))
    ),
    (("Operator", "Generate Mesh With Particles for Selected"),
     ((), ()),
     ("zh_CN", "利用选中物体的粒子生成模型",
     (False, ()))
    ),
    (("*", "Scale Distance"),
     ((), ()),
     ("zh_CN", "缩放到最小距离为",
     (False, ()))
    ),
    (("Operator", "Scale Fit for Selected"),
     ((), ()),
     ("zh_CN", "缩放选中的物体",
     (False, ()))
    ),

    (("*", "dynamic parent"),
     ((), ()),
     ("zh_CN", "动态父级操作",
     (False, ()))
    ),
    (("Operator", "Create"),
     ((), ()),
     ("zh_CN", "创建",
     (False, ()))
    ),
    (("Operator", "Disable"),
     ((), ()),
     ("zh_CN", "取消",
     (False, ()))
    ),

    (("*", "color"),
     ((), ()),
     ("zh_CN", "灯光",
     (False, ()))
    ),
    (("*", "start frame"),
     ((), ()),
     ("zh_CN", "起始帧",
     (False, ()))
    ),
    (("*", "end frame"),
     ((), ()),
     ("zh_CN", "结束帧",
     (False, ()))
    ),
    (("*", "1. full"),
     ((), ()),
     ("zh_CN", "1. 常亮",
     (False, ()))
    ),
    (("*", "7. candlelight"),
     ((), ()),
     ("zh_CN", "7. 烛光效果",
     (False, ()))
    ),
    (("*", "keep color"),
     ((), ()),
     ("zh_CN", "保留灯光效果",
     (False, ()))
    ),

    (("*", "checking"),
     ((), ()),
     ("zh_CN", "检查",
     (False, ()))
    ),
    (("*", "Maximal Velocity"),
     ((), ()),
     ("zh_CN", "最大合速度",
     (False, ()))
    ),
    (("*", "Horizontal Velocity"),
     ((), ()),
     ("zh_CN", "最大水平方向速度",
     (False, ()))
    ),
    (("Operator", "Check"),
     ((), ()),
     ("zh_CN", "开始检查",
     (False, ()))
    ),
    (("*", "vertical velocity"),
     ((), ()),
     ("zh_CN", "竖直方向速度",
     (False, ()))
    ),
    (("*", "acceleration"),
     ((), ()),
     ("zh_CN", "加速度",
     (False, ()))
    ),

    (("*", "export"),
     ((), ()),
     ("zh_CN", "导出",
     (False, ()))
    ),
    (("Operator", "Export Path"),
     ((), ()),
     ("zh_CN", "导出航点",
     (False, ()))
    ),

    (("*", "hover mouse to show tooltips"),
     ((), ()),
     ("zh_CN", "悬停鼠标显示说明",
     (False, ()))
    ),

    (("*", "duration"),
     ((), ()),
     ("zh_CN", "持续时间",
     (False, ()))
    ),
    (("*", "number"),
     ((), ()),
     ("zh_CN", "数量",
     (False, ()))
    ),
    (("*", "interval"),
     ((), ()),
     ("zh_CN", "时间间隔",
     (False, ()))
    ),
    (("*", "jitter"),
     ((), ()),
     ("zh_CN", "浮动系数",
     (False, ()))
    ),

    (("*", "inverted"),
     ((), ()),
     ("zh_CN", "反向",
     (False, ()))
    ),
)

translations_dict = {}
for msg in translations_tuple:
    key = msg[0]
    for lang, trans, (is_fuzzy, comments) in msg[2:]:
        if trans and not is_fuzzy:
            translations_dict.setdefault(lang, {})[key] = trans

# ##### END AUTOGENERATED I18N SECTION #####

# Define remaining addon (operators, UI...) here.

def register():
   # Usual operator/UI/etc. registration...
    unregister()
    bpy.app.translations.register(__name__, translations_dict)


def unregister():
    bpy.app.translations.unregister(__name__)