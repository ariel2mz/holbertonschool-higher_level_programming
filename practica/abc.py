from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def process_payment():
        pass

class CreditCardPayment(Payment):
    def process_payment():
        print("XD")

class PayPal(Payment):
    def process_payment():
        print("XDDD")
