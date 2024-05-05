# Bot-of-Thanatos

This repo is related to the game Titan Quest. There is a achievement called "Avatar of Thanatos" whichr requires you to kill a high amount of enemies. To increase the speed I wrote a small bot to auto farm for you.

# Getting started

In order to use the bot, you need to do prepare a couple of things. Start by cloning or downloading the repository.

## Import Firewall

I recommend to import my Hero `Firewall`. The bot is programmed with his resistances and walk speed in mind. If you chose your own hero, you might need to fine-tune the script accordingly to make it work.

You can simply copy the character file `_Firewall` into your game files. Mine were located at 
> C:\Users\<my_windows_user>\Documents\My Games\Titan Quest - Immortal Throne\SaveData\Main.

After you have copied the file, start the game and you should find him ready to be selected.

## Game settings

The scripts requires some specific in game settings in order to work.
<ol>
    <li>Screen Resolution is fixed at 1920 x 1080 (Widescreen)</li>
    <li>Window Mode is set to Full screen</li>
    <li>HUD Size is set to Normal</li>
    <li>The Keybinding for Force Move is set to 'O'</li>
</ol>

## Install Python and dependencies

The bot is written in Python. You need to install the latest version: https://www.python.org/

After you have installed it, open a Terminal window and install the dependencies:
> pip install pyautogui
> pip install pyscreeze
> pip install Pillow
> pip install Image
> pip install PyWin32

Congrats! You should be good to go to use the bot.

# Using the bot

Start Titan Quest and select Firewall as a character. Now press Esc and go back to the main menu.
You can now start the bot. Navigate into the repository and execute
> python run_bot.py

You have about 15 seconds before anything will start to happen. Navigate back to Titan Quest and you will see that the character is being moved on its own.

Note that the script is acutally moving the mouse and uses the keyboard. So while it is running, you should not use the PC for anything else or your mouse will click randomly from time to time. I recommend to let it run when you are at work or over night.

When you want to give it a break, open the windows terminal windows again. You will find some stats there like run counter and time. You can terminte the bot with Ctrl + C.