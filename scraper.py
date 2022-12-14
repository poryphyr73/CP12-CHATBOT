from urllib.request import urlopen

def scrape(url):
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    return html
    
