import os
import sys

import pytest
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

from network_config_manager import NetworkConfigManager
from netmiko import ConnectHandler

@pytest.fixture
def net_config():
    """
    Skapa en instans av NetworkConfigManager.
    Anropa connect() -metoden i instansen för att etablera SSH-anslutningen till
    servern.
    Återställa alla konfigurationsvärden till utgångsläge genom att anropa rätt
    metoder i instansen:
    update_hostname("1") för att sätta hostname till "1".
    update_interface_state("down") för att sätta interface state till "down".
    update_response_prefix("Standard Response") för att sätta response
    prefix.
    """
    net_config = NetworkConfigManager()
    net_config.connect()
    net_config.update_hostname("1")
    net_config.update_interface_state("down")
    net_config.update_response_prefix("Standard Response")
    yield net_config
    net_config.disconnect()


class TestNetworkConfig:
    def test_show_host_name(self, net_config):
        # Tests that the connection returns hostname 1
        hostname = net_config.show_hostname()
        assert hostname == "hostname: 1"

    def test_show_interface_state(self, net_config):
        # Tests that the connection returns correct interface state
        assert False

    def test_show_response_prefix(self, net_config):
        # tests that response prefix is good
        assert False

    def test_update_hostname(self, net_config):
        # tests that hostname can be updated from its default values
        assert False

    def test_update_interface_state(self, net_config):
        # tests that interface state can be updated from its default values
        assert False

    def test_response_prefix(self, net_config):
        # tests that response prefix can be updated from its default values
        assert False
