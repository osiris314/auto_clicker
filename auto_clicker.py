import pyautogui, time

repeat = 0
setup_wait = 5
x_position = 25
y_position = 1060
btw_clicks_wait = 1

time.sleep(setup_wait)

if repeat == 0:
    while True:
        pyautogui.click(x=x_position, y=y_position)
        time.sleep(btw_clicks_wait)
else:
    for x in range(repeat):
        pyautogui.click(x=x_position, y=y_position)
        time.sleep(btw_clicks_wait)