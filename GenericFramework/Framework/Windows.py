from Framework.Base import WinGuiAuto


class Notepad(WinGuiAuto):
    def __init__(self, filename):
        super().__init__(filename)
        self.main_window = self.app.UntitledNotepad

    def enter_text(self, text):
        self.main_window.Edit.type_keys(text)

    def minimize_window(self):
        self.main_window.minimize()

    def maximize_window(self):
        self.main_window.maximize()

    def save_file(self, file_path):
        self.main_window.menu_select("File -> Save As")
        save_dialog = self.main_window.window(title="Save As")
        save_dialog.child_window(title="File name:", auto_id="1001", control_type="Edit").set_edit_text(file_path)
        save_dialog.Save.click()
