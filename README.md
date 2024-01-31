# LAB - Class 17

## Project: Wikipedia Citation Needed Web Scraper

### Author: [Caleb Hemphill](https://github.com/kaylubh)

Simple web scraper which parses a Wikipedia article page to find all instances of paragraphs with a "citation needed" annotation.

### Setup

#### Requirements

1. Install [Python](https://www.python.org/) if not already

1. Create and activate a virtual environment

    `python3 -m venv .venv`

    `source .venv/bin/activate` (Linux/Mac)

    `source .venv/Scripts/activate` (Windows)

1. Install packages

    `pip install -r requirements.txt`

#### Run

From root of project directory run `python -m web_scraper.scraper`.

#### Tests

No test modules to run for this project. The best way to test functionality and accuracy is to view the same article in a browser and use the browsers built-in find in page feature (ctrl/cmd + f) to find all instances of "citation needed" and verify if the count and/or paragraphs match.

Known Issues

- Does not recognize "citation needed" on non-paragraph elements
- Does not recognize similar "citation needed" annotations with different formatting or use cases
