import time
import random
import json

class NetworkElement:
    def __init__(self, name):
        self.name = name
        self.connections = {}
    
    def connect(self, other_element, bandwidth):
        self.connections[other_element.name] = bandwidth
        other_element.connections[self.name] = bandwidth
        
    def get_connections(self):
        return self.connections


class Switch(NetworkElement):
    def __init__(self, name):
        super().__init__(name)
        self.flows = {}

    def add_flow(self, dst, priority=1):
        self.flows[dst] = priority
        
    def remove_flow(self, dst):
        if dst in self.flows:
            del self.flows[dst]
        
    def get_flows(self):
        return self.flows


class Controller:
    def __init__(self, name):
        self.name = name
        self.switches = {}
    
    def add_switch(self, switch):
        self.switches[switch.name] = switch
        
    def remove_switch(self, switch):
        if switch.name in self.switches:
            del self.switches[switch.name]
    
    def configure_flow(self, switch_name, dst, priority):
        if switch_name in self.switches:
            self.switches[switch_name].add_flow(dst, priority)
    
    def delete_flow(self, switch_name, dst):
        if switch_name in self.switches:
            self.switches[switch_name].remove_flow(dst)

    def simulate(self):
        print(f"Simulating network configuration for controller {self.name}...")
        for switch in self.switches.values():
            print(f"Switch {switch.name} flows: {switch.get_flows()}")


class Network:
    def __init__(self):
        self.controllers = {}
        self.switches = {}
        
    def add_controller(self, controller):
        self.controllers[controller.name] = controller
        
    def add_switch(self, switch):
        self.switches[switch.name] = switch
        
        for controller in self.controllers.values():
            controller.add_switch(switch)
    
    def connect_switches(self, switch_name1, switch_name2, bandwidth):
        if switch_name1 in self.switches and switch_name2 in self.switches:
            self.switches[switch_name1].connect(self.switches[switch_name2], bandwidth)
    
    def simulate(self):
        for controller in self.controllers.values():
            controller.simulate()


def main():
    network = Network()

    controller1 = Controller("Main_Controller")
    network.add_controller(controller1)

    switch1 = Switch("Switch_1")
    switch2 = Switch("Switch_2")
    switch3 = Switch("Switch_3")
    
    network.add_switch(switch1)
    network.add_switch(switch2)
    network.add_switch(switch3)

    network.connect_switches("Switch_1", "Switch_2", 100)
    network.connect_switches("Switch_2", "Switch_3", 200)
    
    controller1.configure_flow("Switch_1", "Switch_2", 5)
    controller1.configure_flow("Switch_2", "Switch_3", 3)

    network.simulate()
    print("Flow configuration complete.\n")
    
    # Simulating dynamic updates 
    time.sleep(2)
    print("Updating flows...")
    controller1.delete_flow("Switch_1", "Switch_2")
    controller1.configure_flow("Switch_1", "Switch_3", 1)
    network.simulate()


if __name__ == "__main__":
    main()