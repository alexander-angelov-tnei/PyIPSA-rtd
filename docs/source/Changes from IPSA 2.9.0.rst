Changes from IPSA 2.9.0
========================

Set license via environmental variable
---------------------------------------

There is a new option, only available for IPSA Linux for now, in order to set a Sentinel LDK license in IPSA. It is now possible to set the Sentinel LDK license Key ID in an environmental variable, and PyIPSA will automatically check the environmental variable if no other license is set. This was done in order to allow to run PyIPSA from non-desktop environment operative systems. This eliminates the need to first lunch IPSA to set the license. PyIPSA can be lunched straight-away if the right license Key ID is set in the environmental variable.

The environment variable to be set is **IPSALDKLICENSE** and it expects an 18-digit (or less) license Key ID. If no other licenses are set for the machine, the environment variable license Key ID is compared to the ones available to the machine and if there is a match the license is set and stored for the next runs, so that the same process does not need to be repeated. If the license Key ID is not correct, PyIPSA will stop the process and list the license Key IDs it was able to find. Alternatively, this list along with other diagnostics info, can be seen from the following Sentinel web-application: localhost:1947.
