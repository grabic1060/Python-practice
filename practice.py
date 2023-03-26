class calculator():
    def __init__(self,A,B):
        self.A=A
        self.B=B

    def plus(self):
        sum=self.A+self.B
        return sum

    def minus(self):
        sum = self.A-self.B
        return sum

    def multiple(self):
        sum = self.A*self.B
        return sum

    def divide(self):
        sum = self.A/self.B
        return sum

a=float(input())
symbol=input()
b=float(input())

result=calculator(a,b)
if (symbol == '+'):
    print(result.plus())
if (symbol == '-'):
    print(result.minus())
if (symbol == '*'):
    print(result.multiple())
if (symbol == '/'):
    print(result.divide())
