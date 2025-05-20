def greet():
    teacher_name = input("🧑‍🏫 Enter your name: ").title()
    ask_class = input("🔰 Enter your class (1-8): ")
    if ask_class.isdigit():
        ask_class = int(ask_class)
        if 1 <= ask_class <= 8:
            if teacher_name.isalpha():
                print(f"🎉🎊🧮 Welcome {teacher_name} to the Python Marks Calculator Programme! 🧮🎊🎉")
                print(f"👩‍🏫 Teacher: {teacher_name}")
                print(f"🏫 Standard: {ask_class}")
            else:
                print("⚠️ Invalid name! 🔄Please use alphabets only.")
                exit()
        else:
            if teacher_name.isalpha():
                print("🚫🛑🔄 Please enter a class between 1 and 8 only.")
                exit()
            else:
                print("⚠️🛑🔄Please enter a class between 1 and 8 only and\n🚫🛑 Invalid name! Please use alphabets only.")
                exit()
    else:
        if teacher_name.isalpha():
            print("🚫🛑🔄 Please enter numbers only")
            exit()
        else:
            print("⚠️🛑🔄 Please enter a class between 1 and 8 only.\n🚫🛑Invalid name! Please use alphabets only.")
            exit()

def number_of_students():
    while True:
        try:
            get_students_num = int(input("\n📋🎓How many students marks you wanna calculate❓ "))
            return get_students_num
        except ValueError:
            print("⚠️Please enter only numbers🔄 ")

def get_students_name():
    while True:
        ask_stu_name = input("✏️Enter student's name:  ").title()
        if ask_stu_name.replace(" ", "").isalpha():
            return ask_stu_name
        else:
            print("⚠️Please enter only names🔄")

def get_students_roll(name):
    while True:
        try:
            ask_roll = int(input(f"🆔Enter {name} roll number:  "))
            return ask_roll
        except ValueError:
            print("⚠️Please print only numbers🔄")

def total_marks():
    while True:
        try:
            ask_total_marks = int(input("🔢Enter total marks of each subject: "))
            return ask_total_marks
        except ValueError:
            print("⚠️Please enter only numbers🔄")

def percentage(obtained_marks, total_value):
    result = (obtained_marks / total_value) * 100
    return result

def get_correct(subject, name):
    while True:
        try:
            ask_marks = float(input(f"🧾Enter marks of {name} in {subject}: "))
            if 0 <= ask_marks <= 100:
                return ask_marks
            else:
                print("Please enter between (0-100)")
        except ValueError:
            print("❗ Invalid input.🔄 Please enter a number.")

def gd(marks):
    if 90 <= marks <= 100:
        return "A+🏆"
    elif 80 <= marks < 90:
        return "A🎖️"
    elif 70 <= marks < 80:
        return "B+👍"
    elif 60 <= marks < 70:
        return "B🙌"
    elif 45 <= marks < 60:
        return "C+📉"
    elif 25 <= marks < 45:
        return "C📉👎"
    elif 15 <= marks < 25:
        return "D+📉📉👎"
    else:
        return "Fail😞"

def one_to_eight():
    import time
    num_students = number_of_students()
    i = 0
    while i < num_students:
        get_stu_name = get_students_name()
        ge_st_ro = get_students_roll(get_stu_name)
        get_toa_marks = total_marks()

        ma = get_correct("Maths", get_stu_name)
        en = get_correct("English", get_stu_name)
        hin = get_correct("Hindi", get_stu_name)
        gk = get_correct("G.K", get_stu_name)
        sc = get_correct("Science", get_stu_name)
        st = get_correct("Social Science", get_stu_name)
        cm = get_correct("Computer", get_stu_name)

        ma_1 = round(percentage(ma, get_toa_marks), 2)
        en_1 = round(percentage(en, get_toa_marks), 2)
        hin_1 = round(percentage(hin, get_toa_marks), 2)
        gk_1 = round(percentage(gk, get_toa_marks), 2)
        sc_1 = round(percentage(sc, get_toa_marks), 2)
        st_1 = round(percentage(st, get_toa_marks), 2)
        cm_1 = round(percentage(cm, get_toa_marks), 2)

        total_obtained = ma + en + hin + gk + sc + st + cm
        total_max = get_toa_marks * 7
        overall_percentage = round(percentage(total_obtained, total_max), 2)
        overall_grade = gd(overall_percentage)

        print(".." * 50)
        print(f"\n🗂️💾 Marks of {get_stu_name} (Roll: {ge_st_ro}) recorded successfully!\n")
        time.sleep(1)

        print("🏁" * 60)
        print(f"🏁 Name: {get_stu_name:<15} | Subject               | Marks  | Grade   | Percentage 🏁")
        print(f"🏁 Roll No: {ge_st_ro:<12} | Maths                 | {ma:<6} | {gd(ma):<5} | {ma_1:<9}% 🏁")
        print(f"🏁 {'':<26} | Science               | {sc:<6} | {gd(sc):<5} | {sc_1:<9}% 🏁")
        print(f"🏁 {'':<26} | S.S.T                 | {st:<6} | {gd(st):<5} | {st_1:<9}% 🏁")
        print(f"🏁 {'':<26} | Hindi                 | {hin:<6} | {gd(hin):<5} | {hin_1:<9}% 🏁")
        print(f"🏁 {'':<26} | English               | {en:<6} | {gd(en):<5} | {en_1:<9}% 🏁")
        print(f"🏁 {'':<26} | Computer              | {cm:<6} | {gd(cm):<5} | {cm_1:<9}% 🏁")
        print(f"🏁 {'':<26} | G.K                   | {gk:<6} | {gd(gk):<5} | {gk_1:<9}% 🏁")
        print("🏁" * 60)
        print(f"🏁 {'Overall Percentage':<26} | {'':<6} | {overall_grade:<5} | {overall_percentage:<9}% 🏁")
        print("🏁" * 60)


        filename = f"{get_stu_name.replace(' ', '_')}_marks.txt"
        with open(filename, "w") as file:
            file.write(f"Marks Report for {get_stu_name} (Roll No: {ge_st_ro})\n")
            file.write("-" * 50 + "\n")
            file.write(f"{'Subject':<20} {'Marks':<8} {'Grade':<8} {'Percentage':<10}\n")
            file.write("-" * 50 + "\n")
            file.write(f"{'Maths':<20} {ma:<8} {gd(ma):<8} {ma_1}%\n")
            file.write(f"{'Science':<20} {sc:<8} {gd(sc):<8} {sc_1}%\n")
            file.write(f"{'Social Science':<20} {st:<8} {gd(st):<8} {st_1}%\n")
            file.write(f"{'Hindi':<20} {hin:<8} {gd(hin):<8} {hin_1}%\n")
            file.write(f"{'English':<20} {en:<8} {gd(en):<8} {en_1}%\n")
            file.write(f"{'Computer':<20} {cm:<8} {gd(cm):<8} {cm_1}%\n")
            file.write(f"{'G.K':<20} {gk:<8} {gd(gk):<8} {gk_1}%\n")
            file.write("-" * 50 + "\n")
            file.write(f"{'Overall Percentage':<20} {'':<8} {overall_grade:<8} {overall_percentage}%\n")
