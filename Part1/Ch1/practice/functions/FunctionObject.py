def func1(x):
    return x ** 2

def func2(x):
    return 10 * x

def func3(x):
    return x + 3

f1 = func1
f2 = func2
f3 = func3

print(f1(3))            # x²
print(f2(f1(3)))        # 10x²
print(f3(f2(f1(3))))    # 10x² + 3

x = 3

func_list = [f1, f2, f3]

for f in func_list:
    x = f(x)

print(x)