import time
import pyautogui
from ahk import AHK

ahk = AHK(executable_path="AutoHotkeyU64.exe")

print("Sherbscape Autowarper")
print("probably still works, if not dm me")
print("open source on my github mrsherbs")
print("swap to your roblox window to start, you have to keep it in focus")

while True:
    if ahk.find_window_by_title("Roblox") == ahk.get_active_window():
        break

while True:
    ahk.run_script("Send, {Space Up}")
    ahk.run_script("Send, {Space Down}")

    time.sleep(0.5)

    s = pyautogui.screenshot()
    star_Pos = None
    for pos in pyautogui.locateAllOnScreen("star.png", confidence=0.8):
        center = pyautogui.position(pos.left + pos.width/2, pos.top + pos.height/2)
        pixel = pyautogui.screenshot().getpixel((center.x, center.y))

        if 70 > pixel[2] > 55:
            print(pixel[2])
            star_Pos = center
            break

    if not star_Pos:
        break

    while True:
        correct_selected_location = pyautogui.position(star_Pos.x + 150, star_Pos.y)

        if pyautogui.pixelMatchesColor(correct_selected_location.x, correct_selected_location.y, (90, 90, 85)):
            break
        else:
            ahk.run_script("-Y.ahk")

    ahk.run_script("Send, {Space Up}")

    while True:
        try:
            pyautogui.locateCenterOnScreen("warping.png", confidence=0.9)
            break
        except:
            pass

    while True:
        try:
            pyautogui.locateCenterOnScreen("speed.png", confidence=0.8)
            break
        except:
            pass

    time.sleep(2)
