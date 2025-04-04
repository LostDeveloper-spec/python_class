fruit_calories = {"apple": 130, "avocado": 50, "banana": 110, "blueberries": 85, "cantaloupe": 50, "cherries": 100, "grapefruit": 60, "grapes": 90, "honeydew melon": 50, "kiwifruit": 90, "lemon": 15, "lime": 20, "nectarine": 60, "orange": 80, "peach": 60, "pear": 100,"pineapple": 50, "plums": 70, "strawberries": 50, "watermelon": 80}

fruit = input("Item: ").strip().lower()

if fruit in fruit_calories:
    print(f"Calories: {fruit_calories[fruit]}")
else:
    print("Not a fruit/not in database")