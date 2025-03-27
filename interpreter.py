A = input("Enter an arithmetic expression (x y z): ")
x, y, z = A.split()
x = int(x)
z = int(z)

if y == '+':
    result = x + z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/':
    result = x / z
else:
   result = ("Invalid operator.")
print(result)