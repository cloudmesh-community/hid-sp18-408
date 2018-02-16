import connexion
import six

from swagger_server.models.network import NETWORK  # noqa: E501
from swagger_server import util
from network_stub import get_network

def network_get():  # noqa: E501
    """network_get

    Returns network information of the hosting server # noqa: E501


    :rtype: NETWORK
    """
    return NETWORK(get_network())
