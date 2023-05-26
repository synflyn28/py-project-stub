"""
This code is an example of business logic that could be present in a Python
package.
"""


def concat_string(str1, str2):
    """
    This function concatenates two strings.
    :param arg1:
    :return:
    """

    if str1 is not str or str2 is not str:
        raise IOError("Can't concat non-strings!")

    return str1 + str2