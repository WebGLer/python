def collatz(number):
    if number%2 == 0:
        print(number//2)
        return number//2
    else:
        return (3*number)+1

for i in range(5):
    num = int(input('输入数字：'))
    print(collatz(num))