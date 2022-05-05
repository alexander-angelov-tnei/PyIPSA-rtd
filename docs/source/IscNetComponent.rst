IscNetComponent
================

The ``IscNetComponent`` class is the base class for all IPSA components. All functions that are exposed (described below) are accessible via the derived component classes. The functions in this section should therefore be used in conjunction with one of the IPSA component classes, e.g. for accessing busbar data the following code would be used:

::

    busbar = ipsa_network.GetBusbar(“Busbar1”)
    nBusbarUID = busbar.GetUID()

Extension Data
---------------

It is possible to add extension data to an object of any type. The definitions of the data extension fields are held as static data associated with the component, i.e. all components of the same type have the same extension data fields. The actual field values on each component are stored with the component.

All extension data is handled transparently by the IPSA filing modules and is not currently used for analysis by IPSA. All extension data fields are persistent when filed.

The field names for extended data fields **should not** contain spaces. Only alphanumeric characters and underscores are permitted.


IscNetComponent Class
----------------------
.. autoclass:: ipsa.IscNetComponent
   :members:
