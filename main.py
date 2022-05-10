
def main():
    import scraper
    scraper = scraper.Scraper()
    scraper.accept_cookies()
    scraper.search_site()
    scraper.click_go_button()
    scraper.find_links()
    scraper.create_dict()
    scraper.create_json()
    scraper.close_driver()

if __name__ == '__main__':
    main()