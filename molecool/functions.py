"""Provide the primary functions.
The source code goes here."""
import os
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

def canvas(with_attribution=True):
    """
    Placeholder function to show example of docstring (NumPy format)
    
    Replace this function and doc string for your own project
    
    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who quote is from
    
    Returns
    -------
    quote : str
        Compiled quote including string and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t - Adapted by H.D.T"
    return quote

if __name__ == "__main__":
    #Do something if invoked on its own
    print(canvas())