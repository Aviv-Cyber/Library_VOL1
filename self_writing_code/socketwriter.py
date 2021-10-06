from datetime import datetime

class Aviv(object):

    def __init__(self, date):
        self.date = date

    def show(self):
        print(f"the date is {self.date}".replace("23", "00"))

goko = Aviv(datetime.now())

goko.show()