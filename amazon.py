
def main():
    import scraper
    bot = scraper.Scraper
    bot = scraper.Scraper('https://www.amazon.co.uk')
    bot.accept_cookies("//span[contains(@class,'on-primary')]")
    bot.search_site("//input[contains(@id, 'search')]",'Mobile Phones')
    bot.clickgo("//input[@value='Go']")

if __name__ == '__main__':
    main()