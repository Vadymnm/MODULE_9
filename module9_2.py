
# =================  Function factory  =====================
print('   Function factory ')
def create_operation(operation):
    if operation == "multiply":
        def multiply(x,y):
            return x*y
        return multiply

    if operation == "divide":
        def divide(x,y):
            return x / y
        return divide

my_func_multiply = create_operation("multiply")
print(my_func_multiply(5,12))

my_func_divide = create_operation("divide")
print(my_func_divide(12,5))
#print(my_func_divide(12,0))

print('-------------------------------------------------')
# =================  lambda  =====================

print('  lambda  ')
pow_ = lambda x, y: x ** y
print(pow_(55, 3))

def pow (x, y):
    return x ** y
    return pow

print(pow(3,4))

print('-------------------------------------------------')
# =================  Calling Objects  =====================
print('  Calling Objects ')
class Rect:
   def __init__(self, value1,value2):
       self.value1 = value1
       self.value2 = value2
   def __call__(self,value1,value2):
       return [self.value1 * self.value2]

a = 5
b = 25
sqr = Rect(a,b)
print(sqr(a,b))