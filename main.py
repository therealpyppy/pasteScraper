import requests_html
session = requests_html.HTMLSession()

class Paste:
    def __init__(self, id = "GzSLsUsw"):
        self.id = id
        self.url = f"https://pastebin.com/{self.id}"
        self.content = session.get(self.url)

paste = Paste(input("What's the id of the paste? "))
print(paste.content.html.find(".source")[0].text)
