def value(greeting: str) -> int:
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

def main():
    user_input = input("Greeting: ")
    print(f"${value(user_input)}")

main()