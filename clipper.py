from scraper import scrape

current_body = ""
current_html = ""

def get_raw_body():
    body_index = current_html.find("<body")
    start_index = body_index + len("<body>")
    end_index = current_html.find("</body>")
    return current_html[start_index:end_index]

def get_text_body(index):
    i = 0
    temp_start = 0
    temp_end = 0
    body = current_body
    while(1):
        body = current_html[temp_start:]
        temp_start = body.index("<tbody")
        print(temp_start)
        temp_end = body.index("</tbody")
        print(temp_end)
        if(i == index): break
        i+=1
    return body[temp_start:temp_end]

current_html = scrape("https://en.wikipedia.org/wiki/Otto_IV,_Holy_Roman_Emperor")
current_body = get_raw_body()
print(get_text_body(2))