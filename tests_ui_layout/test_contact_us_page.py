# import time
# from playwright.sync_api import Playwright, sync_playwright
# import pytest
# from pom.contact_us_page import ContactUs
#
# # @pytest.mark.skip(reason='Duplicated test')
# def test_submit_form(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False , slow_mo=500)
#     page = browser.new_page()
#     contact_page = ContactUs(page)
#     contact_page.navigate()
#     contact_page.submit_form("Ahad", "st7 block F", "testmail@gmail.com", "1233222", "test subj", "test messageasdasdasdasdasdasasdasdasdasdasdasasdasdasd" )
#     print("Success")
#
# with sync_playwright() as playwright:
#     test_submit_form(playwright)
#     # time.sleep(5)
