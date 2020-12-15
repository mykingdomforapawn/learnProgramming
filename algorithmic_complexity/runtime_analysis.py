"""Playground to experiment and compare the runtime of different algorithms.

A collection of simple anlgorithms can be found in the module algorithm_potpourry.py and should be imported.
"""

import numpy as np

import algorithm_potpourri as ap
import runtime_analysis_utils as utils

# set input sizes and algorithms
inputSizes = np.arange(1, 11)
algorithms = np.array(
    [ap.double_input,
     ap.loop_to_double_input,
     ap.multiple_loop_to_double_input,
     ap.nested_loop_to_double_input,
     ap.fibonacci])

# calculate runtime for each input size/algorithm combination
runtimes = utils.calculate_runtime(algorithms, inputSizes)
print(runtimes)

# plot runtimes over input size
utils.plot_runtimes(runtimes)
