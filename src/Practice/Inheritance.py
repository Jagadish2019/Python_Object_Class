#Inheritance example

class Apple:
    manufacturer = "Apple Inc."
    contactWebsite = "www.apple.com/contact"

    def contactDetails(self):
        print("To contact us, log on to ", self.contactWebsite)

class MacBook(Apple):
    def __init__(self):
        self.yearOfmanufacturer=2017

    def manufacturerDetails(self):
        print("This MacBook was manufactured in the year {} by {}. ".format(self.yearOfmanufacturer,self.manufacturer))

macBook = MacBook()
macBook.manufacturerDetails()
macBook.contactDetails()