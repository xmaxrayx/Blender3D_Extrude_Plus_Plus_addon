bl_info = {
    "name": "Extrude + +",
    "author": "xMaxrayx, xMaxrayx-P",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "Called by a hotkey",
    "description": "Pi menue for Extrude and other stuff",
    "warning": "",
    "doc_url": "",
    "category": "Edit Mesh",
}

import bpy
from bpy.types import Menu, Operator

# spawn an edit mode selection pie (run while object is in edit mode to get a valid output)
# Idname should small
###############################################################################################
#extrude start
class MY_EXTRUDE(bpy.types.Operator):
    """(・｀ω´・)"""
    bl_idname = "my.extrude"
    bl_label = "Extrude"

    #@classmethod
    #def poll(cls, context):
     #   return context.active_object is not None

    def execute(self, context):
        bpy.ops.view3d.edit_mesh_extrude_move_normal()
        return {'FINISHED'}
#extrude end    

##################################################################################################
#extrude individual start
class MY_EXTRUDE_INDIVIDUAL(bpy.types.Operator):
    """o(^-^)o"""
    bl_idname = "myextrude.individual"
    bl_label = "Individualy"

    #@classmethod
    #def poll(cls, context):
     #   return context.active_object is not None

    def execute(self, context):
        #bpy.ops.mesh.extrude_faces_move()
        bpy.ops.view3d.edit_mesh_extrude_individual_move()


        
        return {'FINISHED'}
#extrude individual end

################################################################################################
#extrude along_normals start
class MY_EXTRUDE_ALONG_NORMALS(bpy.types.Operator):
    """(/≥▽≤/)"""
    bl_idname = "myextrude.along"
    bl_label = "Along Nromals"

    
    def execute(self, context):
        bpy.ops.view3d.edit_mesh_extrude_move_shrink_fatten()
        return {'FINISHED'}
#extrude along_normals end

################################################################################################

#extrude manifold start                        @{

class MY_EXTRUDE_MANIFOLD(bpy.types.Operator):
    """ヾ (o ° ω ° O ) ノ゙"""
    bl_idname = "myextrude.manifold"
    bl_label = "Manifold"

    #@classmethod
    #def poll(cls, context):
     #   return context.active_object is not None

    def execute(self, context):
        bpy.ops.view3d.edit_mesh_extrude_manifold_normal()
        return {'FINISHED'}
#                                                            }@extrude manifold end

############################################################################################################

class Extrude_plus_plus(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Extrude + +"
    bl_idname = "extrude.max"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        
        pie.operator("my.extrude", icon="EMPTY_SINGLE_ARROW")
        pie.operator("myextrude.individual", icon="OUTLINER_OB_POINTCLOUD")
        pie.operator("myextrude.manifold", icon="MOD_SOLIDIFY")
        pie.operator("myextrude.along", icon="MOD_BOOLEAN")

    addon_keymaps = []

def register():
    bpy.utils.register_class(Extrude_plus_plus)
    bpy.utils.register_class(MY_EXTRUDE)
    bpy.utils.register_class(MY_EXTRUDE_INDIVIDUAL)
    bpy.utils.register_class(MY_EXTRUDE_MANIFOLD)
    bpy.utils.register_class(MY_EXTRUDE_ALONG_NORMALS)
    
    
  
     # Add the hotkey
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new("wm.call_menu_pie", type='F2', value='PRESS')
        kmi.properties.name = "Extrude_plus_plus"
        
 
  

    
def unregister():
    bpy.utils.unregister_class(Extrude_plus_plus)
    bpy.utils.unregister_class(MY_EXTRUDE)
    bpy.utils.unregister_class(MY_EXTRUDE_INDIVIDUAL)
    bpy.utils.unregister_class(MY_EXTRUDE_MANIFOLD)
    bpy.utils.unregister_class(MY_EXTRUDE_ALONG_NORMALS)

     ####
      # Remove the hotkey
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()

    bpy.ops.wm.call_menu_pie(name="Extrude_plus_plus")
