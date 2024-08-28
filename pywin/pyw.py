#from pywin import application

from pywinauto import findwindows
# Start Notepad application
#app = application.Application().start("notepad.exe")
"""
# Wait for the Notepad window to be ready
main_window = app.window(title="Untitled - Notepad")
main_window.wait("ready")

# Get the class name of the Notepad window
class_name = main_window.class_name()
print("Class Name of Notepad:", class_name)



# Get the top-level window
top_window = findwindows.find_window(title="UntitledNotepad", class_name="Notepad")

# Print the window handle (HWND)
print("Top Window Handle:", top_window)

# Alternatively, you can use top_window() function to get the top-level window directly
#top_window_direct = findwindows.top_window()

# Print the window handle (HWND) obtained using top_window()
#print("Top Window Handle (using top_window()):", top_window_direct)
"""

"""from pywin import findwindows

# Specify criteria to identify the window
criteria = {'title': 'Untitled - Notepad', 'class_name': 'Notepad'}

# Find the window based on the specified criteria
notepad_window = findwindows.find_window(**criteria)

# Print the window handle (HWND)
print("Notepad Window Handle:", notepad_window)
"""

"""
from pywin import application

# Start Notepad application
app = application.Application().start("notepad.exe")

# Wait for the Notepad window to be ready
main_window = app.window(title="Untitled - Notepad")
main_window.wait("ready")

# Check if the Notepad window exists
if main_window.exists():
    print("Notepad window exists.")
else:
print("Notepad window does not exist.")
"""

"""import pywin.mouse
from time import sleep
from pywin.mouse import move

# Move the mouse cursor to coordinates (100, 100)
move(coords=(1200, 300))
sleep(3)
pywin.mouse.scroll(coords=(500, 300), wheel_dist=10)

"""

from pywinauto.keyboard import send_keys

# Send the string "Hello, Pywinauto!" to the currently focused window
send_keys("Hello, Pywinauto!")

# Send the Enter key
send_keys("{ENTER}")

# Send a combination of keys
send_keys("^a")  # Press Ctrl+A (Select All)

# Send keys with a delay between each key press
send_keys("Hello, Pywinauto!", with_spaces=True, pause=0.1)


