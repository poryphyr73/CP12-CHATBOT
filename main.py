from urllib.request import urlopen

url = "https://en.wikipedia.org/wiki/John_Foster_(printer)"

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

body_index = html.find("<body")
start_index = body_index + len("<body>")
end_index = html.find("</body>")

body = html[start_index:end_index]

print(body)