import random
from .utils import NoneType
from .structure import bpy_struct


class View2D(bpy_struct):
    pass


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
        return
    
    def user_remap(self, new_id):
        self = new_id
    
    def make_local(self, clear_proxy=True):
        return ID()
    
    def user_of_id(self, id):
        return self.users
    
    def animation_data_create(self):
        return NoneType()
    
    def animation_data_clear(self):
        return
    
    def update_tag(refresh={}):
        return
    
    @classmethod
    def bl_rna_get_subclass(self, id, default=None):
        return default
    
    @classmethod
    def bl_rna_get_subclass_py(self, id, default=None):
        return default


class Region(bpy_struct):
    alignment = "None"
    height = random.randint(0, 32767)
    type = "WINDOW"
    view2d = View2D()
    width = random.randint(0, 32767)
    x, y = random.randint(-32767, 32767), random.randint(-32767, 32767)

    def tag_redraw(self):
        return
    
    @classmethod
    def bl_rna_get_subclass(cls, id, default=None):
        return default
    
    @classmethod
    def bl_rna_get_subclass_py(cls, id, default=None):
        return default


class Area(bpy_struct):
    height = random.randint(0, 32767)
    regions = [Region()] * random.randint(2, 20)
