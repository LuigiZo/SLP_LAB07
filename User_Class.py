from datetime import date
class User:
    def __init__(self, name, last_name, address, gender, birth_date):  # constructor / initializer
        self.name = name
        self.last_name = last_name
        self.address = address
        self.gender = gender
        self.birth_date = birth_date

    def __str__(self):  # str representation of the object
        return self.name +" "+ self.last_name +" "+ self.address[0]+" "+self.address[1]+" "+self.address[2] +" "+ str(self.gender) +" "+ str(self.birth_date) + " (" + str(self.get_current_age())+" y.o.)\n"

    def to_csf_File(self):
        return self.name +";"+ self.last_name +";"+ self.address[0]+";"+self.address[1]+";"+self.address[2] +";"+ str(self.gender) +";"+ str(self.birth_date) + " (" + str(self.get_current_age())+" y.o.)\n"

    def get_current_age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
