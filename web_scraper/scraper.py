import requests

def get_citations_needed_count(wikipedia_article_url):
    """
    
    """

    raw_article_page = requests.get(wikipedia_article_url)



    return raw_article_page

def get_citations_needed_report(wikipedia_article_url):
    """
    
    """

def extract_citations_needed(raw_article_page):
    """
    
    """



###############
## Start App ##
###############
    
article = "https://en.wikipedia.org/wiki/Potato"

print(get_citations_needed_count(article))
