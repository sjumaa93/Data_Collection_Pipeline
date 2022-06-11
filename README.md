# Web Scraping Data Collection Pipeline
In this project I have implemented an industry grade data collection pipeline that runs scalably in the cloud.

The webscraper retrieves data from Amazon and uploads it to an RDS database and their associated images to an S3 bucket. This can potentially be used for tracking product price changes for a price comparison website.

# How the system works
![alt text](https://i.ibb.co/ZG0jNVk/Screenshot-2022-05-19-at-8-11-31-pm.png)
- The system relies on selenium to automate web navigation and collecting all the neccasary attributes from Amazon.co.uk
- Each project has a unique ID which will ensure only unique data is scraped
- The data it collects is then saved locally and on an s3 bucket
- Image data is also uploaded to an s3 bucket saved as the product ID and the image name
- The data is then tabularized and stored in an AWS Postgres RDS system
- 

# How the scraper works
- In this part of the project I found a website where I want to scrape information from, and build a scraper around it.
- I created main.py where the scraper would run from.
- I created a scraper class under scraper.py with multiple different functions that would be needed to scrape a site.
- I created methods to accept cookies, search the site, collect titles and collect prices to name a few.
- I created a unique identifier using uuid.
- Once the scraper runs it stores information into a dictionary, which I save as a json file.