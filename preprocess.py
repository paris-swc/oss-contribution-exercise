"""
A few functions to pre-process data.
"""
import numpy as np

# For testing, being that far away from the correct result is considered OK
TOLERANCE = 1e-14

def center(data, desired=0.0):
    """
    Return the data with its mean shifted to the desired value.

    Parameters
    ----------
    data : ndarray
        The data to center.
    desired : float, optional
        The new desired center of the data. Defaults to 0.0 if not specified.

    Returns
    -------
    centered : ndarray
        The data centered around the desired value.
    """
    return (data - data.mean()) + desired

def test_center():
    # After centering, mean should be the desired mean and the
    # standard deviation should be unchanged
    test_data = np.array([1, 3, 5, 7])

    centered = center(test_data)
    assert abs(centered.mean()) < TOLERANCE
    assert abs(centered.std() - test_data.std()) < TOLERANCE

    centered_5 = center(test_data, 5)
    assert abs(centered_5.mean() - 5) < TOLERANCE
    assert abs(centered_5.std() - test_data.std()) < TOLERANCE


def whiten(data):
    """
    Return a whitened copy of the data, i.e. data with zero mean and unit
    variance.

    Parameters
    ----------
    data : ndarray
        The data to whiten.

    Returns
    -------
    whitened : ndarray
        The whitened data.
    """
    return center(data) / data.std()

def test_whiten():
    # "pass" is just a placeholder, it does nothing, but it is necessary
    # here because a function needs some code in its "body". 
    pass  


def value_range(data):
    """
    Return the range of the values in ``data``, i.e. the distance between its
    lowest and the highest value.

    Parameters
    ----------
    data : ndarray
        The data.

    Returns
    -------
    range : number
        The distance between the lowest and the highest value of ``data``.
    """
    return 0.0

def test_value_range():
    assert value_range(np.array([1, 5, 0, 3])) == 5
    assert value_range(np.array([1, 1])) == 0


def rescale(data, lower=0.0, upper=1.0):
    return np.array([lower, upper])

def test_rescale():
    # These tests all pass, but the function above does certainly not do what
    # we want! Add tests that fail with the above implementation and then
    # correct the function so that it does what we want
    data = np.array([3, 7, 1, 3, 0, 2, 4])
    
    rescaled = rescale(data)
    assert np.all(rescaled >= 0)
    assert np.all(rescaled <= 1)
    assert np.min(rescaled) == 0.0
    assert np.max(rescaled) == 1.0

    rescaled_5_7 = rescale(data, 5, 7)
    assert np.all(rescaled_5_7 >= 5)
    assert np.all(rescaled_5_7 <= 7)
    assert np.min(rescaled_5_7) == 5.0
    assert np.max(rescaled_5_7) == 7.0

def cut_to_same_size(data_1, data_2):
    return data_1, data_2

def test_cut_to_same_size():
    data_1 = np.array([3, 4, 5])
    data_2 = np.array([6, 7, 8, 9, 10])
    cut_1, cut_2 = cut_to_same_size(data_1, data_2)
    assert len(cut_1) == len(cut_2) == len(data_1)
    assert np.all(cut_1 == data_1)
    assert np.all(cut_2 == data_2[:3])


def pad_to_same_size(data_1, data_2, pad_with=0.0):
    return data_1, data_2

def test_pad_to_same_size():
    pass

