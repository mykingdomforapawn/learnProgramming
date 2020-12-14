"""Collection of simple algorithms to analyse their runtime.

This module should be imported to runtime_analysis in order to experiment and compare the runtime of different algorithms.
"""


def double_first_element(arr):
    """Double first element of an array.

    Parameters:
        arr (int): Array of random integers.

    Returns:
        None

    Raises:
        None

    """

    arr[0] * 2
    return


def double_all_elements(arr):
    """Double all elements of an array.

    Parameters:
        arr (int): Array of random integers.

    Returns:
        None

    Raises:
        None

    """

    for idxArr in range(len(arr)):
        arr[idxArr] * 2
    return


def add_all_pairs(arr):
    """Add all possible pairs of elements from array.

    Parameters:
        arr (int): Array of random integers.

    Returns:
        None

    Raises:
        None

    """

    for idxArrX in range(len(arr)):
        for idxArrY in range(len(arr)):
            arr[idxArrX] + arr[idxArrY]
    return
