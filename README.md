# almanac-app-service
Flask server providing data aggregation, processing, and api endpoints for the web-server

### To run:

If you don't have virtualenv installed, from command line run:

`sudo pip install virtualenv`

Clone the repo and set up a virtual environment inside it:

`virtualenv venv`

Then grab Flask:

`pip install Flask`

To start the server:

`python app.py`

### For Testing:

Inside the project repo, run:

`nosetests -v --with-coverage --cover-inclusive --cover-package=server`

### API Endpoints:

'/news' currently returns the headline, url, abstract, and created_date of the 10 newest articles from NYT newswire in all categories.
It also returns related financial data from the Yahoo finance api i.e. the USD/EUR conversion rate at market close each day from an arbitrary start date
up to the date the article was published

'/top/<category>' does the same with top articles from NYT in a specific category: home, world, national, politics, nyregion, business, opinion,
technology, science, health, sports, arts, fashion, dining, travel, magazine, realestate.

'date/<date>' takes a date and returns the USD/EUR conversion rate each day from an arbitrary start date up to the parameter.
Current arbitrary start date is: 2015-11-23
