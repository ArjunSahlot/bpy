import random


class bpy_struct:
    def as_pointer(self):
        return random.randint(100, 999999)

    def driver_add(self, path, index=-1):
        return
    
    def driver_remove(self, path, index=-1):
        return False
    
    def get(self, key, default=None):
        return default
    
    def is_property_hidden(self, property):
        return True


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
