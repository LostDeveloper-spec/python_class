menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
def main():
end = {
    "finish": 0,
    "done":0,
    "finished":0
}

    total = 0.0


    while True:
        item = input("Item: ").strip().title()
        if item in menu:
            total += menu[item]
            print(f"Total: ${total:.2f}")
        if item in end[item]:
            break

main()