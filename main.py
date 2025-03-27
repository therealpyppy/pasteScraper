import requests_html
session = requests_html.HTMLSession()

run = True

class Paste:
    def __init__(self, id = "GzSLsUsw"):
        self.id = id
        self.url = f"https://pastebin.com/{self.id}"
        self.content = session.get(self.url)
        self.valid = self.content.html.find(".content__title")[0].text != "Not Found (#404)"

    def getTextContent(self):
        return self.content.html.find()

while run:
    paste = Paste(input("What's the id of the paste? "))
    while not paste.valid:
        print("Invalid paste ID.")
        paste = Paste(input("What's the id of the paste? "))
    print(paste.valid)