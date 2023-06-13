"""A Python package to visualize molecules given their Cartesian coordinates.
This was created for the Python Best Practices Workshop"""

# Add imports here
from .functions import canvas
# from .measure import calculate_angle, calculate_distance
from molecool.measure import calculate_angle, calculate_distance #Same as above line
from molecool.atom_data import atomic_weights, atom_colors
from molecool.visualization import draw_molecule 

from molecool import io
from molecool.molecules import bond_histogram, build_bond_list, compute_molecular_mass


from ._version import __version__
