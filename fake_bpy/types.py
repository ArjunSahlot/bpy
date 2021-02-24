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
from .utils.nonetype import NoneType
from .utils.blend_data import *
from .utils.structure import bpy_struct, ID


class View2D(bpy_struct):
    def region_to_view(self, x, y):
        return [0.0, 0.0]
    
    def view_to_region(self, x, y, clip=True):
        return [0, 0]
    
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
        return NoneType()
    
    @classmethod
    def bl_rna_get_subclass(cls, id, default=None):
        return default
    
    @classmethod
    def bl_rna_get_subclass_py(cls, id, default=None):
        return default


class Space(bpy_struct):
    show_locked_time = False
    show_region_header = False
    type = "EMPTY"

    @classmethod
    def bl_rna_get_subclass(self, id, default=None):
        return default
    
    @classmethod
    def bl_rna_get_subclass_py(self, id, default=None):
        return default
    
    def draw_handler_add(cself, allback, args, region_type, draw_type):
        return NoneType()
    
    def draw_handler_remove(self, handler, region_type):
        return NoneType()


class AreaSpaces(bpy_struct):
    active = Space()

    @classmethod
    def bl_rna_get_subclass(self, id, default=None):
        return default
    
    @classmethod
    def bl_rna_get_subclass_py(self, id, default=None):
        return default


class Area(bpy_struct):
    regions = [Region()] * random.randint(2, 20)
    show_menus = False
    spaces = [Space()] * random.randint(1, 4)
    type = "VIEW_3D"
    ui_type = ""
    x = y = width = height = 0

    def tag_redraw(self):
        return NoneType()
    
    def header_text_set(self, text):
        return NoneType()
    
    @classmethod
    def bl_rna_get_subclass(self, id, default=None):
        return default
    
    @classmethod
    def bl_rna_get_subclass_py(self, id, default=None):
        return default


class BlendData(bpy_struct):
    def __init__(self):
        self.actions
        self.armatures
        self.brushes
        self.cache_files
        self.cameras
        self.collections
        self.curves
        self.filepath
        self.fonts
        self.grease_pencils
        self.images
        self.is_dirty
        self.is_saved
        self.lattices
        self.libraries
        self.lightprobes
        self.lights
        self.linestyles
        self.masks
        self.materials
        self.meshes
        self.metaballs
        self.movieclips
        self.node_groups
        self.objects
        self.paint_curves
        self.palettes
        self.particles
        self.scenes
        self.screens
        self.shape_keys
        self.sounds
        self.speakers
        self.texts
        self.textures
        self.use_autopack
        self.version
        self.volumes
        self.window_managers
        self.workspaces
        self.worlds
    
    def batch_remove(self, ids):
        return NoneType()
    
    @classmethod
    def bl_rna_get_subclass(self, id, default=None):
        return default
    
    @classmethod
    def bl_rna_get_subclass_py(self, id, default=None):
        return default
    
    def orphans_purge(self):
        return NoneType()
    
    def user_map(self, key_types={...}, value_types={...}, **kwargs):
        return {ID():NoneType() for _ in range(random.randint(1, 10))}
