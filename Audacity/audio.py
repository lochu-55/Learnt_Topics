from pywinauto.application import Application
import time

# Provide the correct path to the Audacity executable
audacity_path = r"C:\Program Files\Audacity\audacity.exe"

# Launch Audacity
app = Application().start(audacity_path)

# Wait for Audacity to fully load (adjust the delay time as needed)
time.sleep(10)

# Get the Audacity main window
audacity_window = app.window(title='Audacity')

time.sleep(10)
# Access the "Edit" menu
#audacity_window.print_control_identifiers()
audacity_window.menu_select("File->Open")

open_window = app.Selectoneormorefiles
open_window.type_keys(r"C:\Users\vlab\Music\jyo.mp3")
open_window.Open.click()
