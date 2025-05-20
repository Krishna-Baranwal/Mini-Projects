import sys

name = input("🧑‍💻 Enter your name:  ").title()
print(f"Welcome {name}🎉 to the Basic Python Calculator program 🧮!")

try:
    ask_times = int(input("\nHow many times will you run the program❓  "))
except ValueError:
    print("Not a number❌")
    sys.exit()


history = {
    "history_add": [],
    "history_multiply": [],
    "history_division": [],
    "history_minus": []
}

def get_a_number(function):
    while True:
        try:
            a = float(input(function))
            return a
        except ValueError:
            print("Not a number🔴🛑")

def calculate():
    try:
        num_1 = get_a_number("\n🔢 Enter first number:  ")
        num_2 = get_a_number("🔢 Enter second number:  ")

        print('\nAdd -----> Type ➕\nSubtract -----> Type ➖\nDivide -----> Type ➗\nMultiply -----> Type ✖️ ')
        operation = input("\nEnter Operation 🛠️:  ")

        if operation == '+':
            result = num_1 + num_2
            print(f'🧠 Addition of number {num_1} ➕ {num_2} is {result}')
            history["history_add"].append(result)

        elif operation == '-':
            minus1 = int(input(f"1) {num_1} ➖ {num_2}\n2) {num_2} ➖ {num_1}:: Type 1 or 2: ⚖️ "))
            match minus1:
                case 1:
                    result1 = num_1 - num_2
                    print(f"🧠 Subtraction of {num_1} ➖ {num_2} is {result1}")
                    history["history_minus"].append(result1)
                case 2:
                    result2 = num_2 - num_1
                    print(f"🧠 Subtraction of {num_2} ➖ {num_1} is {result2}")
                    history["history_minus"].append(result2)
                case _:
                    print('Invalid option🔴🛑')

        elif operation == '*':
            result3 = num_1 * num_2
            print(f"🧠 Multiplication of {num_1} ✖️ {num_2} is {result3}")
            history["history_multiply"].append(result3)

        elif operation == '/':
            divide = int(input(f"1) {num_1} ➗ {num_2}\n2) {num_2} ➗ {num_1}:: Type 1 or 2: ⚖️  "))
            if divide == 1:
                try:
                    result4 = num_1 / num_2
                    print(f"🧠 Division of {num_1} ➗ {num_2} is {result4}")
                    history["history_division"].append(result4)
                except ZeroDivisionError:
                    print("Division by zero is invalid❌")

            elif divide == 2:
                try:
                    result5 = num_2 / num_1
                    print(f"🧠 Division of {num_2} ➗ {num_1} is {result5}")
                    history["history_division"].append(result5)
                except ZeroDivisionError:
                    print("Division by zero is invalid❌")

            else:
                print('Invalid option🔴🛑❌')

        else:
            print("Invalid operation symbol❌")

    except ValueError:
        print("Invalid🔴🛑❌")

i = 0
while i < ask_times:
    calculate()
    ask_end = input("🔄 Do you want to continue running the program❓ [y/n]  ").lower()
    if ask_end == 'n':
        break
    elif ask_end == 'y':
        i += 1
    else:
        print("Invalid option🛑❌")

see_history = input("\n📝Do you want to see your history❓ [y/n]   ").lower()
if see_history == 'y':
    print(f"\n📜 Your ➕ addition history ===>  {history['history_add']}")
    print(f"📜 Your ➖ subtraction history ===>  {history['history_minus']}")
    print(f"📜 Your ➗ division history ===>  {history['history_division']}")
    print(f"📜 Your ✖️ multiplication history ===>  {history['history_multiply']}")
elif see_history == 'n':
    print(f"\n🎉📊💻\nShri Harivansh {name}\n🎉📊💻")
else:
    print("Invalid option🛑❌")

print(f"\n🎉 Thank you {name} for using the Basic Python Calculator! 🚀 Have a great day! 😊")
