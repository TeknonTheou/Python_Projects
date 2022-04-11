class User:
    #Define the attributes of the class
    name = "Billy"
    email = "teknontheou@gmail.com"
    password = "abcd1234"

    #Define the methods of the class
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email:  ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password==self.password):
            print("Welcome back, {}.".format(entry_name))
        else:
            print("You are not authorized for this page.")

#add child class Customer
class Customer(User):
    mailing_address = " "
    mailing_list = True
    pin_number = "5678"

    #Define the methods of the child class
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email:  ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin==self.pin_number):
            print("Welcome back, {}.".format(entry_name))
        else:
            print("User email or pin is incorrect.")

#add child class Vendor
class Vendor(User):
    vendor_company = "General"
    vendor_phone = "123-456-7890"
    vendor_id = "TeknonTheou"
    pin_number = "6789"

    #Define the methods of the child class
    def getLoginInfo(self):
        entry_id = input("Enter your vendor id: ")
        entry_pin = input("Enter your pin: ")
        if (entry_id == self.vendor_id and entry_pin==self.pin_number):
            print("Welcome back, {}.".format(self.name))
        else:
            print("User id or pin is incorrect.")


employee = User()
employee.getLoginInfo()

customer = Customer()
customer.getLoginInfo()
    
vendor = Vendor()
vendor.getLoginInfo()
