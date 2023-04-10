import pyautogui as pag
import time
import webbrowser
import array
import keyboard

arrayinfo = ['https://cdn.krnl.place/getkey',
             'https://cdn.krnl.place/getkey_games',
             'https://cdn.krnl.place/getkey_interface',
             'https://cdn.krnl.place/getkey_scripts',
             'https://cdn.krnl.place/getkey.php']
i = 0

webbrowser.open_new(arrayinfo[i])
time.sleep(9)
while i < 4:

    time.sleep(4)
    pag.click(823,243)
    time.sleep(2)
    pag.click(823,318)
    time.sleep(2)
    keyboard.press_and_release('ctrl+w')
    time.sleep(25)
    i = i+1
    
    webbrowser.open_new_tab(arrayinfo[i])

time.sleep(2.5)
pag.doubleClick(815,360)
keyboard.press_and_release('ctrl+c')

# MADE BY CRYSTALFAMOUS:)
