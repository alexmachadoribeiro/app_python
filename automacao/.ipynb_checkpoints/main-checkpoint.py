import pyautogui as auto

auto.PAUSE = 0.5

auto.press("win")
auto.write("firefox")
auto.press("enter")
auto.hotkey("alt", "space")
auto.press("x")
auto.write("python")
auto.press("enter")
auto.hotkey("ctrl", "t")
auto.write("sistemafibra.org.br")
auto.press("enter")