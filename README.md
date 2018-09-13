# tourparser

As of July 29th 2018, this code is no longer being maintained. This repo is kept up in case anyone would want to look at a practical example of webscraping and data organisation. When the Tour de France 2019 begins, I might update this code for the 2019 edition of the Tour de France website.

## What is in this repo?
`collect.py` is the first part of the project. It gathers all the data needed from the [Tour de France website](letour.fr). It organizes the data in the subfolder `./data/html/` with a folder for each team.

`parse.py` is the second part of the project. It takes all .html files from data/html/, converts the data to csv-format and writes them into .csv files in `./data/csv/`

(I used to have `parse.py` write one big data.csv file too but I forgot where I wrote the code. This part may be added later)
