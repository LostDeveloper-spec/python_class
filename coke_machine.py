amount_due = 50
good_coins = [25, 10, 5]

while amount_due > 0:
    print(f"Amount Due: {amount_due} cents")
    coin = int(input("Insert Coin: "))

    if coin in good_coins:
        amount_due-=coin

print(f"Change Owed: {abs(amount_due)} cents") 
