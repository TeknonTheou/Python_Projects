
from abc import ABC, abstractmethod

class card(ABC):
    def invoice(self, amount):
        print("Your purchase amount:",amount)
#this function is telling us to pass in an argument, but we don't say how or
#what kind of data it will be
    @abstractmethod
    def payment (Self, amount):
        pass

class CreditCardPayment(card):
#here we've defined how to implement the payment function from the invoice class
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $400 limit.'.format(amount))

obj = CreditCardPayment()
obj.invoice('$500')
obj.payment('$500')
