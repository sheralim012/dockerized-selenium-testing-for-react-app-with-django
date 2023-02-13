from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from users.factories import UserFactory


class LoginTest(LiveServerTestCase):
    host = "0.0.0.0"
    port = 8001

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.FirefoxOptions()
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--window-size=1280,720")
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        cls.driver = webdriver.Remote(
            command_executor="http://selenium-hub:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.FIREFOX,
            options=options,
        )
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        self.user = UserFactory(username='sheralim012', email="sheralim012@gmail.com")

    def test_login(self):
        self.driver.get(f"http://frontend:3000/login")

        username_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        username_input.send_keys("sheralim012")
        password_input.send_keys("password")
        login_button.send_keys(Keys.RETURN)

        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'user-info'), "Email: sheralim012@gmail.com"))
