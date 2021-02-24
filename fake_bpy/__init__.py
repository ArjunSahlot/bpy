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

from . import context
# from . import data
# from . import msgbus
# from . import ops
from . import types
# from . import utils
# from . import path
# from . import app
# from . import props

print(
"""
Note:
It is not necessary that your code will not work in bpy if it doesn't work in fake-bpy.
fake-bpy is just a module that will help check your code for missing params or incorrect method usage. 
It does not contain the data that Blender does.
""")