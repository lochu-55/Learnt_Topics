from BaseClass.Framework.notepad import Notepad
from Elements.GUI_elements import Elements
ele = Elements()
import logging
import pytest
obj = Notepad()

def test_open_notepad():
    logging.info("checking whether {APP} is opening ")
    result = obj.open_notepad()
    assert result == True

@pytest.mark.pywinauto
def test_edit():
    logging.info("opening notepad")
    obj.open_notepad()
    logging.info("Editing text in notepad")
    result = obj.Edit_text(ele.TEXT)
    logging.info("checking that text edited correctly")
    assert result == ele.TEXT
    logging.info("Closing notepad")
    obj.close_notepad()

@pytest.mark.pywinauto
def test_find():
    logging.info("opening notepad")
    obj.open_notepad()
    logging.info("Editing text in notepad")
    obj.Edit_text(ele.TEXT)
    logging.info("Finding text in notepad")
    result = obj.find(ele.FIND_TEXT)
    assert result == True
    logging.info("Closing notepad")
    obj.close_notepad()

@pytest.mark.pywinauto
def test_replace():
    logging.info("opening notepad")
    obj.open_notepad()
    logging.info("Editing text in notepad")
    obj.Edit_text(ele.TEXT)
    logging.info("Replacing text in notepad")
    result = obj.find_replace()
    assert result == True
    logging.info("Closing notepad")
    obj.close_notepad()

@pytest.mark.pywinauto
def test_change_font():
    logging.info("opening notepad")
    obj.open_notepad()
    logging.info("Editing text in notepad")
    obj.Edit_text(ele.TEXT)
    logging.info("Changing Font,Font Style,Font Size for text")
    obj.change_font()
    logging.info("Closing notepad")
    obj.close_notepad()

@pytest.mark.pywinauto
def test_pagesetup():
    logging.info("opening notepad")
    obj.open_notepad()
    logging.info("Editing text in notepad")
    obj.Edit_text(ele.TEXT)
    logging.info("chaging pagesetup settings")
    obj.pagesetup()
    logging.info("Closing notepad")
    obj.close_notepad()

@pytest.mark.pywinauto
def test_time():
    logging.info("opening notepad")
    obj.open_notepad()
    logging.info("printing date and time in file")
    obj.time()
    logging.info("Closing notepad")
    obj.close_notepad()

@pytest.mark.pywinauto
def test_print():
    logging.info("opening notepad")
    obj.open_notepad()
    logging.info("Editing text in notepad")
    obj.Edit_text(ele.TEXT)
    logging.info("printing file")
    obj.print()
    logging.info("Closing notepad")
    obj.close_notepad()

@pytest.mark.pywinauto
def test_select_all():
    logging.info("opening notepad")
    obj.open_notepad()
    logging.info("Editing text in notepad")
    obj.Edit_text(ele.TEXT)
    logging.info("selecting all the text and deleting and doing undo in notepad")
    obj.select_all()
    logging.info("Closing notepad")
    obj.close_notepad()

@pytest.mark.pywinauto
def test_zoom():
    logging.info("opening notepad")
    obj.open_notepad()
    logging.info("Editing text in notepad")
    obj.Edit_text(ele.TEXT)
    logging.info("zooming the text")
    obj.view()
    logging.info("Closing notepad")
    obj.close_notepad()

@pytest.mark.pywinauto
def test_about():
    logging.info("opening notepad")
    obj.open_notepad()
    logging.info("printing about notepad")
    obj.about()
    logging.info("Closing notepad")
    obj.close_notepad()

@pytest.mark.pywinauto
def test_save():
    logging.info("opening notepad")
    obj.open_notepad()
    logging.info("Editing text in notepad")
    obj.Edit_text(ele.TEXT)
    logging.info("checking that the file saved successfully")
    result = obj.Save_File(ele.FILE_NAME_TO_SAVE)
    assert result == ele.FILE_NAME_TO_SAVE + " - Notepad" ,"FILE NOT SAVED"

@pytest.mark.pywinauto
def test_open():
    logging.info("opening notepad")
    obj.open_notepad()
    logging.info("Opening existing file notepad")
    result = obj.open_file(ele.FILE_NAME_TO_OPEN)
    assert result == True , "FILE NOT FOUND ERROR"
    #assert result == "b1 - Notepad"
    logging.info("Closing notepad")
    obj.close_notepad()
