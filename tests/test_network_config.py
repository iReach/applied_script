import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

from network_config_manager import NetworkConfigManager
from netmiko import ConnectHandler

class TestNetworkConfig:

    def setup_method(self):
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
        self.net_config = NetworkConfigManager()
        self.net_config.connect()
        self.net_config.update_hostname("1")
        self.net_config.update_interface_state("down")
        self.net_config.update_response_prefix("Standard Response")

    def teardown_method(self):
        """
        Skapa en teardown_method som ska:
        Stänga SSH-anslutningen efter varje test genom att anropa disconnect()
        """
        self.net_config.disconnect()

    def test_show_host_name(self):
        # Tests that the connection returns hostname 1
        hostname = self.net_config.show_hostname()
        assert hostname == "hostname: 1"

    def test_show_interface_state(self):
        # Tests that the connection returns correct interface state
        assert False

    def test_show_response_prefix(self):
        # tests that response prefix is good
        assert False

    def test_update_hostname(self):
        # tests that hostname can be updated from its default values
        assert False

    def test_update_interface_state(self):
        # tests that interface state can be updated from its default values
        assert False

    def test_response_prefix(self):
        # tests that response prefix can be updated from its default values
        assert False
