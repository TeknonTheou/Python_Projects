class User:
    #Define the attributes of the class
    name = "No Name Provided"
    email = " "
    password = "1234abcd"
    account = 0
    #initialize class
    def __init__ (self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account

 #Define the methods of the class
    def login(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password==self.password):
            print("Welcome back, {}.".format(entry_name))
        else:
            print("You are not authorized for this page.")

    
#add child classes (customer and vendor)
class Customer(User):
    mailing_address = " "
    mailing_list = True
    pin_number = "5678"

    #Define the methods of the child class
    def login(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your password: ")
        if (entry_email == self.email and entry_pin==self.pin_number):
            print("Welcome back, {}.".format(entry_name))
        else:
            print("Invalid email or pin.")

class Vendor(User):
    vendor_company = "General"
    vendor_phone = "123-456-7890"
    pin_number = "6789"

    #Define the methods of the child class
    def login(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your password: ")
        if (entry_email == self.email and entry_pin==self.pin_number):
            print("Welcome back, {}.".format(entry_name))
        else:
            print("Invalid email or pin.")

# Unvoke method inside each class.
manager = User()
magager.login

customer = Customer()
customer.login

vendor = Vendor()
vendor.login
