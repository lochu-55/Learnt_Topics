import pytest
from Framework.Windows import Notepad
from Locators.Win_locators import Note_Paths
from time import sleep

@pytest.fixture(scope='module')
def n():
    obj = Notepad(__name__)
    yield obj

def test_textbox(n):
    n.enter_text("Hello, World!\n")
    n.log_msg("entering text")
    sleep(2)  # Wait for 2 seconds to see the text entered


def test_max(n):
    n.maximize_window()
    n.log_msg("maximizing window")
    sleep(2)  # Wait for 2 seconds to see the window maximized

def test_save(n):
    n.save_file(Note_Paths.PATH1)
    sleep(2)  # Wait for 2 seconds to see the file saved
    n.close_gui()
    n.log_msg("closing window")
