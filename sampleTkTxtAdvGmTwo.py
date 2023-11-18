scenarioChoice = [
            ["1choice1", "1choice2"],
            ["2choice1", "2choice2"],
            ["3choice1", "3choice2"],
            ["4choice1", "4choice2"],
            ["5choice1", "5choice2"],
        ]
print(scenarioChoice[0][1])
inputOne = input("1choice1 or 1choice2: ")

if inputOne == scenarioChoice[0][0]:
    print("you picked choice1")
elif inputOne == scenarioChoice[0][1]:
    print("you picked choice2")