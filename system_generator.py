"""
Contains base utility class to generate an openmm System
object from the topology proposal
"""

class SystemGenerator(object):
    """
    This is the base class for utility functions that generate a System
    object from TopologyProposal namedtuple

    Arguments
    ---------
    proposal : TopologyProposal namedtuple
        Contains the proposed new topology and metadata

    Properties
    ----------
    system : simtk.openmm.System object, read only
        The system object corresponding to the given topology
    """

    def __init__(self, proposal):
        pass

    @property
    def system(self):
	pass
