# Parsing articles from CSVs pipeline


## To sort articles by media outlet
First we need to add missing domains to media objects in the database.

`python manage.py load_media --file media_url_mapping.json`

Then run the command to sort articles.

`python manage.py sort_csv_by_media`

New CSVs will be saved to 'generated_csv' folder.


## Parse urls from CSVs with scrapy
Run

`runner_from_csv.sh`

Successfully parsed articles will be saved to 'exports' folder.

Articles not found will be saved to 'exports-errors' folder.

After that successfully parsed articles will be saved to the database using `python manage.py load_parsed_news` command.
