"""def get_fuel_percentage():
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
"""
#New

def convert(fraction):
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if x > y:
            raise ValueError("Numerator cannot be greater than denominator.")
        percentage = round((x / y) * 100)
        return percentage
    except ValueError:
        raise ValueError("Invalid input. Provide integers in X/Y format.")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError) as e:
            print(e)