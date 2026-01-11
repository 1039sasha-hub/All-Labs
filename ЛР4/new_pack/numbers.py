def even(num):
    if num % 2 == 0:
        print('Число четное')
    else:
        print('Число нечетное')
    
    def comp(a,b):
        if a > b:
            print('Число {a} больше числа {b}')
        elif a < b:
             print('Число {a} меньше числа {b}')
        else:
            print('Числа равны')