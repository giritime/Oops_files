class Circle:
    def __init__(self):
        self.radius = 0
        self.area = 0
        self.perimeter = 0
        
    def input_radius(self):
        self.radius = int(input('enter the radius of the circle '))
        
    def calc_area(self):
        self.area = 3.14 * self.radius * self.radius
        
    def calc_perimeter(self):
        self.perimeter = 2 * 3.14 * self.radius
        
    def display(self):
        # calling the methods calc of area and calc of perimeter
        self.calc_area()
        self.calc_perimeter()
        print ('area of the circle is ',self.area)
        print ('perimeter of the circle is ',self.perimeter)
        
print ('----in the main block - START ')
# about to create the circle object
c1 = Circle()  # one object is created
c1.input_radius()   # using the created object reference - call the inout method
c1.display()  # display method prints the output. WATCH from display call the other methods
print ('----- main block ENDS here ----')

