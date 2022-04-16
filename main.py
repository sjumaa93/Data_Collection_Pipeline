
def main():
    import scraper
    bot = scraper.Web_Scraper('https://www.amazon.co.uk')
    bot.accept_cookies("//span[contains(@class,'on-primary')]")
    bot.search_site("//input[contains(@id, 'search')]",'Mobile Phones')
    bot.click_go_button("//input[@value='Go']")
    bot.find_data(
        "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']",
        "//span[contains(@class, 'a-size-large product-title-word-break')]",
        "//span[contains(@class, 'a-price-whole')]",
        #"//span[contains(@class, 'imgTagWrapper')]",
        )

    bot.create_json
    bot.close_driver()

if __name__ == '__main__':
    main()