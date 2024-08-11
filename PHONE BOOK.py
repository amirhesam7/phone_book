class Human:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def __str__(self):
        return f"\nName:{self.fname} {self.lname}"
h1=Human("Hesam","Kokabi")
h2=Human("Amir","Dehghani")
h3=Human("Ali","Ahmadi")
class Contact:
    def __init__(self,phone_number,email):
        self.phone_number=phone_number
        self.email=email
    def __str__(self):
        return f"\nPhone Number:{self.phone_number}\nEmail:{self.email}"
c1=Contact(912,"venom@gmail.com")
c2=Contact(936,"batman@yahoo.com")
c3=Contact(919,"spiderman@gmail.com")
class Address:
    def __init__(self,city,street,alley,zipcode):
        self.city=city
        self.street=street
        self.alley=alley
        self.zipcode=zipcode
    def __str__(self):
        return f"\nAddress:{self.city},{self.street},{self.alley},{self.zipcode}"
a1=Address("Tehran","aval","dovom",23)
a2=Address("Karaj","aval","dovom",44)
a3=Address("Esfahan","aval","dovom",56)
class Phone_book:
    def __init__(self):
        self.db=[]
    def create(self,name):
        self.db.append(name)
    def read(self):
        return self.db
    def delete(self,index):
        del self.db[index]
    def update(self,index,value):
        self.db[index]=value
def main_menu():
    print("-"*50)
    print("1 ) add a new contact")
    print("2 ) show all contacts")
    print("3 ) edit contact")
    print("4 ) delete contact")
    print("5 ) exit")
    print("-"*50)
main_menu()
current=input()
while current !="5":
    p1=Phone_book()
    if current=="1":
        print("add contact menu")
        p1.create(input("Please enter your first contact:"))
        p1.create(input("Please enter your second contact:"))
        p1.create(input("Please enter your third contact:"))
        print(p1.read())
        main_menu()
        current=input()
    elif current=="2":
        print("show all contact menu")
        print(h1,h2,h3)
        print(c1,c2,c3)
        print(a1,a2,a3)
        main_menu()
        current=input()
    elif current=="3":
        print("edit contact menu")
        p1.update(0,"Benyamin")
        print(p1.read())
        main_menu()
        current=input()
    if current=="4":
        print("delete contact menu")
        p1.delete(2)
        print(p1.read())
        main_menu()
        current=input()








        


    
