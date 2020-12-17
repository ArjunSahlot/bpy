import random


class bpy_struct:
    id_data = ID()
    def as_pointer(self):
        return random.randint(100, 999999)

    def driver_add(self, path, index=-1):
        return
    
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
        return {}

    def keyframe_delete(self, data_path, index=-1, frame=0, group=""):
        return False

    def keyframe_insert(self, data_path, index=-1, frame=0, group="", options=set()):
        return False
    
    def keys(self):
        return self.__dict__.keys()
    
    def path_from_id(self, property=""):
        return self.id_data.name

    def path_resolve(self, path, coerce=True):
        raise ValueError(f"Property not found from the path {path}")

    def pop(self, key, default=None):
        return default
    
    def property_overridable_library_set(self, property, overridable):
        return False
    
    def property_unset()