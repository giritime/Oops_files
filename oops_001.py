class Car:
   def __init__(self):
     self.brand_name = ''
     self.price = 0
     print ('.................................')
     print ('hello I am inside the constructor ')
     print ('NOTE constructor is automaticall called')
     print('WHEN does the constructor get invoked ?')
     print ('when the object is GETTING CREATED/instantiated ')
     print ('.................................')
   def input_car_info(self):
       self.brand_name  = input('enter the car brand name ')
       self.price = int(input('what is the price ? '))
   def display(self):
     print ('Name of the car is ' , self.brand_name)
     print ('Price of the car (in INR) ', self.price)
   def get_details(self):
       res = self.brand_name+ ' ***** in INR ' + str(self.price)
       return res
       # return self.brand_name,self.price
    

c1 = Car()
c1.input_car_info()
c1.display()
print()
c2 = Car()
c2.input_car_info()
temp = c2.get_details()
print (temp)