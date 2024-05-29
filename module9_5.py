
def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        print(' Summ = ',number)
        for i in range(2, int(number ** 0.5) + 1):
#            print('i = ',i,'number % i =',(number % i))
            if number % i == 0:
                print('составное')
                return False
        else:
            print('простое')
        return True
    return wrapper

@is_prime
def sum_tree(*args):
    sum_ = 0
    for fig in args:
        sum_ += fig
    return (sum_)


result = sum_tree(2,3,6,6)
print(result)

























