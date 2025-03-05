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
        interface_state = self.net_config.show_interface_state()
        assert interface_state == "interface_state: down"

    def test_show_response_prefix(self):

        # tests that response prefix is good
        response_prefix = self.net_config.show_response_prefix()
        assert response_prefix == "response_prefix: Standard Response"

    def test_update_hostname(self):
        update_hostname = self.net_config.update_hostname("10")
        assert update_hostname == "hostname: 10"


        # tests that hostname can be updated from its default values

    def test_update_interface_state(self):
        self.net_config.update_interface_state("up")
        interface_state = self.net_config.show_interface_state()
        assert interface_state == "interface_state: up"  

        # tests that interface state can be updated from its default values

    def test_uppdate_response_prefix(self):
        self.net_config.update_response_prefix("standard response10")
        response_prefix = self.net_config.show_response_prefix() 
        # tests that response prefix can be updated from its default values
        assert response_prefix == "response_prefix: standard response10"

