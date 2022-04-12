"""
Lumache - Python library for cooks and food lovers.
"""


class IscInterface:
    """
    The IscInterface class is the main interface class used to access all other Ipsa objects and functions.
    It must be created before any other references to Ipsa objects.
    """
    def ReadFile(strName: str):
        """
        Opens an Ipsa i2f file strName and returns an IscNetwork instance for that file.

        :param strName: The Ipsa i2f file that is going to be opened.
        :type strName: str
        :return: The IscNetwork instance for the strName file
        :rtype: IscNetwork
        """
        pass
