
class EvenNumbers:

    def __init__(self):
        self.start = 0
        self.end = 1
        self.i = 0

    def __iter__(self):
        #self.i = start
        self.i = start - 1
        return self

    def __next__(self):
        self.end = end
        self.i += 1
        if self.i % 2 == 0:
            print(self.i)
        if self.i >= self.end:
            raise StopIteration
        return self
        
start = 7
end = 16
my_function_ = EvenNumbers()

print('------------------------------')
print(f'Even numbers in range: start - {start}, end - {end}')

for i in my_function_:
     pass









































