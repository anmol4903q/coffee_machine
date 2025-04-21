# ☕ Coffee Vending Machine Simulation (Python)

A beginner-friendly simulation of a coffee vending machine built using Python. This project was created as part of my learning journey to practice loops, conditionals, dictionaries, and function-based programming.

---

## 📋 Features

- 🚀 Menu of 3 coffee options: Espresso, Latte, Cappuccino
- 💰 Accepts currency one-by-one until user types `done`
- 🔁 Runs in a loop so users can order multiple times
- 🧠 Tracks ingredients (milk, water, coffee) in real-time
- 🔐 Hidden `ADMIN` mode to check remaining ingredients
- 🔄 Refunds if not enough money is inserted
- 💵 Returns change if extra money is given

---

## 📌 Menu & Prices

| Coffee      | Price |
|-------------|--------|
| Espresso    | ₹100   |
| Latte       | ₹150   |
| Cappuccino  | ₹170   |

---

## 🧠 Logic & Concepts Used

This project helped me understand the following key concepts in Python:

- **Dictionaries** for managing the coffee menu and ingredients
- **Functions** to handle different coffee types separately
- **Loops (`while`, `for`)** to take repeated input and process recipes
- **Conditional statements** to check for sufficient ingredients and money
- **User input** validation with `.isdigit()` and `.upper()`
- **Simulation logic** for inserting money like in a real vending machine

### 🔧 Challenges I Faced & Solved

| Problem | Solution |
|--------|----------|
| Admin mode wasn't showing ingredients | Used `.upper()` on input and moved the check before money input |
| Accepting money step-by-step | Used a `while True` loop with a break condition on `done` |
| Logic error in ingredient deduction | Created separate recipes in each coffee function and used loops |
| Change & refund handling | Used simple arithmetic with conditions to return or deny coffee |

---

## 🛠 How to Run

1. Make sure Python is installed (version 3+).
2. Clone or download this repo.
3. Run the file `COFFEE_MACHINE.py` using a Python IDE (like Thonny or VS Code) or terminal:
   ```bash
   python COFFEE_MACHINE.py
