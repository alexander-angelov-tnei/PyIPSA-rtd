class IscNetworkData:
    """
    The IscNetworkData class provides access to the Ipsa network data such as the system base MVA,
    to set and get data values.
    """
    def GetIValue(self, nFieldIndex: int) -> int:
        """
        Returns an integer value for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The integer value.
        :rtype: int
        """
        pass

    def GetDValue(self, nFieldIndex: int) -> float:
        """
        Returns a double value for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The double value.
        :rtype: float
        """
        pass

    def GetSValue(self, nFieldIndex: int) -> str:
        """
        Returns a string value for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The string value.
        :rtype: str
        """
        pass

    def GetBValue(self, nFieldIndex: int) -> bool:
        """
        Returns a boolean value for the enumerated field.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :return: The boolean value.
        :rtype: bool
        """
        pass

    def SetIValue(self, nFieldIndex: int, nValue: int) -> bool:
        """
        Sets the value for the enumerated field from an integer.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param nValue: The given integer value.
        :type nValue: int
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetDValue(self, nFieldIndex: int, dValue: float) -> bool:
        """
        Sets the value for the enumerated field from a double.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param dValue: The given double value.
        :type dValue: float
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetSValue(self, nFieldIndex: int, strValue: int) -> bool:
        """
        Sets the value for the enumerated field from a string.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param strValue: The given string value.
        :type strValue: str
        :return: True if successful.
        :rtype: bool
        """
        pass

    def SetBValue(self, nFieldIndex: int, bValue: bool) -> bool:
        """
        Sets the value for the enumerated field from boolean.

        :param nFieldIndex: The field index.
        :type nFieldIndex: int
        :param bValue: The given boolean value.
        :type bValue: bool
        :return: True if successful.
        :rtype: bool
        """
        pass