def get_fuel_percentage():
    while True:
        
        fraction = input("Fraction: ")
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError
        if x > y:
          raise ValueError
        percentage = round((x / y) * 100)

        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return f"{percentage}%"

result = get_fuel_percentage()
print(result)
