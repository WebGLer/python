def span(num):
    print('num:',num)
    print("type(num):",type(num))
    try:
        return 50/num
    except ZeroDivisionError:
       return 'Error : Invalid argument'
print(span(10))
print(span(0))
print(span(5))
print(span(20))