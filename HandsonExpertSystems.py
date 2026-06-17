from pyknow import *

class ComputerIssueExpert(KnowledgeEngine):

    @Rule(Fact(no_power=True))
    def power_issue(self):
        print("Forward Chaining: Diagnosis - Power Supply Problem")

    @Rule(Fact(blue_screen=True), Fact(slow_performance=True))
    def hardware_issue(self):
        print("Forward Chaining: Diagnosis - Overheating or Hardware Fault")

    @Rule(Fact(no_internet=True))
    def network_issue(self):
        print("Forward Chaining: Diagnosis - Network Problem")
   
    @Rule(Fact(blue_screen=True))
    def driver_issue(self):
        print("Forward Chaining: Suggestion - Check for Driver Issues")



def backward_chaining(facts, hypothesis):
    print("\nBackward Chaining Results:")

    if hypothesis == "Power Supply Problem":
        if facts.get("no_power"):
            print("Yes → Power Supply Problem")
        else:
            print("No → Conditions not met for Power Supply Problem")

    elif hypothesis == "Overheating or Hardware Fault":
        if facts.get("blue_screen") and facts.get("slow_performance"):
            print("Yes → Overheating or Hardware Fault")
        else:
            print("No → Conditions not met for Overheating or Hardware Fault")

    elif hypothesis == "Network Problem":
        if facts.get("no_internet"):
            print("Yes → Network Problem")
        else:
            print("No → Conditions not met for Network Problem")

    elif hypothesis == "Driver Issue":
        if facts.get("blue_screen"):
            print("Yes → Check for Driver Issues")
        else:
            print("No → Conditions not met for Driver Issue")

    else:
        print("Hypothesis not recognized.")

facts = {
    "no_power": True,
    "blue_screen": True,
    "slow_performance": True,
    "no_internet": False
}

method = input("Choose chaining method (forward/backward): ").lower()

if method == "forward":
    engine = ComputerIssueExpert()
    engine.reset()

    for key, value in facts.items():
        if value:
            engine.declare(Fact(**{key: True}))

    engine.run()

elif method == "backward":
    hypothesis = input("Enter hypothesis to test (e.g., 'Power Supply Problem'): ")
    backward_chaining(facts, hypothesis)

else:
    print("Invalid method selected. Choose 'forward' or 'backward'.")