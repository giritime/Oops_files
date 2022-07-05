#1) create a class called Product
#  have the data members as prod id, name, cost price and selling price
#  have methods like input, display and calc selling price
#  keep the profit percentage as 12.5%
#  SP = CP + Profit percentage x CP
class product:
    def __init__(self):
        self.prod_id = 0
        self.prod_name = ''
        self.Prod_cost_price = 0
        self.profit_percentage = 0.125
        self.Prod_selling_price = 0


    def input(self):
        self.prod_id = int(input('Enter the Product id. : \t '))
        self.prod_name = str(input('Enter the Product Name : \t ')) 
        self.prod_cost_price = int(input('Enter the Product Cost : \t '))
    
    def display(self):
        prod.calc_selling_price()        # Calculate profit percentage 
        print ('Selling Price : \t ',self.prod_selling_price )
    
    def calc_selling_price(self):
        self.prod_selling_price = self.prod_cost_price + (self.prod_cost_price * self.profit_percentage)  
        
print ('----in the main block - START ')
# about to create the Selling
prod = product()  # Selling object is created
prod.input()   # Get product id. from user # Get product name from user  # Get cost price from user


prod.display()  # display method prints the output. WATCH from display call the other methods
print ('----- main block ENDS here ----') 