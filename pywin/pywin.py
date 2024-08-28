from pywinauto.application import Application
from time import sleep
app = Application(backend="uia").start('notepad.exe').connect(title="Untitled - Notepad",timeout=10)
app.UntitledNotepad.print_control_identifiers()

def test_edit():
    edit =app.UntitledNotepad.child_window(title="Text Editor", auto_id="15", control_type="Edit").wrapper_object()
    edit.type_keys("writing to the notepad using pywin ",with_spaces=True)


def test_zoom():
    file = app.UntitledNotepad.child_window(title="View", control_type="MenuItem").wrapper_object()
    file.click_input()
    #app.UntitledNotepad.print_control_identifiers()
    zoom = app.UntitledNotepad.child_window(title="Zoom", control_type="MenuItem").click_input()
    #app.UntitledNotepad.print_control_identifiers()
    zoomin = app.UntitledNotepad.child_window(title="Zoom In	Ctrl+Plus", auto_id="34", control_type="MenuItem").click_input()

#def test_format():

def test_save():
    save = app.UntitledNotepad.child_window(title="File", control_type="MenuItem").click_input()
    app.UntitledNotepad.print_control_identifiers()
    saveas = app.UntitledNotepad.child_window(title="Save As...	Ctrl+Shift+S", auto_id="4", control_type="MenuItem").click_input()
    #app.UntitledNotepad.print_control_identifiers()
    name = app.UntitledNotepad.child_window(title="File name:", auto_id="FileNameControlHost", control_type="ComboBox")
    name.type_keys("file3")
    app.UntitledNotepad.Save.click()

