# covid-production-analysis

Assignment work for the Data and Society-HT21, a simple investigation into the effects of Covid-19 on the global production and silicon chip shortage using hypothesis testing.

This is a group with @rafikhaliqi71.

## Running the repo

To install required packages you will first need to install:
- Python 3.8+
- Poetry

Then you can run ``poetry install`` to install the dependencies.

After installing the dependencies to download the data you will need to CD into the scrips dir and run the data collection scrips you can do this by

```
cd scraping_scripts
poetry shell
python automotive_data.py
python covid_data.py
```

This will download the data from OICA for 2018 to 2021 (if available, at time of writing 2021 is not) and the complied daily reports from Johns Hopkins' Covids 19 github repo, note this may take some time.

## Automotive Case

We wish to understand the effect of the global pandemic on production in the automotive industry.
