# import necessary modules
from bs4 import BeautifulSoup
import requests
import json

def scraper():
# get the URL in a useable form 
    url = "https://www.w3schools.com/cssref/css_selectors.asp"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

# select your objects
    table_rows = [elem for elem in soup.select('.ws-table-all tr')]
    return table_rows


# define filter function
def filter_func(elem):
    return True

# apply filter function
# table_rows = list(filter(filter_func, table_rows))

def jsonson():
# create the structure for the json file
    selectors = []

    for row in table_rows:
        cells = list(row.select('td'))
        if cells:
            entry = {
                'selector': "placeholder text, which will be overwritten below",
                'example': cells[1].text,
                'description': cells[2].text,
            
         }
         # we need the following code beacause not all entries in the first column are text - some are links (a-tag)
            if cells[0].a:
                entry['selector'] = cells[0].a.text
            else:
                entry['selector'] = cells[0].text

            selectors.append(entry)
        

    with open("selectors.json", 'w') as f:
        json.dump(selectors, f)

table_rows = scraper()
jsonson()
