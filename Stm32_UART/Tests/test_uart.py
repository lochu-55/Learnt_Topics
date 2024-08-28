from Base.uart_stm import uart_py
import logging
import pytest


ut = uart_py()


@pytest.mark.sanity
def test_open_file():
    logging.info("checking the file opened or not...")
    result = ut.file_open()
    assert result == True


@pytest.mark.stm32
def test_debug_mode():
    logging.info("checking the working of debug mode...")
    assert ut.debug_mode() == True


@pytest.mark.stm32
def test_resume():
    logging.info("checking the resume function...")
    assert ut.Resume() == True


@pytest.mark.serial
def test_uart():
    logging.info("printing uart output through com port using pyserial...")
    assert ut.connect_to_port() == "hello"


def test_close_app():
    ut.app.kill()
