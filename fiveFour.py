from abc import *

class Printer(ABC):
    @abstractmethod
    def printit(self, text):
        pass
    @abstractmethod
    def disconnect(self):
        pass
class IBM(Printer):
    def printit(self, text):
        print(text)
    def disconnect(self):
        print('Printing completed on IBM Printer')

class HP(Printer):
    def printit(self, text):
        print(text)
    def disconnect(self):
        print('Printing completed on HP printer')

class Myclass:
    str = input("Enter the Printer name: ").upper()
    classname = globals()[str]
    x = classname()
    x.printit('Hello, this is sent to printer')
    x.disconnect()
