import numpy as np
from numpy.testing.utils import assert_almost_equal

import preprocess


def test_center():
    # After centering, mean should be the desired mean and the
    # standard deviation should be unchanged
    test_data = np.array([1, 3, 5, 7])

    centered = preprocess.center(test_data)
    assert_almost_equal(centered.mean(), 0)
    assert_almost_equal(centered.std(), test_data.std())

    centered_5 = preprocess.center(test_data, 5)
    assert_almost_equal(centered_5.mean(), 5)
    assert_almost_equal(centered_5.std(), test_data.std())


def test_whiten():
    # "pass" is just a placeholder, it does nothing, but it is necessary
    # here because a function needs some code in its "body".
    pass  # TODO: Add tests


def test_value_range():
    assert preprocess.value_range(np.array([1, 5, 0, 3])) == 5
    assert preprocess.value_range(np.array([1, 1])) == 0


def test_rescale():
    # These tests all pass, but the function above does certainly not do what
    # we want! Add tests that fail with the above implementation and then
    # correct the function so that it does what we want
    data = np.array([3, 7, 1, 3, 0, 2, 4])

    rescaled = preprocess.rescale(data)
    assert np.all(rescaled >= 0)
    assert np.all(rescaled <= 1)
    assert np.min(rescaled) == 0.0
    assert np.max(rescaled) == 1.0

    rescaled_5_7 = preprocess.rescale(data, 5, 7)
    assert np.all(rescaled_5_7 >= 5)
    assert np.all(rescaled_5_7 <= 7)
    assert np.min(rescaled_5_7) == 5.0
    assert np.max(rescaled_5_7) == 7.0


def test_cut_to_same_size():
    data_1 = np.array([3, 4, 5])
    data_2 = np.array([6, 7, 8, 9, 10])
    cut_1, cut_2 = preprocess.cut_to_same_size(data_1, data_2)
    assert len(cut_1) == len(cut_2)
    assert len(cut_1) == len(data_1)
    assert np.all(cut_1 == data_1)
    assert np.all(cut_2 == data_2[:3])


def test_pad_to_same_size():
    pass  # TODO: add tests
