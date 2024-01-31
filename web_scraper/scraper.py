import requests
from bs4 import BeautifulSoup

def parse_article_markup(raw_article_document):
    """
    Using Beautiful Soup, parses an HTML document of a Wikipedia article page and returns the part of the document which contains the main article.
    """

    # parse the document as html
    soup = BeautifulSoup(raw_article_document, "html.parser")

    # extract the article content from the document
    article_document = soup.select("div.mw-content-ltr")[0]

    return article_document

def extract_citations_needed_paragraphs(article_document):
    """
    Given an HTML document of a Wikipedia article parsed with Beautiful Soup, extracts and returns a list of the text content of all paragraphs which have a "[citation needed]" annotation.
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

def get_citations_needed_count(article_url):
    """
    Given a URL to a Wikipedia article, returns the number of times a paragraph has been annotated with "[citation needed]" in the article.
    """

    raw_article_document = requests.get(article_url)
    parsed_article_document = parse_article_markup(raw_article_document.text)
    paragraphs_citations_needed = extract_citations_needed_paragraphs(parsed_article_document)

    return len(paragraphs_citations_needed)

def get_citations_needed_report(article_url):
    """
    Given a URL to a Wikipedia article, returns a string of the paragraphs which have been annotated with "[citation needed]" in the article.   
    """

    raw_article_document = requests.get(article_url)
    parsed_article_document = parse_article_markup(raw_article_document.text)
    paragraphs_citations_needed = extract_citations_needed_paragraphs(parsed_article_document)

    citations_needed_report = ""
    for paragraph in paragraphs_citations_needed:
        citations_needed_report += (f"\n***Citation Needed***\n{paragraph}\n")

    return citations_needed_report

def citations_needed_app():
    """
    Prompts the user for a URL path to a Wikipedia article to check for paragraphs that need citations. Provides the user print statements of the count of citations needed and the content of the paragraphs which need citations.
    """

    print("\nInput the full URL path for a Wikipedia article to be checked for citations needed.\nThe URL MUST be a Wikipedia article and be a valid path.\nExample: https://en.wikipedia.org/wiki/Potaton\n")

    article_url_to_check = input("> ")

    citations_needed_count = get_citations_needed_count(article_url_to_check)
    
    print(f"\nThere are {citations_needed_count} citations needed for this article")

    if citations_needed_count > 0:

        print("Would you like to see the paragraphs which need citations?\n")
        citations_report_response = input("(y)es? ")

        if citations_report_response.lower() == "y":

            citations_needed_report = get_citations_needed_report(article_url_to_check)

            print(citations_needed_report)
            print("\nExiting...\nRun again to check a new article\n")
        
        else:

            print("\nExiting...\nRun again to check a new article\n")

    else:

        print("\nExiting...\nRun again to check a new article\n")


###############
## Start App ##
###############

citations_needed_app()
