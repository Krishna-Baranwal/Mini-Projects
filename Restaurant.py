# Libraries
from time import sleep
import random
import logging
import qrcode
import smtplib
from email.message import EmailMessage
import pyttsx3


# User logging/logout  system
logging.basicConfig(filename="user1.log\n", level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")


def user_logging(username):
    logging.info(f"User {username} has logged in")

def user_logout(username):
    logging.info(f"User {username} has logout")



# Sending email
def send_bill_email(to_email, user_name, order_list, total):
    try:
        email_sender = "kbaranwal638@gmail.com"
        email_password = "qmpx oazb hlyg zcuy"
        email_receiver = to_email

        subject = f"🍽️ Your FoodCode Kitchen Order Bill - Thank You {user_name}!"

        body = "📄 Here is your order summary:\n\n"
        body += f"{'Item':<20}{'Qty':<6}{'Total Price':>12}\n"
        body += "-" * 50 + "\n"

        for item, info in order_list.items():
            price = f"₹{info['Total Price']}"
            body += f"{item.strip():<20}{str(info['Quantity']):<5}{price:>12}\n"

        body += "-" * 50 + "\n"
        body += f"{'Total':<25}{'₹' + str(total):>12}\n"
        body += "\n🙏 Thank you for ordering from FoodCode Kitchen!\n🍽️ Visit Again!"

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_sender, email_password)
            smtp.send_message(em)

        print("📧 Email sent successfully!")

    except Exception as e:
        print("❌ Failed to send email:", e)



# Details of User
def get_name():
    while True:
        user_name = input("📝 Please Register your name here:  ").title().strip()
        if user_name.replace(" ", "").isalpha():
            return user_name
        else:
            print("🚫 Invalid name. Please use only alphabets.")

def get_phone_number():
    while True:
        ask_phone_number = input("📞 Please enter your Phone/Mobile number: ")
        if ask_phone_number.isdigit() and len(ask_phone_number) == 10:
            return ask_phone_number
        else:
            print("❌ Invalid number. Must be 10 digits. Try again.")

def get_gmail():
    while True:
        ask_email = input("📧 Please enter your Gmail address: ").strip()
        if ask_email.endswith("@gmail.com") and "@" in ask_email and ask_email.index("@") > 0:
            return ask_email
        else:
            print("🛑 Invalid Gmail. Please enter a valid Gmail like 'example@gmail.com'.")

# Order related queries
def ask_number_of_orders():
    while True:
        get_order_num = input(f"\n🛒 How many items would you like to order from this menu? ")
        if get_order_num.isdigit():
            return int(get_order_num)
        else:
            print("❌ Enter a valid number.")

def orders_quantity():
    while True:
        quantity = input(f"🔢 Enter quantity: ")
        if quantity.isdigit():
            return int(quantity)
        else:
            print("⚠️ Please enter only numeric values.")
# Customer feedback
def feedback():
    feed = input("\n🗣️ Would you like to give a feedback? [y/n]: ").strip().lower()
    if feed == 'y':
        rate = input("⭐ Would you like to give a rating? [y/n]: ").strip().lower()
        if rate == 'y':
            while True:
                rate_ask = input("👉 Please give a rating (1-5): ").strip()
                if rate_ask.isdigit() and 1 <= int(rate_ask) <= 5:
                    print(f"🙏 Thank you for rating us {rate_ask} ⭐")
                    break
                else:
                    print("❌ Invalid rating. Enter a number between 1 and 5.")
        else:
            print("👍 Skipped rating.")

        feed_ask = input("✍️ Please write your feedback here (or press enter to skip): ").strip()
        if feed_ask:
            print("✅ Thank you for your valuable feedback!")
            return feed_ask
        else:
            print("👍 Feedback skipped.")
    else:
        print("👍 No problem! Thank you for visiting FoodCode Kitchen.")




