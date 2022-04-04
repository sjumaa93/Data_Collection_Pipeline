import scraper

bot = scraper.Scraper

bot = scraper.Scraper('https://www.amazon.com')
bot.accept_cookies("//span[contains(@class,'on-primary')]")