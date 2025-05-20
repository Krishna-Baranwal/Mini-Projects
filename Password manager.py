def get_name():
    while True:
            name = input(f"Enter your name:  ").title()
            if not name.isalpha():
                print("Please only alphabets")
            else:
                print( name)
                break
get_name()