# Menu of dishes
def menu():
    dishes = {
        "sweets_menu": {
            "Gulab Jamun": 40,
            "Rasgulla": 35,
            "Kaju Katli": 60,
            "Halwa": 30,
            "Jalebi": 25,
            "Besan Ladoo": 45,
            "Rabri": 55,
            "Barfi": 50,
            "Cham Cham": 38,
            "Soan Papdi": 20
        },
        "spicy_menu": {
            "Chilli Paneer": 120,
            "Spicy Noodles": 110,
            "Mirchi Bajji": 25,
            "Paneer Tikka": 130,
            "Masala Corn": 40,
            "Tandoori Paneer": 150,
            "Veg Hakka Noodles": 100,
            "Gobi Manchurian": 95,
            "Paneer ": 115,
            "Spicy Fries": 60
        },
        "beverage_menu": {
            "Coke": 40,
            "Lassi": 50,
            "Lemonade": 35,
            "Cold Coffee": 60,
            "Butter Milk": 30,
            "Sweet Lassi": 55,
            "Mango Shake": 70,
            "Rose Milk": 45,
            "Badam Milk": 65,
            "Masala Chaas": 30
        },
        "fastfood_menu": {
            "Veg Pizza": 180,
            "Aloo Tikki Burger": 90,
            "French Fries": 60,
            "Cheese Pasta": 150,
            "Veg Sandwich": 70,
            "Garlic Bread": 85,
            "Maggie Masala": 40,
            "Paneer Burger": 95,
            "Stuffed Roll": 75,
            "Corn Cheese Balls": 80
        },
        "southindian_menu": {
            "Masala Dosa": 80,
            "Idli Sambhar": 60,
            "Vada": 50,
            "Uttapam": 70,
            "Onion Dosa": 85,
            "Set Dosa": 60,
            "Ghee Roast Dosa": 90,
            "Mysore Dosa": 75,
            "Rava Dosa": 80,
            "Upma": 55
        },
        "snacks_menu": {
            "Samosa": 20,
            "Momos": 40,
            "Veg Sandwich": 50,
            "Pakora": 30,
            "Paneer Cutlet": 45,
            "Bread Roll": 35,
            "Kachori": 25,
            "Dhokla": 40,
            "Mini Kathi Roll": 60,
            "Aloo Tikki": 30
        }
    }
    return dishes
# Advanced feature
def generate_qr_code(payment_link):
    qr = qrcode.make(payment_link)
    qr.show()  # opens the QR code image

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Payment mode
def online_payment(total, user_name):
    print("\n💳 You chose Online Payment!")
    print("🧾 Amount to be paid: ₹", total)
    sleep(2)

    payment_link = f"upi://pay?pa=foodcode@upi&pn=FoodCodeKitchen&am={total}&cu=INR"
    sleep(1)
    print("📲 Generating UPI QR Code... Please wait.")
    sleep(2)

    generate_qr_code(payment_link)

    confirm = input("✅ Have you scanned the QR and done payment? [yes/no]: ").strip().lower()
    if confirm == "yes":
        message = f"A payment of {total} rupees is done by {user_name}"
        print(f"\n💸 {message} ✅")
        speak(message)  # 🎤 Speak out loud like Alexa
        print("💰 Payment Successful! Thank you for paying online 🙏")
        return True
    else:
        print("❌ Payment not completed. Please try again or choose another method.")
        return False


