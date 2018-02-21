import connexion
import six

from swagger_server.models.network import Network  # noqa: E501
from swagger_server import util

from network_stub import get_network

def network_get():  # noqa: E501
    """network_get

    Returns network interface card info information of the hosting server # noqa: E501


    :rtype: Network
    """
    return Network(get_network())
