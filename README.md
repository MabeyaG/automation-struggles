# Web Scraping with Python

## The Task
Scrape the title of a webpage using Python.

## The Struggle
- Got a 403 error using `requests`.
- Page returned no content, so BS4 broke silently.

## The Fix
- Used browser headers in `requests`.
- Checked status before parsing.
- # automation-struggles
Real devs. Real problems. One language at a time
