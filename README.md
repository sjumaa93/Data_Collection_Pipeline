# Web Scraping Data Collection Pipeline
In this project I have implemented an industry grade data collection pipeline that runs scalably in the cloud.

The webscraper retrieves data from Amazon and uploads it to an RDS database and their associated images to an S3 bucket. This can potentially be used for tracking product price changes for a price comparison website.

# How the system works
- The system relies on selenium to automate web navigation and collecting all the neccasary attributes from Amazon.co.uk
- Each project has a unique ID which will ensure only unique data is scraped
- The data it collects is then saved locally and on an s3 bucket
- Image data is also uploaded to an s3 bucket saved as the product ID and the image name
- The data is then tabularized and stored in an AWS Postgres RDS system

# How the scraper works
- In this part of the project I found a website where I want to scrape information from, and build a scraper around it.
- I created main.py where the scraper would run from.
- I created a scraper class under scraper.py with multiple different functions that would be needed to scrape a site.
- I created methods to accept cookies, search the site, collect titles and collect prices to name a few.
- I created a unique identifier using uuid.
- Once the scraper runs it stores information into a dictionary, which I save as a json file.

# Documenting and Testing
- I created tests on my scraper to make sure the scraper runs as it should
- One of the tests looks at whether we continue past the cookie page
- Another test looks for an attribute only found on the search results page to determine we on the correct page

# Preventing Rescraping
- To prevent rescraping the user ID from the product is compared with the user IDs in the AWS database
- These product IDs will always be unique and that is why I have used them as a point of reference to check if a product has already been scraper
- If a product has been scraper the scraper will simply move onto the next product and continue scraping.

# Containerising the scraper & Monitoring
- The application is containerized using docker and runs on an AWS EC2 instance on the cloud. 
- A prometheus monitoring system is also deployed to monitor the health of the EC2 host the docker and the containerized application.
- The monitored metrics are tracked by a Grafana dashboard.

# CI/CD Pipeline for Docker Image
- The system also implements CI/CD with the help of Github actions.
- A push to the main branch of the repository will trigger a build of the docker image of the application.
- The image is then expected to be pulled at regular intervals during the scraping process.



