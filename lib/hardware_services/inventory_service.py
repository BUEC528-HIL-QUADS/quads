# EC528 change
#
# This will be an abstract class (perhaps can use abc) that will serve as a generic interface
# for QUADS to interact with and isolate its inventory. It will allow QUADS to substitute different inventory
# isolation services while making minimal changes to the current implementation of QUADS.
#
# This class will declare methods corresponding to the functions defined in lib/libquads.py so that QUADS can
# retain its normal workflow and command options. Once implemented, integration with a new inventory isolation
# service will only require writing a driver that inherits from this class and overwrites its methods with
# its service-specific behavior.
#
# The inventory service used can be specified at runtime (by changing a single parameter in the conf/quads.yml file).
# A user will specify the name of the service, which will be read in and used as a key in a dictionary (location tbd
# - perhaps in libquads.py, or its own "class mapper" class?) that maps superclass to subclass.
# Duck typing will be used to dynamically assign to a variable in libquads.py a concrete instance of the specified
# subclass (using the "class mapper" dictionary). The quads library will thus be decoupled from any knowledge of
# the specific inventory service being used, as it can now make calls based on this generic interface.
#
#
# abstract methods to be overwritten by concrete subclasses:
# note: these are only examples and do not describe the actual prototypes
#
#   remove_host():
#   remove_cloud():
#   update_host():
#   update_cloud():
#   move_hosts():
#   list_hosts():
#   list_clouds():
#
# this list may need to expand to accommodate for scheduling behavior, but for now we assume that scheduling
# will be able to continue with minimal changes (only thing that this will change is where QUADS pulls its data from)
#####################################################################################################################

import os, sys, importlib
from abc import ABCMeta, abstractmethod


sys.path.append(os.path.dirname(__file__) + "/hardware_services/inventory_drivers/")


def get_inventory_serivce(name, url):
    inventoryservice = name + "InventoryDriver"
    importlib.import_module()
    return getattr(sys.modules[inventoryservice], inventoryservice)(url)


class InventoryService(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def update_cloud(self, **kwargs):
        """ TODO add documentation
        """

    @abstractmethod
    def update_host(self, **kwargs):
        """ TODO add documentation
        """

    @abstractmethod
    def remove_cloud(self, **kwargs):
        """ TODO add documentation
        """

    @abstractmethod
    def remove_host(self, **kwargs):
        """ TODO add documentation
        """

    @abstractmethod
    def list_clouds(self):
        """ TODO add documentation
        """

    @abstractmethod
    def list_hosts(self):
        """ TODO add documentation
        """

    @abstractmethod
    def load_data(self, quads, force, initialize):
        """ TODO add documentation
        """

    @abstractmethod
    def init_data(self, quads, force):
        """ TODO add documentation
        """

    @abstractmethod
    def sync_state(self, quads):
        """ TODO add documentation
        """

    @abstractmethod
    def write_data(self, quads, doexit):
        """ TODO add documentation
        """
