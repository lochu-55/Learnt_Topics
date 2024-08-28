
from pywinauto import Application
import time
import pywinauto.mouse
from time import sleep
from pywinauto.mouse import move


# Start Paint
app = Application().start("mspaint.exe")

# Connect to the Paint window
paint_window = app["Untitled - Paint"]

# Wait for Paint to be ready (adjust sleep time as needed)
time.sleep(2)



# Move the mouse cursor to coordinates (100, 100)
move(coords=(500, 500))
sleep(3)
pywinauto.mouse.scroll(coords=(50, 30), wheel_dist=10)