import unittest
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from random import choice
from string import ascii_letters, digits

class SignInTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a new Firefox session
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        cls.driver.get("https://slack.com/signin")

    def test_signin_with_valid_credentials(self):
        # Explicit wait = 10 seconds
        wait = ui.WebDriverWait(self, 10)

        # Get the domain textbox
        domain_field = self.driver.find_element_by_id("domain")
        domain_field.clear()

        # Submit button
        submit_domain_button = self.driver.find_element_by_id("submit_team_domain")

        # Enter valid domain and click Submit button
        domain_field.send_keys("slackchallenge")
        submit_domain_button.click()

        # Title assertion
        title = self.driver.title
        self.assertEqual(title, "Sign In | Slack")

        # Email and password textfields
        email_field = self.driver.find_element_by_id("email")
        email_field.clear()
        password_field = self.driver.find_element_by_id("password")
        password_field.clear()

        # Sign In button
        signin_button = self.driver.find_element_by_id("signin_btn")

        # Enter valid email and password, click Sign In button
        email_field.send_keys("****@gmail.com")
        password_field.send_keys("****")
        signin_button.click()

        # Wait for a message textfield
        message_input = self.driver.find_element_by_id("message-input")
        wait.until(lambda driver: message_input.is_displayed())

    @classmethod
    def tearDownClass(cls):
        # Close the browser window
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main(verbosity=2)
