from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class StudentRegistrationSystemTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome()  # Use your appropriate WebDriver
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_student_registration_and_payment(self):
        self.driver.get(f"{self.live_server_url}/register/")  # Update with your registration URL

        # Fill in the registration form
        name_input = self.driver.find_element(By.NAME, "name")
        email_input = self.driver.find_element(By.NAME, "email")
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        name_input.send_keys("John Doe")
        email_input.send_keys("johndoe@example.com")
        submit_button.click()

        # Redirect to Stripe Checkout
        time.sleep(3)  # Allow redirection
        self.assertIn("checkout.stripe.com", self.driver.current_url)

        # Simulate Stripe test card payment
        card_number = self.driver.find_element(By.NAME, "cardnumber")
        card_number.send_keys("4242424242424242")  # Stripe test card

        expiry_date = self.driver.find_element(By.NAME, "exp-date")
        expiry_date.send_keys("12/34")  # Dummy expiry date

        cvc = self.driver.find_element(By.NAME, "cvc")
        cvc.send_keys("123")  # Dummy CVC

        pay_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        pay_button.click()

        # Confirm registration success
        time.sleep(5)  # Wait for redirection
        self.assertIn("success", self.driver.current_url)  # Update with your success page URL
        self.assertTrue(get_user_model().objects.filter(email="johndoe@example.com").exists())

