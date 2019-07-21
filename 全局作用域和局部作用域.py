def span():
    print(egg)      #代码块中没有egg变量则自动从上一级作用域里去找

egg = 40
span()
print(egg)