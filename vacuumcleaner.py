from time import sleep

def simpleVacuumCleanerAgent(percept):
    position, status = percept
    if status == "Dirty":
        return "Suck"
    elif position == "A":
        return "Right"
    elif position == "B":
        return "Left"

def main():
    state = {"A" : "Dirty", "B": "Dirty"}
    currentPosition = "A"
    currentStatus = state[currentPosition]
    while True:
        print("State:", state)
        print("Vacuum Cleaner Location:", currentPosition)
        percept = [currentPosition, currentStatus]
        action = simpleVacuumCleanerAgent(percept)
        sleep(2)
        print("Action:", action)
        if action == "Suck":
            state[currentPosition] = "Clean"
        elif action == "Right":
            currentPosition = "B"
        elif action == "Left":
            currentPosition = "A"
        currentStatus = state[currentPosition]

main()
