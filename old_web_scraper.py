"""Web scraper used to pull the versions of Selenium per language."""
from BeautifulSoup import BeautifulSoup

import requests

# empty list to list all rows from the table
list_of_languages = []
# empty list of cells or columns per row
list_of_versions = []
# empty dictionary to hold key:value pairs of Language:Client Version
selenium_dict = {}
# snapshot taken as of 2-4-2016 of the current client version for comparison
client_version_baseline = {
    'C#': '2.50.1',
    'Ruby': '2.50.0',
    'Python': '2.50.0',
    'Java': '2.50.1',
    'Javascript (Node)': '2.48.2'
}


def scrape_table():
    """Grab specific table from specified URL and strip out data needed."""
    # define the url we wish to scrape data from
    url = requests.get('http://www.seleniumhq.org/download/')
    # set a variable that holds all HTML contents of the page
    html = url.content
    # new BeautifulSoup instance and we feed it the html
    soup = BeautifulSoup(html)
    # next, we do some detective work to find out unique information
    # to pass to BeautifulSoup so it knows what table we are targeting
    # find all elements in div with id mainContent, then drill down to
    # the table tag
    table = soup.find("div", attrs={"id": "mainContent"}).table

    # find all <tr> elements in the table
    # for each table row in the table starting after the table header...
    for tr in table.findAll('tr')[1:]:
        # for each cell in the table row for the first cell
        for td in tr.findAll('td')[0:1]:
            # replace html tag and deposit raw text into the languages list
            language = td.text.replace('<td>', '')
            list_of_languages.append(language)
        # for each cell in the table row for the second cell
        for td in tr.findAll('td')[1:2]:
            # replace html tag and deposit raw text into client versions list
            version = td.text.replace('<td>', '')
            list_of_versions.append(version)


def populate_dict():
    """Take the values of each list and build a dict."""
    # time to add the keys and values to the dictionary;
    # there is a 1 to 1 relationship for the languages and client versions;
    # list_of_languages[0] is directly related to list_of_versions[0]
    for x in range(0, len(list_of_languages), 1):
        selenium_dict[list_of_languages[x]] = list_of_versions[x]


def print_dict():
    """Print out the dictionary."""
    # some simple formatting
    print "\nLanguage --> Client Version"
    # print each key in the dict, print each key and each value
    for key in selenium_dict:
        print key + " --> " + selenium_dict[key]


def check_python_version():
    """Check to see if a new version for Python is available."""
    current_version = selenium_dict['Python']
    if current_version != client_version_baseline['Python']:
        print '\nNewer version available! Your version: {0}; '\
              'Current Version: {1}. You should think about upgrading!'\
              .format(client_version_baseline['Python'], current_version)
    else:
        print "\nYou have the latest Python version!"

scrape_table()
populate_dict()
print_dict()
check_python_version()