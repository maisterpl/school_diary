class TestClass():
    def __str__(self) -> str:
        return "Test class."


class Test():
    
    def __init__(self, number1, numner2, LIST1 = [], LIST2 = []) -> None:
        self.number1 = number1
        self.numner2 = numner2
        self.LIST1 = []
        self.LIST2 = {}
        
    def __str__(self) -> str:
        print(self.number1)
        print(self.numner2)
        print(self.LIST1)
        print(self.LIST2)
        return ""
    
    def add1(self, number):
        self.LIST1.append(number)
        
    def add2(self, key, value):
        self.LIST2[key] = value
    
print("TEST1")  
test1 = Test(1, 2)
test1.add1(1)
test1.add2()
print(test1.LIST1)
print(test1.LIST2)

print("TEST2")
test2 = Test(3, 4)
test2.add1(3)
test2.add2(4)
print(test2.LIST1)
print(test2.LIST2)

