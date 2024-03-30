# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 00:24:04 2020

@author: gutoa
"""

from .controlsair import AirProperties, AlgControls, sph2cart, cart2sph
from .fem_1d import FEM1D
from .grid_importing import GridImport, GridImport3D
from .fem_3d import FEM3D, fem_load, p2SPL
from .boundary_conditions import BC

from .sources import Source
from .receivers import Receiver
from .geometry_generate import GeometryGenerator
from .optimization_helpers import (
    r_s_for_room,
    r_s_positions,
    r_s_from_grid,
    fitness_metric,
)
from .utils import IR, SBIR
from .bem_3d import BEM3D
from tmma.tmm import TMM
from . import plot_tools
from . import fem_numerical

plot_tools.set_plotly_renderer()


__version__ = "0.2.0"
