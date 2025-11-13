from base_classes import *

class SecureAccount(Account): 
    def __init__(self, password):
        super().__init__()
        self.password = password
        
    
    def get_balance(self, password):
        if password == self.password:
            return super().get_balance()
        else:
            print("Incorrect password")
    
    def deposit(self, amount, password):
        if password == self.password:
            return super().deposit(amount)
        else:
            print("Incorrect password")
    
    def withdraw(self, amount, password):
        if password == self.password:
            return super().withdraw(amount)
        else:
            print("Incorrect password")



class MemoryCalculator(Calculator):
    def __init__(self):
        self.result = 0
        super().__init__()
        
    
    def add(self, x, y):
        if x == "RESULT":
            x = self.result
        if y == "RESULT":
            y = self.result
        self.result = x + y
        return super().add(x, y)
    
    def sub(self, x, y):
        if x == "RESULT":
            x = self.result
        if y == "RESULT":
            y = self.result
        self.result = x - y
        return super().sub(x, y)

class ImprovedFraction(Fraction):
    def __init__(self, numerator, denominator):
        super().__init__( numerator, denominator)
    
    def add(self, other):
        if isinstance(other, int):
            other = ImprovedFraction(other, 1)
        return super().add(other)
    
    def multiply(self, other):
        if isinstance(other, int):
            other = ImprovedFraction(other, 1)
        return super().multiply(other)
  

    def __add__(self,other):
        return self.add(other)
    
    def __mul__(self, other):
        return self.multiply(other)
    
    def __str__(self):
        if self.get_denominator() == 1:
            return str(self.get_numerator())
        else:
            return f"{self.get_numerator()}/{self.get_denominator()}"





    
