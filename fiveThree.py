class C:
    def _init_(self, power):
        self.power = power
    def _lt_(self, other):
        return self.power< other.power

class Python:
    def _init_(self, power):
        self.power = power

b1 = C(5473)
b2 = Python(7943)
if(b1 < b2):
    print('C has more power')
else:
    print('Python has more power')

