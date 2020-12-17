import random
from structure import *


class View2D(bpy_struct):
    pass


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
