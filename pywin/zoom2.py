from pywinauto.application import Application
from time import sleep

app = Application(backend="uia").start(r"C:\Users\vlab\AppData\Roaming\Zoom\bin\Zoom.exe").connect(title="Zoom",timeout=10)
print(app)
main = app.Zoom
main.print_control_identifiers()

def test_signin():
    signin = main.child_window(title="Sign in", control_type="Button").wrapper_object()
    signin.click()
    sleep(2)
    main.print_control_identifiers()
    edit_mail = main.child_window(title="Enter your email", control_type="Edit").wrapper_object()
    edit_mail.click_input()
    # to cleaar existing stuff
    edit_mail.type_keys("^a{BACKSPACE}")
    sleep(2)
    edit_mail.type_keys("sripilla94@gmail.com")
    edit_passwd = main.child_window(title="Enter your password", control_type="Edit").wrapper_object()
    edit_passwd.click_input()
    edit_passwd.type_keys("^a{BACKSPACE}")
    edit_passwd.type_keys("Ammananna@143")
    sleep(2)
    keep = main.child_window(title="Keep me signed in", control_type="CheckBox").wrapper_object()
    keep.click_input()
    sign_in = main.child_window(title="Sign in", control_type="Button").wrapper_object()
    sign_in.click_input()
    main.print_control_identifiers()