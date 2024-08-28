from pywinauto import Application,Desktop

app = Application().start("Calc.exe")
dlg = Desktop().Calculator
dlg.type_keys("9+9=")
dlg.print_control_identifiers()
