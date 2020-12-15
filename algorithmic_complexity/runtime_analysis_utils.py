"""Utilities to perform the runtime analysis.

This module should be imported to runtime_analysis in order to experiment and compare the runtime of different algorithms.
"""

import timeit

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set()


def calculate_runtime(algorithms, inputSizes):
    """Calculate runtimes for a algorithm/input size combinations.

    Parameters:
        algorithms (func): Array of algorithms from algorithm_potpourri.py.
        inputSizes (int): Array of input sizes.

    Returns:
        runtimes (int): Array of runtimes for each input sizes/algorithm combination.

    Raises:
        None

    """

    # initialize df to hold runtimes
    runtimes = pd.DataFrame(np.zeros((len(inputSizes), len(
        algorithms))), index=inputSizes)
    for idxAlgorithm in range(len(algorithms)):
        for idxInputSize in range(len(inputSizes)):
            inputArray = np.random.randint(100, size=inputSizes[idxInputSize])
            start = timeit.default_timer()
            algorithms[idxAlgorithm](inputArray)
            stop = timeit.default_timer()
            runtimes.iloc[idxInputSize, idxAlgorithm] = stop-start
        runtimes.rename(
            columns={idxAlgorithm: algorithms[idxAlgorithm].__name__}, inplace=True)
    return runtimes


def plot_runtimes(runtimes):
    """Plot runtimes for a algorithm/input size combinations.

    Parameters:
        runtimes (int): Array of runtimes for each input sizes/algorithm combination.

    Returns:
        None

    Raises:
        None

    """

    ax = runtimes.plot(kind='line', title='algorithmic_complexity', logx=True)
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()
    return
