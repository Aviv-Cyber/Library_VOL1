str = open('WhatsApp Chat with Danielle Penny - Copy.txt', 'r').read()

yoho = (str.replace('1', '0'))


class Student:
    def __init__(self, date=None, name=None, contact=None, hour_range=None, interest=None, free_text=None):
        self.interest = interest
        self.free_text = free_text
        self.hour_range = hour_range
        self.contact = contact
        self.name = name
        self.date = date


id1 = Student("07.20.2021", "נבו שמח", "0546364872", "16:00 - 18:00", "הכנת ממנים, הכנת אופלים בלייב, מרתון למבחן, "
                                                                      "הבנה של החומר בצורה תיאורטית")
id2 = Student("07.20.2021", "אביה בן חיים", "0542595263", "18:00 - 20:00, 20:00 - 22:00", "הכנת ממנים, הכנת אופלים "
                                                                                          "בלייב, מרתון למבחן, "
                                                                                          "הבנה של החומר בצורה "
                                                                                          "תיאורטית")
for i in range(100):
    print("id{} = {}".format(i, id2.name))