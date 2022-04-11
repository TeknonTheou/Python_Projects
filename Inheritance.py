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
    
#add child classes (customer and vendor)
class Customer(User):
    mailing_address = " "
    mailing_list = True

class Vendor(User):
    vendor_company = "General"
    vendor_phone = "123-456-7890"

    #Define the methods of the class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password==self.password):
            print("Welcome back, {}.".format(self.name))
        else:
            print("You are not authorized for this page.")

new_customer = Customer("John Doe", "JDoe@gmail.com", "abcd1234", 123)
new_customer.mailing_adress = "123 Anywhere"
new_customer.mailing_list = False

print(new_customer.name)
print(new_customer.account)
print(new_customer.mailing_address)
