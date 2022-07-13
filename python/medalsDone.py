medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]

def createMedalTable(results):
    # Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point
    resultsTable = {} # Initialise empty dict to hold results table
    for result in results: # Loop through each result in results
        for team in result["podium"]: # Loop through each team on the podium
            if team.split(".")[0] == '1': # If they came first...
                try:
                    resultsTable[team.split(".")[1]] = resultsTable[team.split(".")[1]] + 3 # Add 3 points to their score
                except KeyError: # Or if the team has no points yet...
                    resultsTable[team.split(".")[1]] = 3 # Set their initial score as 3 points
            if team.split(".")[0] == '2':
                try:
                    resultsTable[team.split(".")[1]] = resultsTable[team.split(".")[1]] + 2
                except KeyError:
                    resultsTable[team.split(".")[1]] = 2
            if team.split(".")[0] == '3':
                try:
                    resultsTable[team.split(".")[1]] = resultsTable[team.split(".")[1]] + 1
                except KeyError:
                    resultsTable[team.split(".")[1]] = 1
    return resultsTable # Return the results table

def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable
