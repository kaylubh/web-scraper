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

def extract_citations_needed_paragraphs(article_document):
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

def get_citations_needed_count(article_url):
    """
    
    """

    raw_article_document = requests.get(article_url)
    parsed_article_document = parse_article_markup(raw_article_document.text)
    paragraphs_citations_needed = extract_citations_needed_paragraphs(parsed_article_document)

    return len(paragraphs_citations_needed)

def get_citations_needed_report(article_url):
    """
    
    """

    raw_article_document = requests.get(article_url)
    parsed_article_document = parse_article_markup(raw_article_document.text)
    paragraphs_citations_needed = extract_citations_needed_paragraphs(parsed_article_document)

    citations_needed_report = []
    for paragraph in paragraphs_citations_needed:
        citations_needed_report.append(f"\n***Citation Needed***\n{paragraph}")

    return citations_needed_report

def citations_needed_app():
    """
    
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

            for citation_needed in citations_needed_report:
                print(citation_needed)

            print("\nExiting...\nRun again to check a new article\n")
        
        else:

            print("\nExiting...\nRun again to check a new article\n")

    else:

        print("\nExiting...\nRun again to check a new article\n")


###############
## Start App ##
###############

citations_needed_app()
