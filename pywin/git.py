from pywinauto import Application
import time

# Start the Notepad application
app = Application(backend="uia").start("notepad.exe")

# Access the main window
main_window = app.window()

# Type some text into the Notepad editor
main_window.type_keys("Hello, Pywinauto!")

# Save the file (simulate pressing Ctrl + S)
main_window.type_keys("^s")  # ^ represents the Ctrl key

# Wait for the "Save As" dialog to appear (you may need to adjust conditions)
save_as_dialog = app.window(title="Save As", class_name="#32770")

# Specify the file name and save the file
save_as_dialog.Edit.set_edit_text("C:\\path\\to\\save\\file.txt")  # Replace with your desired file path
save_as_dialog.Save.click()

# Wait for the save operation to complete (you may need to adjust conditions)
main_window.wait_not("exists", timeout=10)

# Close the Notepad application (optional)
app.kill()

