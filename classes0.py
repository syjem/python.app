
class Register:

    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Year: {self.year}")
        print(f"Sport: {self.sport}")

    def add_sport(self, sport):
        self.sport = sport

    
def main():

    full_name = input("Fullname: ")
    age = input("Age: ")
    year = input("Year: ")
    sport = input("Sport: ")


    student = Register(full_name, age, year)
    student.add_sport(sport)
    student.print_info()

if __name__ == ('__main__'):
    main()
