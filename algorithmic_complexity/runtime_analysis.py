"""Playground to experiment and compare the runtime of different algorithms.

A collection of simple anlgorithms can be found in the module algorithm_potpourry.py and should be imported.
"""

import numpy as np

import algorithm_potpourri as ap
import runtime_analysis_utils as utils

# set input sizes and algorithms
inputSizes = np.array(
    [1, 5, 10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
algorithms = np.array(
    [ap.double_first_element,
     ap.double_all_elements,
     ap.add_all_pairs])

# calculate runtime for each input size/algorithm combination
runtimes = utils.calculate_runtime(algorithms, inputSizes)
print(runtimes)

# plot runtimes over input size
utils.plot_runtimes(runtimes)
