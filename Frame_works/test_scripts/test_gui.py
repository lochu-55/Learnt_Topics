# import pytest
# from time import sleep
# from Base.GUIWEB import automate_gui

# @pytest.fixture(scope="module")
# def obj():
#     # Initialize the GUI object
#     obj = automate_gui()
#     obj.logger.info("opening gui application")
#     # Yield the GUI object to the test functions
#     yield obj

# @pytest.mark.pywinauto
# def test_edit(obj):
#     sleep(2)
#     obj.edit("welcome sri jyothsna")
#     obj.logger.info("editing text in notepad")
#     sleep(2)

# @pytest.mark.pywinauto
# def test_save(obj):
#     obj.logger.info("saving file in notepad")
#     obj.Save_as("sri")
#     sleep(2)

# @pytest.mark.pywinauto
# def test_close(obj):
#     obj.logger.info("closing notepad")
#     obj.close_gui()


