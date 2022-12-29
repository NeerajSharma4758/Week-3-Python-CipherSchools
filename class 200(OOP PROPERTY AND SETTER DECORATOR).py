class Phone:

    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        self.complete_specification = f"{self.brand} {self.model} and price is {self.price}"
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}...")
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
p1=Phone("Nokia","1100",1000)
print(p1.brand)
print(p1.model)
p1.price= -500 
print(p1.price)
print(p1.complete_specification)
# problem 1 price cannot be negative as it is practically not possible
# problem 2 price is not changing in the complete_sprcifications
Nokia
1100
500
Nokia 1100 and price is 1000
#soltuion 
class Phone:

    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=max(price,0)
        #if price >0:
        #    self.price=price
        #else:
         #   self.price=0
        self.complete_specification = f"{self.brand} {self.model} and price is {self.price}"
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}...")
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
p1=Phone("Nokia","1100",-1000)
print(p1.brand)
print(p1.model)
 
print(p1.price)
print(p1.complete_specification)
Nokia
1100
0
Nokia 1100 and price is 0
 
# problem 2 soln
class Phone:

    def complete_specification(self):
        return f"{self.brand} {self.model} and price is {self.price}"
    
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}...")
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
p1=Phone("Nokia","1100",1000)

p1.price= 500 
print(p1.price)
print(p1.complete_specification())   def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=max(price,0)
        #self.complete_specification = f"{self.brand} {self.model} and price is {self.price}"
    
 
500
Nokia 1100 and price is 500