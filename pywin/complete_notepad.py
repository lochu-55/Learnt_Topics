from pywinauto.application import Application
from time import sleep
app = Application().start("notepad.exe")
sleep(1)
main_dlg = app["Untitled - Notepad"]

def test_1():
    app.UntitledNotepad.print_control_identifiers()
    main_dlg.maximize()
    main_dlg.type_keys("hello guys welcome to pywin ... you can auto windows GUI applications using pywin\n",with_spaces=True,with_newlines=True)

#def test_read():
    #main_dlg.menu_select("File->open")

#def test_view_menuitem():
    #main_dlg.menu_select("View->Zoom")
    #sleep(2)
    #app.Zoom.ZoomIn.click_input()
    #sleep(2)
    #main_dlg.menu_select("View->Zoom")
    #sleep(2)
    #main_dlg.ZoomOut.click_input()
    #main_dlg.child_window(title="View", control_type="MenuItem").click_input()
    #main_dlg.print_control_identifiers()
    #main_dlg.child_window(title="Zoom", control_type="MenuItem").click_input()
    #main_dlg.print_control_identifiers()
    #main_dlg.child_window(title="Zoom In	Ctrl+Plus", auto_id="34", control_type="MenuItem").click_input()



def test_Font():
    main_dlg.menu_select("Format->Font")
    sleep(2)
    main_dlg.print_control_identifiers()
    dialog = app.Font
    sleep(2)
    # here we can use edit or combobox for selecting font, font style, size becoz editing option is there
    dialog.Edit.type_keys("")
    dialog.Edit.type_keys("calibri",pause=0.1)
    dialog.Edit2.type_keys("")
    dialog.Edit2.type_keys("Italic", pause=0.1)
    dialog.Edit3.type_keys("15")
    #here we cannot use edit becoz edit option is not there to select script
    dialog.ComboBox4.select("Greek")
    sleep(2)
    dialog.Ok.click_input()
    
def test_Find():
    main_dlg.menu_select("Edit->Find")
    sleep(2)
    Find_dialog = app.Find
    Find_dialog.Edit.type_keys("pywin")
    sleep(2)
    Find_dialog.FindNext.click_input()
    sleep(2)
    Find_dialog.close()

def test_pagesetup():
    
    main_dlg.menu_select("File->PageSetup")
    sleep(2)
    dialog = app.PageSetup
    sleep(2)
    dialog.Edit1.set_text("1")
    dialog.Edit2.set_text("2")
    dialog.Edit3.set_text("3")
    dialog.Edit4.set_text("4")
    dialog.Edit5.set_text("Welcome")
    dialog.Edit6.set_text("By sri jyothsna")
    dialog.Ok.click()


def test_print():
    main_dlg.menu_select("File->Print")
    print_dialog = app.Print
    sleep(1)
    print_dialog.Print.click_input()
    sleep(1)
    #if you want to save as pdf with file name
    #save = app.SavePrintOutputAs
    #save.type_keys("print1")
    #sleep(2)
    #save.Save.click()
    #save.close()

def test_Save():
    main_dlg.menu_select("File -> SaveAs")
    save_dialog = app.SaveAS
    save_dialog.type_keys("jyo2")
    save_dialog.Save.click()
    #save_dialog.close()
    app.kill()

