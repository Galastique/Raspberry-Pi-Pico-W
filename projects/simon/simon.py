from machine import Pin
from utime import sleep
from random import randint

#Buttons
buttonRed = Pin(18, Pin.IN, Pin.PULL_UP)
buttonYellow = Pin(17, Pin.IN, Pin.PULL_UP)
buttonGreen = Pin(16, Pin.IN, Pin.PULL_UP)

#Lights
ledRed = Pin(21, Pin.OUT)
ledYellow = Pin(20, Pin.OUT)
ledGreen = Pin(19, Pin.OUT)
delays = [0.5, 0.25, 0.15] #for difficulties

#Resets lights
def resetLights():
    ledRed.off()
    ledYellow.off()
    ledGreen.off()
    sleep(1)

#New round
def startRound(previousPattern, playerScore):
    sequenceList = generateSequence(previousPattern)
    playerSequence = playerTurn(sequenceList)
    compareSequences(sequenceList, playerSequence, playerScore)

#Generates color pattern
def generateSequence(previousPattern):
    newSequenceList = previousPattern
    newSequenceList.append(["red", "yellow", "green"][randint(0, 2)])
    showSequence(newSequenceList)
    return newSequenceList

#Shows color pattern to repeat
def showSequence(sequenceList):
    for color in sequenceList:
        if color == "red":
            ledRed.on()
        elif color == "yellow":
            ledYellow.on()
        elif color == "green":
            ledGreen.on()
        sleep(difficulty)
        ledRed.off()
        ledYellow.off()
        ledGreen.off()
        sleep(0.10)

#Player turn (repeat sequence)
def playerTurn(sequenceList):
    redButtonIsPressed = yellowButtonIsPressed = greenButtonIsPressed = False #this will detect each individual button presses instead of counting the same one multiple times
    buttonPressList = []
    try:
        while len(buttonPressList) < len(sequenceList) and len(buttonPressList) <= 20:
            #Red button/light
            if not buttonRed.value() and not redButtonIsPressed:
                redButtonIsPressed = True
                buttonPressList.append("red")
                ledRed.on()
                sleep(difficulty)
            elif buttonRed.value():
                redButtonIsPressed = False
            
            #Yellow button/light
            if not buttonYellow.value() and not yellowButtonIsPressed:
                yellowButtonIsPressed = True
                buttonPressList.append("yellow")
                ledYellow.on()
                sleep(difficulty)
            elif buttonYellow.value():
                yellowButtonIsPressed = False
            
            #Green button/light
            if not buttonGreen.value() and not greenButtonIsPressed:
                greenButtonIsPressed = True
                buttonPressList.append("green")
                ledGreen.on()
                sleep(difficulty)
            elif buttonGreen.value():
                greenButtonIsPressed = False
            
            ledRed.off()
            ledYellow.off()
            ledGreen.off()
    except:
        pass
    return buttonPressList

#Compares sequences
def compareSequences(sequenceList, playerSequence, playerScore):
    if sequenceList == playerSequence:
        sleep(1)
        playerScore += 1
        startRound(sequenceList, playerScore)
    else:
        endOfGame(playerName, playerScore)

#End of the game
def endOfGame(playerName, playerScore):
    print("Fin de la partie!\n")
    for x in range(6):
        ledRed.toggle()
        ledYellow.toggle()
        ledGreen.toggle()
        sleep(0.25)
    print(f"{playerName} a eu un score de: {playerScore} points!")


#Simon game
def init():
    #Resets default values
    resetLights()
    global playerName
    global playerScore
    global difficulty
    playerName = input("Veuillez entrer votre nom pour commencer\n>")
    playerScore = 0
    difficulty = 0
    
    print("\n==Jeu de Simon==\nUne séquence va apparaitre à l'aide des lumières LEDs. Vous devez répéter la séquence à l'aide des boutons correspondants. La séquence va être de plus en plus longue, jusqu'au moment où vous perdez ou au moment ou vous réussissez à gagner une séquence d'une longueur de 20.\n")

    #Sets difficulty
    print("\nVeuillez choisir votre difficulté à l'aide des boutons (facile, moyen, difficile)\n")
    while difficulty == 0:
        if not buttonRed.value():
            difficulty = delays[0]
            ledRed.on()
            print("Vous avez choisit: facile")
        elif not buttonYellow.value():
            difficulty = delays[1]
            ledYellow.on()
            print("Vous avez choisit: moyen")
        elif not buttonGreen.value():
            difficulty = delays[2]
            ledGreen.on()
            print("Vous avez choisit: difficile")
        sleep(0.05)
    
    print("\nLe jeu va maintenant commencer...\n\n")
    sleep(0.25)

    resetLights()
    startRound([], playerScore)
    
    #Checks if players wants to play again
    playAgain = input("\nVoulez-vous rejouer? (y/n)\n>")
    
    if playAgain.lower() == "y":
        init()

#Starts program
init()