import requests_html
session = requests_html.HTMLSession()

run = True

class Paste:
    def __init__(self, id = "UqsxYknj", data = None, headers = None):
        if id == None:
            id = "UqsxYknj"
        self.id = id
        self.data = data
        self.headers = headers
        self.url = f"https://pastebin.com/{self.id}"
        self.content = session.get(self.url, headers=self.headers, data=self.data)
        self.valid = self.content.html.find(".content__title")[0].text != "Not Found (#404)"
        self.passwordProtected = self.content.html.find(".content__title")[0].text == "Locked Paste"

    def getTextContent(self):
        return self.content.html.find()

while run:
    id = input("What's the id of the paste? ")
    id = None if id == "" or id == " " else id
    print(id)
    paste = Paste(id)
    try:
        while not paste.valid:
            print("Invalid paste ID.\n")
            id = input("What's the id of the paste? ")
            id = None if id == "" or id == " " else id
            paste = Paste(id)
        
        while paste.passwordProtected:
            password = input("Password: ")
            csrf_token = paste.content.html.find('input[name="_csrf-frontend"]', first=True).attrs['value']
            data = {
                "_csrf-frontend": csrf_token,
                "is_burn": "1",
                "PostPasswordVerificationForm[password]": password
            }
            paste = Paste(id, data=data)
            if paste.passwordProtected:
                print("Incorrect Password!\n")
    except:
        print(paste.content.html.text)