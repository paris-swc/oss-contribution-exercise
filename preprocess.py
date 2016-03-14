"""
A few functions to pre-process data.
"""
import numpy as np


# For testing, being that far away from the correct result is considered OK
TOLERANCE = 1e-14


# ------------------------------------------------------------------------------
# center
# ------------------------------------------------------------------------------
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


# ------------------------------------------------------------------------------
# whiten
# ------------------------------------------------------------------------------
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
    pass  # TODO: Add tests


# ------------------------------------------------------------------------------
# value_range
# ------------------------------------------------------------------------------
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


# ------------------------------------------------------------------------------
# rescale
# ------------------------------------------------------------------------------
def rescale(data, lower=0.0, upper=1.0):
    """
    (Linearly) rescale the data so that it fits into the given range.

    Parameters
    ----------
    data : ndarray
        The data to rescale.
    lower : number, optional
        The lower bound for the data. Defaults to 0.
    upper : number, optional
        The upper bound for the data. Defaults to 1.

    Returns
    -------
    rescaled : ndarray
        The data rescaled between ``lower`` and ``upper``.
    """
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


# ------------------------------------------------------------------------------
# cut_to_same_size
# ------------------------------------------------------------------------------
def cut_to_same_size(data_1, data_2):
    """
    Returns the two given arrays, cut so their length is the length of the
    shorter one, i.e. so that the two arrays have the same length.

    Parameters
    ----------
    data_1 : ndarray
        The first array.
    data_2 : ndarray
        The second array.

    Returns
    -------
    cut_1, cut_2 : (ndarray, ndarray)
        The two original arrays, the longer one cut at the end to the length of
        the shorter one so that both arrays have the same length.
    """
    return data_1, data_2


def test_cut_to_same_size():
    data_1 = np.array([3, 4, 5])
    data_2 = np.array([6, 7, 8, 9, 10])
    cut_1, cut_2 = cut_to_same_size(data_1, data_2)
    assert len(cut_1) == len(cut_2) == len(data_1)
    assert np.all(cut_1 == data_1)
    assert np.all(cut_2 == data_2[:3])


# ------------------------------------------------------------------------------
# pad_to_same_size
# ------------------------------------------------------------------------------
def pad_to_same_size(data_1, data_2, pad_with=0.0):
    """
    Returns the two given arrays, the shorter one padded so that its length is
    the length of the longer one, i.e. so that the two arrays have the same
    length.

    Parameters
    ----------
    data_1 : ndarray
        The first array.
    data_2 : ndarray
        The second array.
    pad_with : number, optional
        The value used for padding at the end. Defaults to 0.

    Returns
    -------
    cut_1, cut_2 : (ndarray, ndarray)
        The two original arrays, the shorter padded at the end with the values
        given as ``pad_width`` so that both arrays have the same length.
    """
    return data_1, data_2


def test_pad_to_same_size():
    pass  # TODO: add tests
