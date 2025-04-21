# ☕ Coffee Vending Machine Simulation

# 📋 Coffee menu with recipes and prices
coffee_menu = [
    {
        "name": "espresso",
        "cost": 100,
        "milk": 0,
        "water": 50,
        "coffee": 18
    },
    {
        "name": "latte",
        "cost": 150,
        "milk": 150,
        "water": 200,
        "coffee": 24
    },
    {
        "name": "cappuccino",
        "cost": 170,
        "milk": 100,
        "water": 250,
        "coffee": 24
    }
]

# 🧃 Current available ingredients in the machine
ingredients = {
    "water": 1000,    
    "milk": 800,       
    "coffee": 500      
}

# 🔧 Function to handle Espresso orders
def espresso(ingredients, order, rupees):
    recipe = {"water": 50, "milk": 0, "coffee": 18}
    cost = 100
    change = 0

    if order == "ESPRESSO":
        # ✅ Check ingredient availability
        if ingredients["water"] >= 50 and ingredients["milk"] >= 0 and ingredients["coffee"] >= 18:
            for i in recipe:
                ingredients[i] -= recipe[i]

            # 💰 Check if payment is enough
            if rupees == cost:
                print("✅ Your coffee will be ready in a while...")
            elif rupees > cost:
                change = rupees - cost
                print(f"💸 You got ₹{change} back")
                print("✅ Your coffee will be ready in a while...")
            elif rupees < cost:
                print('''❌ Not enough money!
💸 Your money will be refunded...''')
        else:
            print("🚫 Sorry! We're out of ingredients.")

# 🔧 Function to handle Latte orders
def latte(ingredients, order, rupees):
    recipe = {"water": 200, "milk": 150, "coffee": 24}
    cost = 150
    change = 0

    if order == "LATTE":
        if ingredients["water"] >= 200 and ingredients["milk"] >= 150 and ingredients["coffee"] >= 24:
            for i in recipe:
                ingredients[i] -= recipe[i]

            if rupees == cost:
                print("✅ Your coffee will be ready in a while...")
            elif rupees > cost:
                change = rupees - cost
                print(f"💸 You got ₹{change} back")
                print("✅ Your coffee will be ready in a while...")
            elif rupees < cost:
                print('''❌ Not enough money!
💸 Your money will be refunded...''')
        else:
            print("🚫 Sorry! We're out of ingredients.")

# 🔧 Function to handle Cappuccino orders
def cappuccino(ingredients, order, rupees):
    recipe = {"water": 100, "milk": 250, "coffee": 24}
    cost = 170
    change = 0

    if order == "CAPPUCCINO":
        # 🚨 Your ingredient check had wrong values before, fixed below!
        if ingredients["water"] >= 250 and ingredients["milk"] >= 100 and ingredients["coffee"] >= 24:
            for i in recipe:
                ingredients[i] -= recipe[i]

            if rupees == cost:
                print("✅ Your coffee will be ready in a while...")
            elif rupees > cost:
                change = rupees - cost
                print(f"💸 You got ₹{change} back")
                print("✅ Your coffee will be ready in a while...")
            elif rupees < cost:
                print('''❌ Not enough money!
💸 Your money will be refunded...''')
        else:
            print("🚫 Sorry! We're out of ingredients.")

# 🔁 Main program loop
ch = 'y'
while ch == 'y':
    print()
    print("*" * 90)
    print()
    print("📜 Our Menu:")
    for i in coffee_menu:
        print(f'👉 {i["name"].capitalize()} : ₹{i["cost"]}')
        
    order = input("\n🤖 What would you like to order: ").upper()

    # 🔐 Admin access to check ingredient stock
    if order == "ADMIN":
        print("\n💡 Ingredients left in the machine:")
        for item, amount in ingredients.items():
            print(f"  {item.capitalize()}: {amount}ml")
        continue  # ⛔ Skip payment for admin

    # 💸 Accepting coins one by one
    rupees = 0
    while True:
        r = input("💰 Insert money (type 'done' when you're done): ").upper()
        if r == 'DONE':
            break
        elif r.isdigit():
            rupees += int(r)
            print(f"💵 Your inserted total: ₹{rupees}")
        else:
            print("❗ Please enter a valid amount or type 'done'.")

    # ☕ Call the appropriate function based on the order
    if order == 'ESPRESSO':
        espresso(ingredients, order, rupees)
    elif order == 'LATTE':
        latte(ingredients, order, rupees)
    elif order == 'CAPPUCCINO':
        cappuccino(ingredients, order, rupees)
    else:
        print("⚠️ Invalid order. Please try again.")

    ch = input("\n🔁 Would you like another coffee? (y/n): ").lower()