# Main part
def main(mail):
    all_menu = menu()
    name_ = get_name()

    category_map = {
        "CH": "spicy_menu",
        "SP": "spicy_menu",
        "SW": "sweets_menu",
        "BE": "beverage_menu",
        "FF": "fastfood_menu",
        "SI": "southindian_menu",
        "SS": "snacks_menu"
    }
    print(f"\nPrinting your menus option")
    sleep(1)
    print("\n---------🍱 List of Foods 🍱---------")
    print("1. 🌶️🔥 Chilly/Spicy     -----> Type [CH/SP]")
    print("2. 🍬 🍰 Sweets          -----> Type [SW]")
    print("3. 🥤 🍹 Beverages       -----> Type [BE]")
    print("4. 🍔 🍟 Fast Food       -----> Type [FF]")
    print("5. 🍛 🥘 South Indian    -----> Type [SI]")
    print("6. 🍩 🥪 Snacks          -----> Type [SS]")

    while True:
        user_choice_in_menu = input("📌 Please enter your choice:  ").upper()

        if user_choice_in_menu in category_map:
            menu_key = category_map[user_choice_in_menu]
            sleep(1)
            print("\n⏳ Loading menu items...\n")
            sleep(3)

            selected_menu = all_menu[menu_key]
            print(f"========== {menu_key} ==========")
            for index, (item, price) in enumerate(selected_menu.items(), start=1):
                print(f"{index}. 🍽️ {item.ljust(22)} ₹{str(price).rjust(3)}")

            sleep(2)
            order_count = 1
            order_list = {}

            num_of_orders = ask_number_of_orders()
            sleep(0.5)
            while order_count <= num_of_orders:
                get_order = input(f"🍴 Please enter your {order_count} order:  ").title().strip()
                if get_order in selected_menu:
                    qty = orders_quantity()
                    if get_order in order_list:
                        print("⚠️ You already ordered this. Please choose another item.")
                        continue
                    order_list[get_order] = {
                        "Total Price": selected_menu[get_order] * qty,
                        "Quantity": qty
                    }

                    print(f"\n✅ Order placed successfully!")
                    order_count += 1
                else:
                    print("\n⚠️ This item is not in the menu. Please choose from above.")

            # Suggest a famous item
            suggestion = random.choice(list(selected_menu))
            sleep(1)
            print("\n🌟 Chef's Recommendation Just for You! 🌟")
            sleep(0.5)
            suggestion_ask = input(f"👉 Would you like to try our famous '{suggestion}'? [y/n]  ")
            if suggestion_ask.lower() == 'y':
                qty = orders_quantity()
                order_list[suggestion] = {
                    "Total Price": selected_menu[suggestion] * qty,
                    "Quantity": qty
                }
                print(f"\n✅ Added Chef's Special to your order!")
            else:
                print("👍 No problem! Moving ahead...")

            # Bill Display
            print("\n📋 Generating Your Bill... Please wait ⏳")
            sleep(4)
            print("\n" + "=" * 40)
            print("        🧾 FoodCode Kitchen Bill")
            print("=" * 40)
            print(f"{'🍛 Item'.ljust(20)} {'Qty'.center(5)} {'Total Price'.rjust(8)}")
            print("-" * 40)

            total = 0
            for item, info in order_list.items():
                name = item.ljust(20)
                qty = str(info['Quantity']).center(5)
                price = f"₹{info['Total Price']}".rjust(8)
                print(f"{name}{qty}{price}")
                total += info['Total Price']

            print("-" * 40)
            print(f"{'💰 Total'.ljust(25)}{'₹' + str(total).rjust(10)}")
            print("=" * 40)

            while True:
                payment_method = input("\n💰 Choose payment method: [1] Cash  [2] Online : ").strip()
                if payment_method == "1":
                    print("💵 Cash payment selected. Please pay at the counter.")
                    break
                elif payment_method == "2":
                    if online_payment(total, name_):
                        break
                    else:
                        print("🔁 Let's try payment again.")
                else:
                    print("❌ Invalid choice. Please select again.")

            ask_email = input("\n📩 Would you like the bill emailed to you? [yes/no]: ").lower()
            if ask_email == "yes":
                send_bill_email(mail, name_, order_list, total)

            break

        else:
            print("⚠️ Invalid input. Please try again with CH, SW, BE, etc.\n")


if __name__ == "__main__":
    print("-------------🍽️ Welcome to FoodCode Kitchen 🍽️-------------\n")
    print("🙋 Hello sir/ma'am\n📥 We need a few details from you. Please register below:")


    # Details asking
    sleep(3)
    name = get_name()
    sleep(1)
    phone = get_phone_number()
    sleep(1)
    mail = get_gmail()
    email_sender = "kbaranwal638@gmail.com"

    # User logging
    user_logging(name)

    # Printing details
    print("\n🧾 Fetching your details...")
    sleep(3)
    print("\n📄 Your details are here:")
    print(f"🆔 Name: {name}")
    print(f"☎️ Phone/Mobile Number: {phone}")
    print(f"📧 Gmail: {mail}\n")


    # Advanced Feature for speaking
    speak(f"Welcome {name}, you are now logged in.")
    ...

    # Main part
    main(mail)

    # Feedback
    feedback()

    # User logout
    user_logout(name)
    speak(f"Goodbye {name}, you are now logged out.")
