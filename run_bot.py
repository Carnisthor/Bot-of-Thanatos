from pyautogui import *
from datetime import datetime
import pyautogui
import time
import keyboard
import win32api, win32con


def printLive(infoMessage, currentRun, failedRuns, start):
    LINE_UP = "\033[1A"
    LINE_CLEAR = "\x1b[2K"

    # Clean previous status
    for i in range(3):
        print(LINE_UP, end=LINE_CLEAR)

    elapsedTime = datetime.now() - start

    # Print new status
    print("INFO: ", infoMessage)
    print("Current run: ", currentRun, " ; Failed runs: ", failedRuns)
    print("Bot is running for: ", elapsedTime)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(2)


# Moves the character using the key mapping for 'force move'
def move(x, y, hotkey="o"):
    time.sleep(0.5)
    win32api.SetCursorPos((x, y))
    keyboard.press(hotkey)
    time.sleep(0.1)
    keyboard.release(hotkey)
    time.sleep(2)


# Presses a button and waits for it to take effect
def pressButton(button):
    keyboard.press(button)
    time.sleep(0.1)
    keyboard.release(button)
    time.sleep(1)


def exitGame():
    click(319, 20)
    click(963, 601)
    click(898, 599)


def stayInTomb(currentRun, failedRuns, start):
    for i in range(10):
        # Check if character is really in the tomb by looking at the minimap
        try:
            r, g, b = pyautogui.pixel(1832, 26)
            if r != 0 and g != 0 and b != 0:
                printLive("Character not in tomb", currentRun, failedRuns, start)
                return 1
        except:
            printLive(
                "Minimap was undetecable this time", currentRun, failedRuns, start
            )

        minutesInTomb = str(i) + " minute(s) waited"
        printLive(minutesInTomb, currentRun, failedRuns, start)
        time.sleep(60)
    return 0


def startRun():
    # All positions on the screen which mark the way into the tumb
    positions = (
        (425, 18),
        (1407, 72),
        (663, 354),
        (663, 353),
        (878, 53),
        (1711, 167),
        (1711, 168),
        (1309, 390),
        (1132, 185),
        (1131, 185),
        (422, 381),
        (422, 380),
        (653, 102),
        (474, 398),
        (578, 316),
        (578, 315),
        (578, 316),
        (578, 315),
        (401, 386),
        (401, 387),
        (474, 92),
        (751, 424),
        (211, 157),
        (211, 158),
        (211, 157),
        (566, 119),
    )

    # Select the character
    click(1737, 132)

    # Start the game
    click(1758, 1050)

    time.sleep(10)

    # Activate buffs
    pressButton("1")
    pressButton("2")
    pressButton("3")

    # Move to the tumb
    for position in positions:
        move(position[0], position[1])


# Actual execution of the Thanatos Bot
# Having a buffer to navigate to the game before the bot is executed
welcomeMessage = """###########################################################################\n
    ###################### Titan Quest - Bot of Thanatos ######################\n
    ###########################################################################\n
    \n\n\n"""
print(welcomeMessage)
runCounter = 1
failedRuns = 0
startTime = datetime.now()
printLive("Starting Bot of Thanatos", runCounter, failedRuns, startTime)
# Waiting shortly for user to navigate to TQ
time.sleep(10)

while True:
    printLive("Moving into the tumb", runCounter, failedRuns, startTime)
    # Move to acutal position
    startRun()
    printLive("Moved into position", runCounter, failedRuns, startTime)

    # Sleep until 10 minutes have passed
    failedRuns = stayInTomb(runCounter, failedRuns, startTime) + failedRuns

    # Exit the game
    exitGame()
    printLive("Completed run", runCounter, failedRuns, startTime)
    runCounter = runCounter + 1