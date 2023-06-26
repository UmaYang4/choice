实现一个简单的计算器程序，可以进行基本的加、减、乘、除运算：
python
Copy code
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("请选择操作：")
print("1. 加法")
print("2. 减法")
print("3. 乘法")
print("4. 除法")

choice = input("请输入操作编号：")

if choice in ["1", "2", "3", "4"]:
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))

    if choice == "1":
        result = add(num1, num2)
        operator = "+"
    elif choice == "2":
        result = subtract(num1, num2)
        operator = "-"
    elif choice == "3":
        result = multiply(num1, num2)
        operator = "*"
    else:
        result = divide(num1, num2)
        operator = "/"

    print(f"{num1} {operator} {num2} = {result}")
else:
    print("无效的操作编号。")
