import pytest


@pytest.fixture()
def login_setup_for_chat(context_1,context_2, browser):
    page1= context_1.new_page()
    page2= context_2.new_page()
    page1.goto("https://www.chat-avenue.com/general/")
    page2.goto("https://www.chat-avenue.com/general/")
    page1.set_default_timeout(5000)
    page2.set_default.timeout(5000)

    yield page1,page2
    page1.close()
    page2.close()
