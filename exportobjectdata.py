bl_info = {
    "name": "Export Level",
    "author": "Tom Tsiliopoulos",
    "version": (0, 1, 0),
    "blender": (2, 79, 0),
    "location": "File > Import-Export > Export Level",
    "description": "Export Object Data for Level",
    "warning": "",
    "category": "Import-Export",
}


import bpy

def write_object_data(context, filepath):
    print("Exporting Object Data...")
    f = open(filepath, 'w', encoding='utf-8')
    for current in bpy.data.objects:
        name = current.name
        locx = current.location.x
        locy = current.location.y
        locz = current.location.z
        rotx = current.rotation_euler.x
        roty = current.rotation_euler.y
        rotz = current.rotation_euler.z
        scalex = current.scale.x
        scaley = current.scale.y
        scalez = current.scale.z
        f.write(name + " " + str(locx) + " " + str(locy) + " " + str(locz) + " " + str(rotx) + " " + str(roty) + " " + str(rotz) + " " + str(scalex) + " " + str(scaley) + " " + str(scalez) + "\n")
    f.close()

    return {'FINISHED'}


# ExportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ExportObjectData(Operator, ExportHelper):
    """Exports all object data in scene: name, location, rotation, scale"""
    bl_idname = "export_level.txt"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Export Level"

    # ExportHelper mixin class uses this
    filename_ext = ".txt"

    filter_glob = StringProperty(
            default="*.txt",
            options={'HIDDEN'},
            maxlen=255,  # Max internal buffer length, longer would be clamped.
            )

    def execute(self, context):
        #return write_object_data(context, self.filepath, self.use_setting)
        return write_object_data(context, self.filepath)


# Only needed if you want to add into a dynamic menu
def menu_func_export(self, context):
    self.layout.operator(ExportObjectData.bl_idname, text="Export Level")


def register():
    bpy.utils.register_class(ExportObjectData)
    bpy.types.INFO_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ExportObjectData)
    bpy.types.INFO_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.export_level.txt('INVOKE_DEFAULT')
