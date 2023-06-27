import httpx
from selectolax.parser import HTMLParser

def scrape_website_content(website_url):
    resp = httpx.get(website_url)
    html = HTMLParser(resp.text)

    return html

def clean_website_content(website_html):
    tags = ['head', 'style','noscript' 'script','path', 'xmp', 'iframe', 'noembed', 'noframes','svg']
    website_html.strip_tags(tags)
    website_document = website_html.body.text()

    return website_document

