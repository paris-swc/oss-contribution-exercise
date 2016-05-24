"""
A few functions to pre-process data.
"""
import numpy as np


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
