import unittest
import scraper
from selenium.webdriver.common.by import By

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.bot = scraper.Scraper()

    def test_accept_cookies(self):
        self.bot.accept_cookies()
    
    def test_search_site(self):
        self.bot.search_site()

    def click_go_button(self):
        self.bot.click_go_button()

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()