import unittest
import scraper
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



class TestScraper(unittest.TestCase):
    def setUp(self):
        self.bot = scraper.Scraper()

    def test_accept_cookies(self):
        self.bot.accept_cookies()
        with self.assertRaises(NoSuchElementException):
            self.bot.driver.find_element_by_xpath(
                '//*[@id="sp-cc-accept"]')
        # self.bot.driver.find_element(By.XPATH, '//*[@id="nav-logo-sprites"]')

    def test_search_site(self):
        self.bot.accept_cookies()
        self.bot.search_site()
        self.bot.driver.find_element(By.XPATH,"//span[contains(@class,'a-size-medium')]")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
