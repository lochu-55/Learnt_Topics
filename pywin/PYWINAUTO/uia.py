import os.path
from pywinauto.application import Application

from time import sleep


class note:

    def open_npd(self):
        self.app = Application(backend="uia").start("notepad.exe")
        self.main_dlg = self.app.UntitledNotepad
        self.notepad_window = self.app.top_window()

    def new_file(self):
        self.notepad_window.menu_select("File->New")


    def edit(self):
        self.notepad_window.Edit.type_keys("hello guys welcome to notepad you can edit ur text using notepad,you can use font styles in notepad",with_spaces=True)
        sleep(1)

    def close_npd(self):
        self.app.kill()

    def font(self):
        self.notepad_window.menu_select("Format->Font")

        font_window = self.notepad_window.child_window(title="Font", control_type="Window")
        font_window.Edit1.set_text("")
        font_window.Edit1.type_keys("calibri")
        sleep(1)
        font_window.Edit2.set_text("")
        sleep(1)
        font_window.Edit2.type_keys("italic")
        font_window.Edit3.set_text("")
        sleep(1)
        font_window.Edit3.set_text("15")
        sleep(1)
        font_window.Ok.click()
        sleep(2)

    def find(self):
        self.notepad_window.menu_select("Edit->Find")

        sleep(2)
        find_window = self.notepad_window.child_window(title="Find", control_type="Window")
        find_window.Edit.set_text("")
        find_window.Edit.type_keys("notepad")
        sleep(1)
        print("class -----", find_window.class_name())
        checkbox1 = find_window.CheckBox
        print("state------",checkbox1.get_toggle_state())
        if checkbox1.get_toggle_state()==1:
            print("checked")
        else:
            print("checking the box1")
            checkbox1.click()

        checkbox2 = find_window.CheckBox2
        print("state------", checkbox1.get_toggle_state())
        if checkbox2.get_toggle_state()==1:
            print("checked")
        else:
            print("checking the box2")
            checkbox2.click()
        radiobutton1 = find_window.RadioButton
        print("radio button state",radiobutton1.is_enabled())
        radiobutton1.click()
        sleep(2)
        find_window.FindNext.click()
        sleep(1)
        find_window.FindNext.click()
        sleep(1)
        find_window.FindNext.click()
        sleep(1)
        find_window.close()

    def replace(self):
        self.notepad_window.menu_select("Edit->Replace")
        #self.notepad_window.print_control_identifiers()
        replace_dialog = self.notepad_window.child_window(title="Replace", control_type="Window")
        replace_dialog.Edit1.set_text("")
        sleep(1)
        replace_dialog.Edit1.type_keys("guys")
        sleep(1)
        replace_dialog.Edit2.set_text("")
        sleep(1)
        replace_dialog.Edit2.type_keys("everyone")
        sleep(1)
        replace_dialog.ReplaceAll.click()
        sleep(2)
        replace_dialog.close()

    def time(self):
        self.notepad_window.menu_select("Edit->Time/Date")
        sleep(1)

    def select_all(self):
        self.notepad_window.menu_select("Edit->SelectAll")
        sleep(1)
        self.notepad_window.menu_select("Edit->Delete")
        sleep(1)
        self.notepad_window.menu_select("Edit->undo")
        sleep(1)

    def view(self):
        self.notepad_window.child_window(title="View", control_type="MenuItem").click_input()
        self.notepad_window.child_window(title="Zoom", control_type="MenuItem").click_input()
        #self.notepad_window.print_control_identifiers()
        self.notepad_window.child_window(title="Zoom In	Ctrl+Plus", auto_id="34", control_type="MenuItem").click_input()
        self.notepad_window.child_window(title="Zoom Out	Ctrl+Minus", auto_id="35", control_type="MenuItem")

    def about(self):
        self.notepad_window.menu_select("Help->About Notepad")
        sleep(1)
        #self.notepad_window.print_control_identifiers()
        self.notepad_window.child_window(title="About Notepad", control_type="Window").close()
        # self.app.UntitledNotepad.Ok.click_input()
        sleep(1)
        # self.notepad_window.menu_select("Help->View Help")
        # self.notepad_window.menu_select("Help->Send Feedback")

    def pagesetup(self):
        self.notepad_window.menu_select("File->PageSetup")
        #self.notepad_window.print_control_identifiers()
        pagesetup_window = self.notepad_window.child_window(title="Page Setup", control_type="Window")

        combo_box = pagesetup_window.ComboBox1
        combo_box.select("A4")
        sleep(1)

        radio_button = pagesetup_window.RadioButton2
        radio_button.click()
        sleep(1)
        pagesetup_window.Edit1.set_text("10")
        sleep(1)
        pagesetup_window.Edit2.set_text("15")
        sleep(1)
        pagesetup_window.Edit3.set_text("20")
        sleep(1)
        pagesetup_window.Edit4.set_text("25")
        pagesetup_window.Edit5.set_text("")
        sleep(1)
        pagesetup_window.Edit5.set_text("welcome")
        sleep(1)
        pagesetup_window.Edit6.set_text("")
        sleep(1)
        pagesetup_window.Edit6.set_text("By Sri Jyothsna")
        sleep(1)
        pagesetup_window.Ok.click()

    def print(self):
        self.notepad_window.menu_select("File->Print")
        #self.notepad_window.print_control_identifiers()
        print_window = self.notepad_window.child_window(title="Print", control_type="Window")
        print_window.Edit5.set_text("3")
        print_window.Print.click()

    def saveas(self):
        self.notepad_window.menu_select("File->Save")
        #self.notepad_window.SaveAs.print_control_identifiers()
        save_as_dialog = self.notepad_window.child_window(title="Save As", control_type="Window")
        print("class name-----", save_as_dialog.class_name())

        save_as_dialog.Edit.type_keys("pywin1")
        save_as_dialog.Save.click()
        #self.notepad_window.SaveAs.print_control_identifiers()
        sleep(1)
        confirm_save = self.notepad_window.child_window(title="Confirm Save As", control_type="Window")
        if confirm_save.is_enabled():
            print("file exists ,give another name.....")
            confirm = self.notepad_window.child_window(title="Confirm Save As", control_type="Window")
            confirm.Yes.click_input()

        #save_as_dialog.Edit.set_text("")
        #save_as_dialog.Save.click()

    def open(self):
        self.notepad_window.menu_select("File->Open")
        #self.notepad_window.Open.print_control_identifiers()
        open_window = self.notepad_window.child_window(title="Open", control_type="Window")
        file_name = r"C:\Users\vlab\Downloads\sri.txt"
        open_window.type_keys(file_name+"{ENTER}")
        #open_window.ComboBox2.select(1)
        #open_window.Open.click()
        print("\nthe content in the file is\n", self.app.Notepad.Edit.get_value())

    """def cut_paste(self):
        self.notepad_window.menu_select("Edit->Copy")
        self.notepad_window.menu_select("Edit->Cut")
        sleep(2)
        self.notepad_window.menu_select("Edit->Paste")
        sleep(2)"""



    

    

    

    

    
    
