Archive of Our Own web scraper for data collection and analysis.

Updating Pipeline to run on Heroku with weekly/monthly scraping to gain information on trends in fanfictions.

Frontend to run on vercel with information stored in SQL and html files stored in AWS S3 before they are deleted (they are only needed for a short time before they are done being processed and their key information saved in SQL.).

- [ ] CSVs seem to rewrite all data when writing to CSV make sure process_artiles and basic_stats are adding rows in csv and not rewriting the entire file
  - [ ] But also transfer to postgresql instead of css anyway
- [ ] Fandoms are separated by |
  - [ ] Not sure if this seperating the same fandom in different languages
  - [ ] Leave for now and see if it causes a problem during processing
- [ ] Include rank???
  - [ ] Currently ranked by hits - hard to find a comprehensive metric other than hits or kudos
- [ ] Don’t need to store html, only need to do html = requests.get(url).text and send to processing
  - [ ] Should store some sort of html before processing to make sure nothing changes bc processing can take awhile
  - [ ] Amazon S3 or firebase
- [ ] Create sql database instead of storing css files
  - [ ] Use postgresql?
- [ ] Move files to be able to be processed in deployed mode
- [ ] Organize processes and how to run each operation bc I am confused looking at the current setup
- [x] Maybe instead of adding current date, pass date down from html header title, so if processing 1000s of pages takes multiple days, we have fewer days
- [ ] Plan where to deploy to set up cron job to complete weekly scrapes of data 1000 pages each time
- [ ] Figure out which ML features to add (TF-IDF, topic labels, sentiment analysis)
  - [ ] Use sci-kit learn to show knowledge
  - [ ] Us streamline by Snowflake for frontend instead of React (at least for now!)
- [ ] Backend should save basic top trends that can update weekly with the scraping but should not need to re ask query each time user accesses the site
- [ ] Run process on ~5000 pages and see if there is a tradeoff in stats found from first 10, 100, 1000, 2000, 3000, 4000, 5000…
  - [ ] 25 pages = 500 articles
    - [ ] 20 articles per page
- [ ] Currently process_articles is taking a long time, maybe get rid of some of the functionality
