from pywinauto import Application
import time

# Start Notepad application
app = Application(backend="uia").start("notepad.exe")
main_dlg =app.UntitledNotepad
# Access the main window
main_window = app.window(title="Untitled - Notepad")

# Type some text into Notepad
main_window.type_keys("Hello, Pywinauto!")

# Save the file (simulate pressing Ctrl + S)
main_window.type_keys("^s")  # ^ represents the Ctrl key

# Wait for a moment to ensure the "Save As" dialog is open
time.sleep(1)

# Access the "Save As" dialog using the uia backend
save_as_dialog = main_dlg.child_window(title="Save As", class_name="#32770")  # Adjust properties based on your system
save_as_dialog.wait('visible')  # Wait until the dialog is visible

# Perform actions on the "Save As" dialog, for example, set file name and save
save_as_dialog.Edit.set_edit_text("C:\\path\\to\\save\\file.txt")
save_as_dialog.Save.click()

# Wait for the save operation to complete
main_window.wait_not('exists', timeout=10)

# Close Notepad (optional)
app.kill()
