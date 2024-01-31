import requests
from bs4 import BeautifulSoup

def parse_article_markup(raw_article_document):
    """
    
    """

    # parse the document as html
    soup = BeautifulSoup(raw_article_document, "html.parser")

    # extract the article content from the document
    article_document = soup.select("div.mw-content-ltr")

    return article_document

def extract_citations_needed():
    """
    
    """

    # extract all paragraphs in the article
    article_para

def get_citations_needed_count(wikipedia_article_url):
    """
    
    """

    raw_article_document = requests.get(wikipedia_article_url)
    parsed_article_document = parse_article_markup(raw_article_document.text)


    return parsed_article_document

def get_citations_needed_report(wikipedia_article_url):
    """
    
    """






###############
## Start App ##
###############
    
article = "https://en.wikipedia.org/wiki/Potato"

print(get_citations_needed_count(article))
