
### This Python script is designed to take command-line input for a search query,
### filter the search results based on a predefined list of valid websites,
### and then open the search results in Google Chrome

import webbrowser
import sys

url = "https://www.google.com/search?q="

valid_websites = [
    'reddit.com',
    'stackoverflow.com',
    'stackexchange.com',
    'medium.com'
]

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

def create_filter():
    filter = '('  # very first character of the filter in open parenthesis
    for index, website in enumerate(valid_websites):  # loop through the entire list, return index as well
        filter += 'site:' + website
        if index == len(valid_websites) - 1:  # checks if we at the very last website, we need to close
            filter += ')'
        else:
            filter += ' OR '  # concatenate all those diff type of site
    return filter

def create_query():
    query = sys.argv[1:]  # create query variable
    return ' '.join(
        query)  # empty func lets you combine all of the element on the query array with the common character of space,
                # concatenate into one gaint string

def create_url():
    if len(sys.argv[1:]) == 0:
        print('Error: Please enter a valid search query')
    else:
        final_url = url + create_query() + create_filter()  # create the file in url
        webbrowser.get(chrome_path).open(final_url)  # open Chrome web browser

create_url()