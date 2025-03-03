import NetworkdConfigManager
from netmiko import ConnectHandler

class TestNetworkConfig:

    def setup(self):
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
        pass

    def teardown(self):
        """
        Skapa en teardown_method som ska:
        Stänga SSH-anslutningen efter varje test genom att anropa disconnect()
        """
        pass

    def test_show_host_name(self):
        # Tests that the connection returns hostname 1
        pass

    def test_show_interface_state(self):
        # Tests that the connection returns correct interface state
        pass

    def test_show_response_prefix(self):
        # tests that response prefix is good
        pass