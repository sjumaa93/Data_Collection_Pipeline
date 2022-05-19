# Data_Collection_Pipeline

![alt text](https://i.ibb.co/ZG0jNVk/Screenshot-2022-05-19-at-8-11-31-pm.png)
# Creating a scraper
- In this part of the project I found a website where I want to scrape information from, and build a scraper around it.
- I created main.py where the scraper would run from.
- I created a scraper class under scraper.py with multiple different functions that would be needed to scrape a site.
- I created methods to accept cookies, search the site, collect titles and collect prices to name a few.
- I created a unique identifier using uuid.
- Once the scraper runs it stores information into a dictionary, which I save as a json file.