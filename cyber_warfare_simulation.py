import random
import time
import json

class CyberAsset:
    def __init__(self, name, security_level):
        self.name = name
        self.security_level = security_level
        self.status = 'Active'

    def __str__(self):
        return f"{self.name} (Security level: {self.security_level}, Status: {self.status})"

class AttackStrategy:
    def __init__(self, name, damage, required_security_level):
        self.name = name
        self.damage = damage
        self.required_security_level = required_security_level

    def __str__(self):
        return f"Attack: {self.name} (Damage: {self.damage}, Required security level: {self.required_security_level})"

class CyberWarfareSimulation:
    def __init__(self):
        self.assets = []
        self.strategies = []
        self.results = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def add_strategy(self, strategy):
        self.strategies.append(strategy)

    def simulate_attack(self, asset, strategy):
        if asset.security_level < strategy.required_security_level:
            damage_done = strategy.damage
            asset.status = 'Compromised'
            self.results.append((asset, strategy, damage_done))
            print(f"Attack successful on {asset.name} using {strategy.name}. Damage: {damage_done}")
        else:
            print(f"Attack on {asset.name} using {strategy.name} failed. Security level adequate.")

    def run_simulation(self):
        for asset in self.assets:
            strategy = random.choice(self.strategies)
            self.simulate_attack(asset, strategy)
            time.sleep(1)  # Simulate time delay

    def report_results(self):
        report = {"results": []}
        for asset, strategy, damage in self.results:
            report["results"].append({
                "asset": asset.name,
                "strategy": strategy.name,
                "damage": damage,
                "status": asset.status
            })
        with open('simulation_report.json', 'w') as f:
            json.dump(report, f, indent=4)
        print("Results have been saved to 'simulation_report.json'.")

def create_sample_assets():
    return [
        CyberAsset("Server A", security_level=3),
        CyberAsset("Server B", security_level=2),
        CyberAsset("Workstation C", security_level=1)
    ]

def create_sample_strategies():
    return [
        AttackStrategy("SQL Injection", damage=5, required_security_level=1),
        AttackStrategy("Phishing", damage=3, required_security_level=2),
        AttackStrategy("DDoS", damage=10, required_security_level=0),
        AttackStrategy("Malware", damage=8, required_security_level=2)
    ]

def main():
    simulation = CyberWarfareSimulation()

    assets = create_sample_assets()
    strategies = create_sample_strategies()

    for asset in assets:
        simulation.add_asset(asset)

    for strategy in strategies:
        simulation.add_strategy(strategy)

    simulation.run_simulation()
    simulation.report_results()

if __name__ == "__main__":
    main()