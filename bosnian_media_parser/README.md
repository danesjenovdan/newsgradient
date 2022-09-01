# BOSNIAN PARSER FOR THE MEDIA

## SETUP
```pip install -r requirements.txt```


## RUN SPIDER
crawl to stdout
```bash
scrapy crawl n1info
```

crawl to file
```bash
scrapy crawl n1info -o some.json
```

## CREATING NEW SPIDERS (OR DEBUGGING)
Scrapy provides a useful command to try parsing options in the shell.
```bash
scrapy shell <url>
```
After running this command Scrapy parses the website at given url and returns its contents in the `response` object. You can then run `response.css("...").get()` or whichever commands you need.