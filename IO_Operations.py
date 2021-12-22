from Lab7.User_Class import User
import datetime, random
from Exceptions import *

class TaskController:
    def __init__(self):
        self.tasks = []
    def create_user(self, name, last_name, address,gender,birth_date):
        usr = User(name, last_name, address, gender, birth_date)
        self.tasks.append(usr)
        self.add_to_the_file(usr,"users.txt")
    def print_tasks(self):
        for task in self.tasks:
            print(task)
    def find_task_by_index(self, index):
        return self.tasks[index]

    def create_n_users(self,n):
        for i in range(int(n)):
            address=("PostalCode"+str(i),"Street"+str(i),"NO:"+str(i))
            self.create_user("Name"+str(i), "LastName"+str(i), address, bool(random.getrandbits(1)), self.get_Random_BirthDate())

    def get_Random_BirthDate(self):
        start_date = datetime.date(1990, 1, 1)
        end_date = datetime.date(2015, 2, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return random_date

    def save_task_to_file(self, path):
        with open(path, "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(str(task))
            print(f"Data saved to file: {path}")

    def save_task_to_CSV(self, path):
        with open(path, "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(task.to_csf_File())
            print(f"Data saved to file: {path}")

    def read_task_to_file(self, path):
        try:
            with open(path, "r", encoding="utf-8") as file:
                tmp=file.readlines()
                #print(tmp)
                if(len(tmp)>=100):
                    raise FileToLong()
                for line in tmp:
                    print(str(line))
        except FileNotFoundError:
            MyFileNotFoundError()
        except FileToLong:
            print("The file is too long")
        except Exception:
            MyException()

    def add_to_the_file(self, usr, path):
        try:
            with open(path, "a", encoding="utf-8") as file:
                if(str(usr).__eq__("")):
                    raise NoTextError
                file.write(str(usr))

            print(f"Data saved to file: {path}")
        except FileNotFoundError:
            MyFileNotFoundError()

    def txt_to_csv_converter(self, pathTXT, pathCSV):
        try:    #por si aparece algún error
            with open(pathTXT, "r", encoding="utf-8") as file:  # w:escribir
                tmp=file.readlines()
                for line in tmp:
                    line=line.replace(" ",";")
                    if (str(line).__eq__("")):
                        raise NoTextError
                    try:
                        with open(pathCSV, "a", encoding="utf-8") as file:  # w:escribir
                            if (str(line).__eq__("")):
                                raise NoTextError
                            file.write(str(line)+";")
                    except FileNotFoundError:
                        MyFileNotFoundError()
        except FileNotFoundError:
            MyFileNotFoundError()

if __name__ == '__main__':
    uc = TaskController()
    uc.create_n_users(10)
    uc.read_task_to_file("user.txt")
    uc.read_task_to_file("Error.txt")
    uc.save_task_to_CSV("Converted.csv")

