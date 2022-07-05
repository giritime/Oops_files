class Student:
    def __init__(self):
        self.roll = 0
        self.name = ''
        self.phy = 0
        self.chem = 0
        self.maths = 0
        self.total = 0
        self.avg = 0
        self.result = ''
    def input_stud_details(self):
        self.roll =int(input('enter the roll number '))
        self.name = input('enter the name ')
    def input_marks_details(self):
        self.phy = float(input('enter Physics marks '))
        self.chem = float(input('enter Chemistry marks '))
        self.maths = float(input('enter Maths marks '))
    # business methods (which do computations )  
    def calc_total(self):
        self.total = self.phy + self.chem + self.maths
    def calc_avg(self):
        self.avg = self.total / 3
    def calc_result(self):
        if self.avg >=50:
            self.result = 'Pass'
        else:
            self.result = 'Fail'
    def display(self):
        # invoke the busines functions....
        self.calc_total()
        self.calc_avg()
        self.calc_result()
        print ('roll number ',self.roll)
        print ('student name ',self.name)
        print ('PCM Total is ',self.total)
        print ('PCM avg % is ',self.avg)
        print ('====================')
        print ('RESULT is ',self.result)
print ('---in the START block of main ------ ')
s1 = Student()
s1.input_stud_details()
s1.input_marks_details()
s1.display()
print ('----in the END block of main ----')