"""Collection of simple algorithms to analyse their runtime.

This module should be imported to runtime_analysis in order to experiment and compare the runtime of different algorithms.
"""


def double_input(n):
    """Double input size.

    Parameters:
        n (int): Integer representing input size.

    Returns:
        None

    Raises:
        None

    """

    n * 2
    return


def loop_to_double_input(n):
    """Double input size in a loop over the input size.

    Parameters:
        n (int): Integer representing input size.

    Returns:
        None

    Raises:
        None

    """

    for _ in range(n):
        n * 2
    return


def multiple_loop_to_double_input(n):
    """Double input size in a loop over the input size multiple times.

    Parameters:
        n (int): Integer representing input size.

    Returns:
        None

    Raises:
        None

    """

    for _ in range(5):
        for _ in range(n):
            n * 2
    return


def nested_loop_to_double_input(n):
    """Double input size in a nested loop over the input size.

    Parameters:
        n (int): Integer representing input size.

    Returns:
        None

    Raises:
        None

    """

    for _ in range(n):
        for _ in range(n):
            n * 2
    return


def fibonacci(n):
    """Calculate fibonacci of input size recursively.

    Parameters:
        n (int): Integer representing input size.

    Returns:
        None

    Raises:
        None

    """

    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
