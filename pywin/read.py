from pywinauto.application import Application
app = Application().start("notepad.exe")
main_dlg = app["Untitled - Notepad"]

main_dlg.menu_select("File->Open")
open_dialog = app.Open
open_dialog.Edit.type_keys("jyo")
open_dialog.Open.click()
print(main_dlg.Edit.window_text())
