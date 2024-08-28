from pywinauto.application import Application
app = Application().start("notepad.exe")
main_dlg = app.UntitledNotepad
import os
from time import sleep

notepad_window = app.top_window()
notepad_window.maximize()

notepad_window.Edit.set_text("hello welcome to notepad u can type ur text here and edit ur text with beautiful fonts and font styles")
#notepad_window.Edit.type_keys("hello")

def test_font():
    notepad_window.menu_select("Format->Font")
    sleep(2)
    font_dialog = app.Font

    print("existing font",font_dialog.Edit.window_text())
    font_dialog.Edit.set_text("Arial")
    sleep(2)
    print("After change",font_dialog.Edit.window_text())

    print("existing font style",font_dialog.ComboBox2.window_text())
# type keys is used when combobox is used it is GUI OR WRAPPER METHOD if we use set_text it generates error
    font_dialog.ComboBox2.type_keys("Bold")
    sleep(2)
    print("After change",font_dialog.ComboBox2.window_text())

    print("existing font size",font_dialog.ComboBox3.window_text())
    font_dialog.ComboBox3.type_keys("20")
    sleep(2)
    print("After change",font_dialog.ComboBox3.window_text())

    font_dialog.Ok.click()

def test_pagesetup():

    notepad_window.menu_select("File->PageSetup")
    sleep(2)
    page_setup_dialog = app.PageSetup

# to select dropdowns we have to open dialog then we have to select by using text like here A4 is the dropdown element
    dropdown = page_setup_dialog.ComboBox1
    dropdown.select("A4")
    sleep(2)
#dropdown = page_setup_dialog.ComboBox2
#dropdown.select("Automatically Select")

# to click radio buttons first we have to open dialog then we have to select which numbered radio button have to be on
    button = page_setup_dialog.RadioButton2
    sleep(2)
    button.click()

    print("existing",page_setup_dialog.Edit1.window_text())
    page_setup_dialog.Edit1.set_text("5")
    sleep(2)
    print("After change",page_setup_dialog.Edit1.window_text())

    print("existing",page_setup_dialog.Edit2.window_text())
    page_setup_dialog.Edit2.set_text("10")
    sleep(2)
    print("After change",page_setup_dialog.Edit2.window_text())


    print("existing",page_setup_dialog.Edit3.window_text())
    page_setup_dialog.Edit3.set_text("15")
    sleep(2)
    print("After change",page_setup_dialog.Edit3.window_text())

    print("existing",page_setup_dialog.Edit4.window_text())
    page_setup_dialog.Edit4.set_text("20")
    sleep(2)
    print("After change",page_setup_dialog.Edit4.window_text())

    print("existing",page_setup_dialog.Edit5.window_text())
    page_setup_dialog.Edit5.set_text("")
    sleep(1)
    page_setup_dialog.Edit5.set_text("Welcome")
    sleep(2)
    print("After change",page_setup_dialog.Edit5.window_text())

    print("existing",page_setup_dialog.Edit6.window_text())
    page_setup_dialog.Edit6.set_text("")
    sleep(1)
    page_setup_dialog.Edit6.set_text("Thank you")
    sleep(2)
    print("After change",page_setup_dialog.Edit6.window_text())
    page_setup_dialog.Ok.click()



def test_find():
    notepad_window.menu_select("Edit->FindNext")
    edit_dialog = app.FindNext
    edit_dialog.Edit.set_text("notepad")
    sleep(1)

    radio_button = edit_dialog.RadioButton2
    radio_button.click()
    sleep(1)
    check_box1 = edit_dialog.CheckBox1
    if check_box1.is_checked():
        print("Ticked match case")
    else:
        check_box1.check()
    sleep(2)
    check_box2 = edit_dialog.CheckBox2
    if check_box2.is_checked():
        print("Ticked wrap around")
    else:
        check_box2.check()
    sleep(2)
    edit_dialog.FindNext.click()
    edit_dialog.close()

def test_replace():
    notepad_window.menu_select("Edit->Replace")
    replace_dialog = app.Replace
    sleep(2)
    replace_dialog.Edit1.set_text("")
    replace_dialog.Edit1.set_text("hello")
    sleep(2)
    replace_dialog.Edit2.set_text("")
    replace_dialog.Edit2.set_text("replaced")
    replace_dialog.ReplaceAll.click()
    sleep(2)
    replace_dialog.close()

#notepad_window.menu_select("View->ZoomIn")

def test_print():

    notepad_window.menu_select("File->Print")
    print_dialog = app.Print
    box = print_dialog.CheckBox
    box.check()
    #box.uncheck()
    if box.is_checked():
        print("enabled")
    else:
        print("not enabled")

    print_dialog.Edit1.set_text("print")
    sleep(2)
    print_dialog.Edit2.set_text("HYD")
    sleep(2)
    print_dialog.Edit3.set_text("printing")
    sleep(2)
# this will click print button as it is 3 rd button in print dialog you can also print like this
#b = print_dialog.Button3
#b.click()
    if print_dialog.Edit4.is_enabled():
        print("enabled")
    else:
        print("not")
    print_dialog.Edit5.set_text("4")
    sleep(2)
    print_dialog.Print.click_input()

#to save file in particular path use os.path.join(os.path.expanduser("~"),"your foldername","filename")
    save_as_dialog = app.SavePrintOutputAs
#path= "D:\\print1"
#save_as_dialog.Edit.set_text(path)
    file_path = os.path.join(os.path.expanduser("~"), "Downloads","NewFolder", "print4")
    save_as_dialog.Edit.set_text(file_path)
    sleep(2)
    folder_path = os.path.dirname(file_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    sleep(2)
    checkbox = save_as_dialog.ComboBox2
    checkbox.select(1)
    sleep(1)
    save_as_dialog.Save.click()
    save_as_dialog.close()
    app.kill()
#printer = print_dialog.GroupBox
#radio = printer.RadioButton1
#radio.select("Microsoft")"""


"""def test_save():

    notepad_window.menu_select("File->Save")
    save_as_dialog = app.SaveAs
    sleep(1)
    print("the existing name",save_as_dialog.Edit.window_text())
    file_path = os.path.join(os.path.expanduser("~"),"Downloads","file2")
    save_as_dialog.Edit.set_text("")
    save_as_dialog.Edit.set_text(file_path)
    sleep(1)
    print("After change",save_as_dialog.Edit.window_text())
    save_as_dialog.Save.click_input()"""

