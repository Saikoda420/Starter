class Student:
    def __init__(self,name,house,listo):
        self.name = name
        self.house = house
        self.listo = listo

def main():
    namaye=[]
    housee=[]
    for _ in range(1):
        alu = get_student()
        namaye.append(alu.name)
        housee.append(alu.house)
        
    for i in range(1):
         print(f"{namaye[i]} is in {housee[i]}")
         print(alu.listo)

def get_student():
        name = input("Enter name: ")
        house = input("House: ")
        listo = [9,9,8,0]
        student = Student(name, house,listo)
        return student
main()