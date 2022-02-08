#import necessary modules
from flask import Flask, render_template
import json
from bs4 import BeautifulSoup
import requests

# set up flask webserver
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def load_selectors():
    with open("selectors.json", 'r') as f:
        return json.load(f)


# webscraping function
def my_scraper():
# get the URL in a useable form 
    url = "https://www.w3schools.com/cssref/css_selectors.asp"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

# select your objects
    table_rows = [elem for elem in soup.select('.ws-table-all tr')]
    return table_rows
    # YOUR CODE GOES HERE


# filter function
def my_filter():
    return true
    # YOUR CODE GOES HERE

# output to json
def write_json():
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
    # YOUR CODE GOES HERE

table_rows = my_scraper()
write_json()

# define route(s)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/css")
def scrapings():
    return render_template("scraping.html")

@app.route("/css-selectors")
def css_selectors():
    return render_template("css-selectors.html", selectors=load_selectors())


# starts the webserver
if __name__ == "__main__":
    app.run()
