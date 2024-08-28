from pywinauto.application import Application

app = Application()
app.start("Notepad.exe")

def test_to_edit():
    app.Notepad.menu_select("File->new")
    app.Notepad.Edit.type_keys("hello friends\nwelcome to veda\nlearn explore and excel",with_spaces=True,with_newlines=True)
    app.Notepad.menu_select("File->Saveas")
    app.Saveas.type_keys("file10")
    app.Saveas.Save.click()

def test_to_read():
    app.Notepad.menu_select("File->open")
    app.Open.Edit.type_keys("file8")
#main.Open.open.click_input()
    app.Open.Open.click(double=True)
    app.Notepad.Edit.window_text()
    app.top_window().print_control_identifiers()
    app.Notepad.Edit.print_control_identifiers()
    print(app.Notepad.Edit.window_text())

#def test_find():
#    app.Notepad.menu_select("Edit->Find")

