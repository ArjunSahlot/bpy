#
#  Fake bpy
#  ```
#  Copyright Arjun Sahlot 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import random
from .nonetype import NoneType


class bpy_struct:
    def __init__(self):
        self.id_data = ""

    def as_pointer(self):
        return random.randint(100, 999999)

    def driver_add(self, path, index=-1):
        return NoneType()
    
    def driver_remove(self, path, index=-1):
        return False
    
    def get(self, key, default=None):
        return default
    
    def is_property_hidden(self, property):
        return bool(random.randint(0, 1))

    def is_property_overridable_library(self, property):
        return False

    def is_property_readonly(self, property):
        return True

    def is_property_set(self, property, ghost=True):
        return True

    def items(self):
        return NoneType()

    def keyframe_delete(self, data_path, index=-1, frame=0, group=""):
        return False

    def keyframe_insert(self, data_path, index=-1, frame=0, group="", options=set()):
        return False
    
    def keys(self):
        return self.__dict__.keys()
    
    def path_from_id(self, property=""):
        return self.id_data

    def path_resolve(self, path, coerce=True):
        raise ValueError(f"Property not found from the path {path}")

    def pop(self, key, default=None):
        return default
    
    def property_overridable_library_set(self, property, overridable):
        return False
    
    def property_unset(self, property):
        return NoneType()
    
    def type_recast(self):
        return bpy_struct()
    
    def values(self):
        return self.__dict__.values()


class ID(bpy_struct):
    def __init__(self):
        self.is_embedded_data = False
        self.is_evaluated = False
        self.is_library_indirect = False
        self.library = Library()
        self.name = ""
        self.name_full = ""
        self.original = ID()
        self.override_library = IDOverrideLibrary()
        self.preview = ImagePreview()
        self.tag = False
        self.use_fake_user = False
        self.users = 0
    
    def evaluated_get(self, depsgraph):
        return ID()
    
    def copy(self):
        return ID()
    
    def override_create(remap_local_usages=False):
        return ID()
    
    def user_clear(self):
        return NoneType()
    
    def user_remap(self, new_id):
        self = new_id
    
    def make_local(self, clear_proxy=True):
        return ID()
    
    def user_of_id(self, id):
        return self.users
    
    def animation_data_create(self):
        return NoneType()
    
    def animation_data_clear(self):
        return NoneType()
    
    def update_tag(refresh={}):
        return NoneType()
    
    @classmethod
    def bl_rna_get_subclass(self, id, default=None):
        return default
    
    @classmethod
    def bl_rna_get_subclass_py(self, id, default=None):
        return default


class PackedFile(bpy_struct):
    data = ""
    size = 0

    @classmethod
    def bl_rna_get_subclass(self, id, default=None):
        return default
    
    @classmethod
    def bl_rna_get_subclass_py(self, id, default=None):
        return default


class Library(ID):
    def __init__(self):
        self.filepath = ""
        self.packed_file = PackedFile()
        self.parent = Library()
        self.version = (0, 0, 0)
        self.users_id = ID()

    def reload(self):
        return NoneType()

    @classmethod
    def bl_rna_get_subclass(self, id, default=None):
        return default
    
    @classmethod
    def bl_rna_get_subclass_py(self, id, default=None):
        return default


class ImagePreview(bpy_struct):
    icon_id = 0
    icon_pixels = 0
    icon_pixels_float = 0.0
    icon_size = (0, 0)
    image_pixels = 0
    image_pixels_float = 0.0
    image_size = (0, 0)
    is_icon_custom = False
    is_image_custom = False

    def reload(self):
        return NoneType()
    
    @classmethod
    def bl_rna_get_subclass(self, id, default=None):
        return default
    
    @classmethod
    def bl_rna_get_subclass_py(self, id, default=None):
        return default


class IDOverrideLibrary(bpy_struct):
    def __init__(self):
        self.properties = [IDOverrideLibraryProperty()] * random.randint(1, 10)


class IDOverrideLibraryProperty(bpy_struct):
    def __init__(self):
        self.operations = [IDOverrideLibraryPropertyOperation()] * random.randint(1, 10)
        self.rna_path = ""
    
    @classmethod
    def bl_rna_get_subclass(self, id, default=None):
        return default
    
    @classmethod
    def bl_rna_get_subclass_py(self, id, default=None):
        return default


class IDOverrideLibraryPropertyOperation(bpy_struct):
    def __init__(self):
        self.flag = "MANDATORY"
        self.operation = "REPLACE"
        self.subitem_local_index = -1
        self.subitem_local_name = ""
        self.subitem_reference_index = -1
        self.subitem_reference_name = ""
    
    @classmethod
    def bl_rna_get_subclass(self, id, default=None):
        return default
    
    @classmethod
    def bl_rna_get_subclass_py(self, id, default=None):
        return default
