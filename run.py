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


    # define filter function
    def filter_func(elem):
        return True

    # apply filter function
    table_rows = list(filter(filter_func, table_rows))


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
    pass


# define route(s)
@app.route("/")
def home():
    return render_template("index.html")

# define route(s)
@app.route("/webscraping")
def webscraping():
    return render_template("webscraping.html")

# define route(s)
@app.route("/shivam")
def shivam():
    return render_template("shivam.html")



@app.route("/success")
def success():
    my_scraper()
    return render_template("success.html")



@app.route("/css-selectors")
def css_selectors():
    return render_template("css-selectors.html", selectors=load_selectors())


# starts the webserver
if __name__ == "__main__":
    app.run()
