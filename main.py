
if __name__ == '__main__':
    import scraper
    bot = scraper.Scraper('https://www.amazon.co.uk')
    bot.accept_cookies("//span[contains(@class,'on-primary')]")
    bot.search_site("//input[contains(@id, 'search')]",'Mobile Phones')
    bot.go_button("//input[@value='Go']")
    bot.findproducts("//span[contains(@class, 'a-size-medium a-color-base a-text-normal')]")

