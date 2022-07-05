#1) create a class SimpleInterest
#   have the attributes called 
#   principle, rate and time
#   compute the SI and amount
#   Given
#   SI = (P x R x T)/100
#   Amount = SI + Principle
   
class SimpleInterest:
    def __init__(self):
        self.principle = 0
        self.rate = 0
        self.time = 0

    def input_principle(self):
        self.principle = int(input('enter the principle amount: \t '))
        
    def input_rate(self):
        self.rate = float(input('enter the rate of interest: \t '))
            
    def input_time(self):
        self.time = float(input('enter the time in years: \t '))        
        
    def calc_SI(self):
        self.SI = (self.principle  * self.rate * self.time)/100
        
    def calc_amount(self):
        self.amount = self.SI + self.principle
        
    def display(self):
        # calling the methods calc of SI and calc of amount
        self.calc_SI()
        self.calc_amount()
        print ('SimpleInterest : \t ',self.SI)
        print ('Amount is : \t',self.amount)
        
print ('----in the main block - START ')
# about to create the Simple Interest
SI1 = SimpleInterest()  # Simple Interest object is created
SI1.input_principle()   # Get principle from user
SI1.input_rate()        # Get rate of interest from user
SI1.input_time()        # Get time in years from user
SI1.display()  # display method prints the output. WATCH from display call the other methods
print ('----- main block ENDS here ----')