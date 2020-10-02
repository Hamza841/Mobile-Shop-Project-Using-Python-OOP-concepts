import time


class AdminFunction:
    @staticmethod
    def show_records():
        import os
        if os.path.exists("mobile.py"):
            mobiles = open("mobile.py", "r")
            mobile = mobiles.read()
            print(mobile, "\n")
            time.sleep(2)
            mobiles.close()
            again_choice = int(input("Press '1' to Return to Admin Panel OR '0' for exiting the program: "))
            if again_choice == 1:
                admin_panel()
            elif again_choice == 0:
                exit()
        else:
            print("File don't exits..")
            again = int(input("Press '1' to Return to Admin Panel OR '0' for exiting the program: "))
            if again == 1:
                admin_panel()
            elif again == 0:
                exit()
            else:
                print("wrong input..Automatically exiting the program...")
                exit()

    @staticmethod
    def insert_records():
        mobiles = open("mobile.py", "a")
        company = input("Enter company name: ")
        mobile = input("Model no: ")
        manufacture = input("Enter year of manufacture: ")
        price = input("Enter the price of mobile: ")
        condition_mobile = input("Enter condition of mobile: ")
        print("\nRecord Entered successfully...")
        mobiles.write(f"\n{company}  {mobile}  {manufacture}  {price}  {condition_mobile}")
        mobiles.close()
        choice_again = int(input("Press '1' to enter Admin Panel OR '0' to exit the program: "))
        if choice_again == 1:
            admin_panel()
        elif choice_again == 0:
            exit()
        else:
            print("Wrong option selected returning you back to Admin Panel..")
            time.sleep(1)
            admin_panel()

    @staticmethod
    def delete_records():
        import os
        if os.path.exists("mobile.py"):
            print("Deleting file in a while....")
            time.sleep(2)
            print("Please Wait.....")
            os.remove("mobile.py")
            time.sleep(1)
            print("File Deleted Successfully...")
        else:
            print("You can't delete a file which don't even exists..")
        choice_delete = int(input("Press '1' for Admin Panel or '0' for exit"))
        if choice_delete == 1:
            admin_panel()
        elif choice_delete == 0:
            print("Exiting the program..")
            exit()
        else:
            print("Wrong option selected..Exiting the program..")
            exit()


records = AdminFunction()


def admin_panel():
    print("Welcome Dear Admin!!Please Enter AdminId and Password to Enter the Admin Panel..")
    admin_id = input("Enter AdminId: ")
    if admin_id == "Hamza":
        admin_pass = input("Enter your Password: ")
        if admin_pass == "Hamza000":
            print(f"Welcome Dear {admin_id} sir!!")
            time.sleep(2)
            print("""
            1)press 1 for displaying records
            2)press 2 for inserting records
            3)press 3 to delete records
            """)
            admin_choice = int(input("Enter your choice: "))
            if admin_choice == 1:
                records.show_records()

            elif admin_choice == 2:
                records.insert_records()

            elif admin_choice == 3:
                records.delete_records()

            else:
                print("Option not available sir! Taking to back to Choice again...")
                time.sleep(2)

        else:
            print("Enter the password correctly sir!")
            time.sleep(2)
            admin_panel()

    else:
        print("Your AdminId is wrong.Type correctly sir!")
        print("Taking you back to Admin Panel..")
        time.sleep(2)
        admin_panel()


class Customer:
    @staticmethod
    def __init__():
        print("Welcome Dear User!")


def customer():
    print("*****Welcome Dear Customer...")
    print("""
    Press 1) for Viewing the collection of mobiles phones to buy.....
    press 2) for selling your old mobile at affordable price.........
    
    """)
    try:
        user_choice = int(input("What you want: "))
        if user_choice == 1:
            import os
            os.system("mobile.py")
        else:
            print("Hi")
    except ValueError:
        print("Error is ", ValueError)


print("Welcome To Best Mobile Shop")
print("""
1) Press 1 for Admin Panel
2) 2 for Customer Menu
""")

try:
    choice = int(input("Enter your choice sir: "))
    if choice == 1:
        admin_panel()
    elif choice == 2:
        customer()
except ValueError:
    print("You entered an option which is not allowed", ValueError)
