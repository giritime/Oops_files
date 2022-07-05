#4) create a class called Product
#   have the attribute prod id, prod name, rate_actual and selling_price
#   also have the prod_catg which is 'E' or 'T'
#   if the prod_catg is 'E' then
#      rate selling will be 12.5% of rate actual
#     add 1% more if rate selling is less than 1000
#   if the prod catg is 'T' then
#      rate selling will be 14.5% of rate actual
#      add 1.5% more if the rate selling 
#      is in the range of 500 to 2900
class product:
    def __init__(self):
        self.prod_id = 0
        self.prod_name = ''
        self.cost_price = 0
        self.selling_price = 0
        self.category = ''
    
    def input_prod_id(self):
        self.prod_id = int(input('Enter the Product id. : \t '))
        
    def input_prod_name(self):
        self.prod_name = str(input('Enter the Product Name : \t '))  
        
    def input_cost_price(self):
        self.cost_price = int(input('Enter the Product Cost : \t '))
        
    def input_category(self):
        self.category = str(input('Enter the Category: \t '))

    def calc_profit_percentage(self):
        if self.category == 'E' or self.category == 'e':
            self.profit_percentage = 0.125
            self.calc_selling_price() # calling the methods calc of selling price
            if self.selling_price < 1000:
                self.profit_percentage = 0.01
                self.cost_price = self.selling_price
                self.calc_selling_price() # calling the methods calc of selling price
            else:
                self.profit_percentage = 0.125
                self.calc_selling_price() # calling the methods calc of selling price
        elif self.category == 'T' or self.category == 't':
            self.profit_percentage = 0.145
            self.calc_selling_price() # calling the methods calc of selling price
            if self.selling_price > 500 and self.selling_price < 2900:
                self.profit_percentage = 0.015
                self.cost_price = self.selling_price
                self.calc_selling_price() # calling the methods calc of selling price
            else:
                self.profit_percentage = 0.145
                self.calc_selling_price() # calling the methods calc of selling price
        else:
            print ('Invalid Category Entered.')
            self.category = 'Invalid'
   
    def calc_selling_price(self):
        self.selling_price = self.cost_price + (self.cost_price * self.profit_percentage)
        
    def display(self):
        pro.calc_profit_percentage()        # Calculate profit percentage 
        if not self.category == 'Invalid':
            print ('Selling Price : \t ',self.selling_price )
        
print ('----in the main block - START ')
# about to create the Selling
pro = product()  # Selling object is created
pro.input_prod_id()   # Get product id. from user
pro.input_prod_name()   # Get product name from user 
pro.input_cost_price()   # Get cost price from user
pro.input_category()   # Get Category from user

pro.display()  # display method prints the output. WATCH from display call the other methods
print ('----- main block ENDS here ----') 