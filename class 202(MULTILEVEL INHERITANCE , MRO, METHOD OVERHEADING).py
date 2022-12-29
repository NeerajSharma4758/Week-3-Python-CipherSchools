class Phone: #base/parent class

    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=max(price,0)
    
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}...")
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class Smartphone(Phone): #child/derived class
    
    def __init__(self,brand,model,price,ram,memory,rear_camera):
        #Phone.__init__(self,brand,model,price) #uncommon way
        super().__init__ (brand,model,price) #common way       
        self.ram=ram
        self.memory=memory
        self.rear_camera=rear_camera
        
class Flagshipphone(Smartphone):
       def __init__(self,brand,model,price,ram,memory,rear_camera,front_camera):
            super().__init__(brand,model,price,ram,memory,rear_camera)
            self.front_camera= front_camera
    

    
 
p=Phone('Nokia','1100',1000)
s=Smartphone("OnePlus",'5',30000,'6 GB','64 GB', '20 MP')
f=Flagshipphone("OnePlus",'5',30000,'6 GB','64 GB', '20 MP','16 MP')

print(p.full_name())
print(s.full_name())
print(f.full_name())
print(help(Smartphone))
Nokia 1100
OnePlus 5
OnePlus 5
Help on class Smartphone in module __main__:

class Smartphone(Phone)
 |  Smartphone(brand, model, price, ram, memory, rear_camera)
 |  
 |  Method resolution order:
 |      Smartphone
 |      Phone
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, brand, model, price, ram, memory, rear_camera)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Phone:
 |  
 |  full_name(self)
 |  
 |  make_a_call(self, phone_number)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Phone:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

None
# can we derive more than one class from base class?

# multilevel inheritance

# method resolution order ---> help.(class name )

# method overriding

#isinstance(), issubclass()
 
# method overriding
class Phone: #base/parent class

    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=max(price,0)
    
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}...")
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class Smartphone(Phone): #child/derived class
    
    def __init__(self,brand,model,price,ram,memory,rear_camera):
        #Phone.__init__(self,brand,model,price) #uncommon way
        super().__init__ (brand,model,price) #common way       
        self.ram=ram
        self.memory=memory
        self.rear_camera=rear_camera
       
    def full_name(self):
        return f"{self.brand} {self.model} and price is {self.price}"
        
class Flagshipphone(Smartphone):
       def __init__(self,brand,model,price,ram,memory,rear_camera,front_camera):
            super().__init__(brand,model,price,ram,memory,rear_camera)
            self.front_camera= front_camera
    

    
 
p=Phone('Nokia','1100',1000)
s=Smartphone("OnePlus",'5',30000,'6 GB','64 GB', '20 MP')
f=Flagshipphone('realme','5',30000,'6 GB','64 GB', '20 MP','16 MP')

print(p.full_name())
print(s.full_name())
print(f.full_name())
print(isinstance(s,Smartphone)) # s is the obejct of smartphone
print(issubclass(Smartphone,Phone))
Nokia 1100
OnePlus 5 and price is 30000
realme 5 and price is 30000
True
True