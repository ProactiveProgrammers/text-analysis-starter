"""Visualize the sets using the supervenn package."""

from typing import List
from typing import Set

from supervenn import supervenn  # type: ignore
import matplotlib.pyplot as plot  # type: ignore


def visualize_sets(sets: List[Set[str]]):
    """Create a visualization of sets."""
    # create a matplotlib figure space
    plot.figure(figsize=(16, 8))
    # compute all of the subsets and then visualize them
    supervenn_plot = supervenn(
        sets, side_plots=True, widths_minmax_ratio=1, sets_ordering="minimize gaps"
    )
    # save the visualization in the output/ directory
    # NOTE: if you want to make the program more configurable, please
    # consider making this directory and file name a parameter to
    # the program instead of being hard-coded as a string
    # NOTE: you are not required to complete this task; however,
    # adding this feature to the program will make it easier for
    # you to complete the analysis of the text files using sets
    plot.savefig("graphics/set-visualization.png")
    # return the dictionary of chunks for visualization purposes
    return supervenn_plot.chunks
