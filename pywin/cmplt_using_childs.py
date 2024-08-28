from pywinauto.application import Application
from time import sleep

app = Application(backend="uia").start("notepad.exe",timeout=30)
notepad = app.UntitledNotepad
notepad.child_window(title="Maximize", control_type="Button").click_input()
notepad.print_control_identifiers()

def test_text():
    send_text =notepad.child_window(title="Text Editor", auto_id="15", control_type="Edit")
    send_text.type_keys(" hello welcome to pywin you can automate windows GUI applications using pywin",with_spaces=True)

def test_edit_menuitem():
    edit = notepad.child_window(title="Edit", control_type="MenuItem").wrapper_object()
    edit.click_input()
    notepad.print_control_identifiers()
    notepad.child_window(title="Find...	Ctrl+F", auto_id="21", control_type="MenuItem").click_input()
    txt = notepad.child_window(title="Find what:", auto_id="1152", control_type="Edit").wrapper_object()
    txt.type_keys("pywin")
    notepad.print_control_identifiers()


    checkbox1 = notepad.child_window(title="Match case", auto_id="1041", control_type="CheckBox")
    #is_enabled = checkbox1.is_enabled()
    #sleep(2)
    #print(is_enabled)
    #if is_enabled:
    #    print("enabled")
    #else:
    checkbox1.click_input()
    sleep(2)
    checkbox2 = notepad.child_window(title="Wrap around", auto_id="1042", control_type="CheckBox")
    #is_enabled =  checkbox2.is_enabled()
    #print(is_enabled)
    #if is_enabled:
    #    print("enabled")
    #else:
    checkbox2.click_input()

    notepad.child_window(title="Up", auto_id="1056", control_type="RadioButton").click_input()

    find = notepad.child_window(title="Find Next", auto_id="1", control_type="Button").wrapper_object()
    sleep(2)
    find.click_input()

def test_view_menuitem():
    notepad.child_window(title="View", control_type="MenuItem").click_input()
    notepad.print_control_identifiers()
    notepad.child_window(title="Zoom", control_type="MenuItem").click_input()
    notepad.print_control_identifiers()
    notepad.child_window(title="Zoom In	Ctrl+Plus", auto_id="34", control_type="MenuItem").click_input()

def test_file_menuitem():
    menu_file =notepad.child_window(title="File", control_type="MenuItem")
    menu_file.click_input()
    #notepad.print_control_identifiers()

    saveas = notepad.child_window(title="Save As...	Ctrl+Shift+S", auto_id="4", control_type="MenuItem").wrapper_object()
    saveas.click_input()
    #notepad.print_control_identifiers()

    file_name= notepad.child_window(title="File name:", auto_id="FileNameControlHost", control_type="ComboBox")
    file_name.type_keys("pywinauto12.txt")

    save = notepad.child_window(title="Save", auto_id="1", control_type="Button")
    save.click_input()
    app.kill()"""