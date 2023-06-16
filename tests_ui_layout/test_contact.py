import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.mark.integration
def test_contact(playwright: Playwright) -> None:
    # Access
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # Act what to do
    page.get_by_role("link", name="Contact Us").click()
    page.get_by_placeholder("Enter your name").click()
    page.get_by_placeholder("Enter your name").fill("Ahad")
    page.get_by_placeholder("Enter your name").press("Tab")
    page.get_by_placeholder("Enter your address").fill("ahada123@gmail.com")
    page.get_by_placeholder("Enter your address").press("Tab")
    page.get_by_placeholder("Enter your email").fill("ahada123@gmail.com")
    page.get_by_placeholder("Enter your address").click()
    page.get_by_placeholder("Enter your address").fill("12str 77 address")
    page.get_by_placeholder("Enter your phone number").click()
    page.get_by_placeholder("Enter your phone number").fill("12345887654")
    page.get_by_placeholder("Type the subject").click()
    page.get_by_placeholder("Type the subject").fill("dummy subject")
    page.get_by_placeholder("Type your message here...").click()
    page.get_by_placeholder("Type your message here...").fill("here is a message")
    page.get_by_test_id("buttonElement").click()

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
