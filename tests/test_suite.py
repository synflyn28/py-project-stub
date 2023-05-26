"""
This is an example pytest suite.
"""
import pytest
from pytest import fixture
from example_package import buisness_logic


@fixture
def generate_example_data():
    """
    This is an example data payload.
    :return:
    """

    return {
        'input_1': 'hello',
        'input_2': 'world'
    }


def test_concat_strings(generate_example_data):
    """
    Test to see if string concat function works properly
    :return:
    """

    assert buisness_logic.concat_string(
        generate_example_data['input_1'],
        generate_example_data['input_2']
    )


def test_concat_strings_filetypes():
    """
    Test to see if the right exception is raised for incorrect
    filetypes.
    :return:
    """

    with pytest.raises(IOError) as exc_info:
        buisness_logic.concat_string(1, "2")
    assert str(exc_info.value) == "Can't concat non-strings!"
