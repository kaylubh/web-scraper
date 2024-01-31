import requests
from bs4 import BeautifulSoup

def parse_article_markup(raw_article_document):
    """
    
    """

    # parse the document as html
    soup = BeautifulSoup(raw_article_document, "html.parser")

    # extract the article content from the document
    article_document = soup.select("div.mw-content-ltr")[0]

    return article_document

def extract_citations_needed(article_document):
    """
    
    """

    # extract all paragraphs in the article
    article_paragraphs = article_document.select("p")

    # extract only paragraphs with a citation needed
    paragraphs_citations_needed = []

    for paragraph in article_paragraphs:

        for link in paragraph.select("a"):

            if link.get("href") == "/wiki/Wikipedia:Citation_needed":
                
                paragraphs_citations_needed.append(paragraph.get_text())


    return paragraphs_citations_needed

def get_citations_needed_count(wikipedia_article_url):
    """
    
    """

    raw_article_document = requests.get(wikipedia_article_url)
    parsed_article_document = parse_article_markup(raw_article_document.text)
    test = extract_citations_needed(parsed_article_document)

    return test

def get_citations_needed_report(wikipedia_article_url):
    """
    
    """






###############
## Start App ##
###############
    
article = "https://en.wikipedia.org/wiki/Potato"

print(get_citations_needed_count(article))
