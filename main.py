# STUDENT_NAME
# STUDENT_TP

import os
from datetime import datetime

current_user = []


def main():
    menu = 0
    while menu < 5:
        print(" ")

        print("""\t\t\t\t  $$$$$$$$$$$$$$@@@@@@@@@@@@@@@@@@@@@@@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
                 "$                                                                           $"
                 "$		            ONLINE EVENT MANAGEMENT SYSTEM (OEMS) 	                  $"
                 "$                                                                           $"
                 "$$$$$$$$$$$$$$@@@@@@@@@@@@@@@@@@@@@@@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
                 """)
        print('\t\t\t\t\t\t  [1] Admin \n\t\t\t\t\t\t'
              '  [2] Registered Customer \n\t\t\t\t\t\t'
              '  [3] Non-Registered Customer \n\t\t\t\t\t\t'
              '  [4] Quit \n ')

        menu = int(input('\tSelect User Type: '))
        print('----------------------------------------------------------------------------------------------------')

        if menu == 1:
            print('\n******************************* ADMIN LOGIN PAGE *********************************')
            print("\nPlease enter your Log in Credentials")
            while True:
                try:
                    username = input("Please enter your username: ")
                    password = input("Please enter your password: ")
                    value = Admin_Login(username, password)
                    if value:
                        Admin_Menu()
                        break
                except Exception as e:
                    print(e)
            break
        elif menu == 2:
            print(
                '\n********************************* REGISTERED CUSTOMER LOGIN PAGE ***********************************')
            while True:
                try:
                    username = input("Please enter your username: ")
                    password = input("Please enter your password: ")
                    value = customer_Login(username, password)
                    if value:
                        print('Hello !', value[1], " you have logged in successfully.")
                        current_user.append(value[1])
                        Registered_Customer_Main()
                        break
                    print("Invalid Credentials, Please Try Again!")
                except Exception as e:
                    print(e)
                break
        elif menu == 3:
            Non_Registered_Customer_Main()
            break
        elif menu == 4:
            print("Thank You For Using The System")
            exit()
            break
        else:
            print("Invalid User Input")

        restart = input("Do You Wish to Continue(Y/N): ").lower()
        if restart == 'y':
            main()
        else:
            print("Thank You For Using The System")
            exit()


def fileIsEmpty(file):
    file_path = file
    if os.stat(file_path).st_size == 0:  # check if size of file is 0
        return True


def Admin_Login(username, password):
    flag = 0
    for line in open("adminLogin.txt", "r").readlines():
        login_info = line.split(";")
        if username == login_info[0] and password == login_info[1]:
            print("Welcome")
            flag = 1
            return flag
        elif username == login_info[0] or password == login_info[1]:
            print("Invalid Username or Password Input!")
            return flag
        else:
            print("Username and Password Does Not Exist!")
            return flag


def customer_payment():
    if not fileIsEmpty("AllBookings.txt"):
        customer_File = open("AllBookings.txt", "r")
        event_records = customer_File.readlines()  # return all lines in the file, as a list
        record = 0
        for event_record in event_records:
            print("[", (record + 1), "]",
                  "Event Name: " + event_record.split(",")[2] + ", Customer: " + event_record.split(",")[1] +
                  " , No of Tickets: " + event_record.split(",")[3] +
                  " , Total Amount: " + event_record.split(",")[4].strip())
            record += 1
        customer_File.close()
    else:
        print("No Payment Details Are Available!")


def search_Customer(id_):
    file = open("AllCustomers.txt", "r")
    customer = file.readlines()
    flag = 0

    for b_record in customer:
        line = b_record.split(",")
        if id_ in line:
            flag = 1
            print("\n[1] Name: " + b_record.split(",")[0] + " ,Username: " + b_record.split(",")[1]
                  + " ,Contact Number: " + b_record.split(",")[3])
    if flag == 0:
        print("No Record Found!")

    while True:
        try:
            restart = str(input("Enter 'Y' to go Back to Menu: ").lower())
            if restart == 'y':
                Admin_Menu()
                break
            print("Invalid Value entered")
        except Exception as e:
            print(e)


def search_payment(name_):
    file = open("AllBookings.txt", "r")
    payment = file.readlines()
    count = 0
    flag = 0

    for p_record in payment:
        line = p_record.split(",")
        if name_ in line:
            flag = 1
            print("[", (count + 1), "]",
                  "Booking ID: " + p_record.split(",")[0] + " ,Customer: " + p_record.split(",")[1]
                  + " ,Event Name: " + p_record.split(",")[2] + " ,Total Amount: " + p_record.split(",")[4].strip())
        count = +1
    if flag == 0:
        print("No Record Found!")

    while True:
        try:
            restart = str(input("Enter 'Y' to go Back to Menu: ").lower())
            if restart == 'y':
                Admin_Menu()
                break
            print("Invalid Value entered")
        except Exception as e:
            print(e)


def Admin_Menu():
    adminMenu = 0
    while adminMenu < 9:
        print('\n******************************* ADMIN MAIN MENU PAGE *********************************')
        print("\t\t[1] Add Event in the Relevant Category \n\t\t[2] Modify Event")
        print("\t\t[3] Display all records\n\t\t[4] Search Specific record of ")
        print("\t\t[5] Exit\n")

        adminMenu = int(input('Select Your Option to enjoy the feature: '))

        if adminMenu == 1:
            print(
                '\n********************************** Add event in the relevant category '
                '**************************************')
            add_Event()
            break
        elif adminMenu == 2:
            modify_event()
            break
        elif adminMenu == 3:
            option = 0
            while option < 6:
                print(
                    "\t\t[1] Each category  \n\t\t[2] All Events \n\t\t[3] Customer Registration \n\t\t["
                    "4] Customer Payment")
                print("\t\t[5] Main Menu\n")
                display = int(input('Select Your Option: '))
                if display == 1:
                    print(
                        '\n********************************* DISPLAY ALL RECORDS FOR CATEGORY '
                        '************************************')
                    display_category()
                    break
                elif display == 2:
                    print('\n****************** DISPLAY ALL RECORDS FOR EACH CATEGORY *********************')
                    display_All_Events()
                    break
                elif display == 3:
                    print('\n****************** DISPLAY CUSTOMER REGISTERED  *********************')
                    display_All_Customers()
                    break
                elif display == 4:
                    print('\n****************** DISPLAY CUSTOMER PAYMENT  *********************')
                    customer_payment();
                    break
                elif display == 5:
                    Admin_Menu()
                    break
                else:
                    print("Invalid Input!\nPlease Enter Your Option Again!\n")
            break
        elif adminMenu == 4:
            option = 0
            while option < 4:
                print("\t\t[1] Specific Customer Registration \n\t\t[2] Specific Customer Payment")
                print("\t\t[3] Main Menu\n")
                search = int(input('Select Your Option: '))
                if search == 1:
                    file = open("AllCustomers.txt", "r")
                    booking = file.readlines()
                    count = 0
                    for booking_record in booking:
                        print("[", (count + 1), "]", "Customer Name: " + booking_record.split(",")[0])
                        count += 1
                    file.close()
                    name_ = input("Enter Customer Name to Search: ")
                    print()
                    search_Customer(name_)
                    break
                elif search == 2:
                    file = open("AllBookings.txt", "r")
                    booking = file.readlines()
                    count = 0
                    print("\nAll Booking Details:")
                    for pay_record in booking:
                        print("[", (count + 1), "]" + pay_record.split(",")[0])
                        count += 1
                    file.close()
                    name_ = input("\nEnter Customer Name to Search Payment Details: ")
                    print()
                    search_payment(name_)
                    break
                elif search == 3:
                    Admin_Menu()
                    break
                else:
                    print("Invalid Input!\nPlease Enter Your Option Again!\n")
            break
        elif adminMenu == 5:
            print("Thanks for using our System! Bye! ")
            main()
        else:
            print("Invalid User Input")
        restart = str(input("Do You Wish to Continue(Y/N) 1: ").lower())
        if restart == 'y':
            Admin_Menu()
        else:
            print("Thank You For Using The System")
            main()


# ADMIN PART CODE
# Add Event Information
def add_Event():
    print('\t\t\t\t\t\t  [1] Virtual Concert \n\t\t\t\t\t\t'
          '  [2] Health and Welling Activities \n\t\t\t\t\t\t'
          '  [3] Attract Star Talent \n\t\t\t\t\t\t'
          '  [4] Video Game Challenge \n\t\t\t\t\t\t'
          '  [5] Online Murder Mystery \n\t\t\t\t\t\t'
          '  [6] Exit \n ')

    category = int(input('\tSelect Event Category: '))
    if category == 1:
        event_cat = "Virtual Concert"
        add_Event_Category(event_cat)
    elif category == 2:
        event_cat = "Health and Welling Activities"
        add_Event_Category(event_cat)
    elif category == 3:
        event_cat = "Attract Star Talent"
        add_Event_Category(event_cat)
    elif category == 4:
        event_cat = "Video Game Challenge"
        add_Event_Category(event_cat)
    elif category == 5:
        event_cat = "Online Murder Mystery"
        add_Event_Category(event_cat)
    elif category == 6:
        print("\nExiting!")
        Admin_Menu()


def add_Event_Category(category):
    EventName = input("\n Enter Event Name: ")
    Time = input("\n Enter the Event Time: ")
    Date = input("\n Enter the Event Date: ")
    Location = input("\n Enter the Event Location: ")
    Price = input("\n Enter Event Ticket Price (RM): ")

    f2 = open("AllEvents.txt", "a")
    f2.write(EventName + "," + category + "," + Time + "," + Date + "," + Location + "," + Price + "\n")
    f2.close()

    print("\n" + str(EventName) + "\tEvent have been added Successfully")
    print("\n")

    while True:
        try:
            restart = str(input("Do You Want to Add Another Event (Y/N): ").lower())
            if restart == 'y':
                add_Event_Category(category)
                break
            elif restart == 'n':
                Admin_Menu()
                break
            print("Invalid Value entered")
        except Exception as e:
            print(e)


# Modify Event
def modify_event():
    event_records = open("AllEvents.txt", "r").readlines()

    record = 0
    for even_record in event_records:
        print("[", (record + 1), "]",
              "Event: " + even_record.split(",")[0] + " ,Category: " + even_record.split(",")[1] +
              " ,Time: " + even_record.split(",")[2] + " ,Date: " + even_record.split(",")[3] +
              " ,Location: " + even_record.split(",")[4] + " ,Price: " + even_record.split(",")[5].strip())
        record += 1

    record_num = int(input("\nEnter record number you wanted to edit: "))
    print()
    event_details = event_records[record_num - 1].split(",")

    element = 0
    for record_element in event_details:
        print("[", (element + 1), "]", record_element)
        element += 1
    element_number = int(input("Enter element number you wanted to edit: "))
    print("\nCurrent element value:", event_details[element_number - 1])
    new_element_value = input("Enter new element value: ")
    new_line = ""
    if element_number == 3 and record != record_num:
        new_line = "\n"
    event_details[element_number - 1] = new_element_value + new_line  # assigning new value into selected element
    updated_record = ','.join(event_details)  # takes all items in a list and joins them into one string
    event_records[record_num - 1] = updated_record  # now selected line has updated value

    with open("AllEvents.txt", "w") as file:
        file.writelines(event_records)  # writing the updated student records into text file
        open("AllEvents.txt", "r").close()
    print("\nRecord updated!")

    while True:
        try:
            restart = str(input("Do You Want To Modify Another Event (Y/N): ").lower())
            if restart == 'y':
                modify_event()
                break
            elif restart == 'n':
                Admin_Menu()
                break
            print("Invalid Value entered")
        except Exception as e:
            print(e)


# display category names
def display_category():
    print('\t\t\t\t\t\t  [1] Virtual Concert \n\t\t\t\t\t\t'
          '  [2] Health and Well-being Activities \n\t\t\t\t\t\t'
          '  [3] Attract Star Talent \n\t\t\t\t\t\t'
          '  [4] Video Game Challenge \n\t\t\t\t\t\t'
          '  [5] Speed Networking \n\t\t\t\t\t\t'
          '  [6] Exit \n')

    category = int(input('\tSelect Event Category: '))
    if category == 1:
        event_cat = "Virtual Concert"
        display_Specific_Event(event_cat)
    elif category == 2:
        event_cat = "Health and Welling Activities"
        display_Specific_Event(event_cat)
    elif category == 3:
        event_cat = "Attract Star Talent"
        display_Specific_Event(event_cat)
    elif category == 4:
        event_cat = "Video Game Challenge"
        display_Specific_Event(event_cat)
    elif category == 5:
        event_cat = "Speed Networking"
        display_Specific_Event(event_cat)
    elif category == 6:
        print("\nExiting!")
        Admin_Menu()


def display_All_Events():
    if not fileIsEmpty("AllEvents.txt"):
        car_file = open("AllEvents.txt", "r")
        event_records = car_file.readlines()  # return all lines in the file, as a list
        record = 0
        for event_record in event_records:
            print("[", (record + 1), "]",
                  "Event: " + event_record.split(",")[0] + ", Category: " + event_record.split(",")[1] +
                  " , Time: " + event_record.split(",")[2] + ", Date: " + event_record.split(",")[3] +
                  " , Location: " + event_record.split(",")[4] + " ,Price: " + event_record.split(",")[5].strip())
            record += 1
        car_file.close()
    else:
        print("No Events Are Available!")


def display_All_Customers():
    if not fileIsEmpty("AllCustomers.txt"):
        customer_File = open("AllCustomers.txt", "r")
        event_records = customer_File.readlines()  # return all lines in the file, as a list
        record = 0
        for event_record in event_records:
            print("[", (record + 1), "]",
                  "Name: " + event_record.split(",")[0] + ", Username: " + event_record.split(",")[1] +
                  " , Contact: " + event_record.split(",")[3].strip())
            record += 1
        customer_File.close()
    else:
        print("No Customers Are Available!")


def display_Specific_Event(category):
    file = open("AllEvents.txt", "r")
    event_cat = file.readlines()
    flag = 0
    count = 0
    for st_record in event_cat:
        line = st_record.split(",")
        if category in line:
            flag = 1
            print("[", (count + 1), "]",
                  "Event: " + st_record.split(",")[0] + " ,Category: " + st_record.split(",")[1] +
                  " ,Time: " + st_record.split(",")[2] + " ,Date: " + st_record.split(",")[3] +
                  " ,Location: " + st_record.split(",")[4] + " ,Price: " + st_record.split(",")[5])
        count = +1
    if flag == 0:
        print("No Record Found!")
    file.close()


def customer_Registration():
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    contact = input("Contact: ")
    print("Thank You For Registering with our system!")
    print("Your Login username will be the provided Email")

    f = open("AllCustomers.txt", "a")
    f.write(name + "," + email + "," + password + "," + contact + "\n")
    f.close()
    print("\nSelect An Option From the Given Features to Enjoy")
    option = 0
    while option < 3:
        print("\t\t[1] Login \n\t\t[2] Main Menu")
        opt = int(input('Select Your Optional: '))
        if opt == 1:
            while True:
                try:
                    username = input("Please enter your username: ")
                    password = input("Please enter your password: ")
                    value = customer_Login(username, password)
                    if value:
                        print('Hello !', value[1], " you have logged in successfully.")
                        current_user.append(value[1])
                        Registered_Customer_Main()
                        break
                    print("Invalid Credentials, Please Try Again!")
                except Exception as e:
                    print(e)
                break
        elif opt == 2:
            Non_Registered_Customer_Main()
            break
        else:
            print("Invalid Input!\nPlease Enter Option Again!\n")


def customer_Login(username, password):
    fileRead = open('AllCustomers.txt', 'r')
    while True:
        line = fileRead.readline()
        lineLength = len(line)
        if lineLength == 0:
            break
        lineItem = line.split(",")
        if username == lineItem[1] and password == lineItem[2]:
            return True, lineItem[0]
            break


def price(number, price_per_ticket):
    return number * price_per_ticket


def buy_Ticket(name):
    record_num = int(input("\nEnter record number you wanted to buy: "))
    event_File = open("AllEvents.txt", "r")
    event_records = event_File.readlines()
    event_details = event_records[record_num - 1].split(",")

    id = (event_details[0])
    price_per_ticket = float(event_details[5])  # price of ticket
    my_string = int(input('Enter Number Of Tickets: '))
    print("Total Amount (RM): " + str(float(price(my_string, price_per_ticket))))

    while True:
        try:
            cash = float(input("Confirm Amount of Cash to Pay: "))
            if cash == int(price(my_string, price_per_ticket)):
                print("Thank You For Your Payment!, \nYour Ticket is Confirmed")
                break
            print("Your Due Amount is: " + str(int(price(my_string, price_per_ticket))))
            print("Please Enter Again!")
        except Exception as e:
            print(e)

    # count number of line to auto generate bookings id
    file = open("AllBookings.txt", "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    booking_id = line_count + 1
    booking_File = open("AllBookings.txt", "a")
    booking_File.write(
        "\n" + str(booking_id) + "," + name + "," + str(id) + "," + str(my_string) + "," + str(cash))
    booking_File.close()
    event_File.close()

    while True:
        try:
            restart = str(input("Do You Want To Buy Another Ticket (Y/N): ").lower())
            if restart == 'y':
                buy_Ticket(name)
                break
            elif restart == 'n':
                Registered_Customer_Main()
                break
            print("Invalid Value entered")
        except Exception as e:
            print(e)


def view_Purchase_History(name):
    file = open("AllBookings.txt", "r")
    count = 0
    flag = 0
    transactions = file.readlines()

    for t_record in transactions:
        line = t_record.split(",")
        if name in line:
            flag = 1
            print("[", (count + 1), "]", "Booking ID: " + t_record.split(",")[0] + " ,Event Name: " + t_record.split(",")[2]
                  + " ,Customer: " + t_record.split(",")[1] + " ,No of Tickets: " + t_record.split(",")[3]
                  + " ,Total Payment: " + t_record.split(",")[4])
        count = +1
    if flag == 0:
        print("No Record Found!")


def Registered_Customer_Main():
    regCustomerMenu = 0
    while regCustomerMenu < 5:
        print('\n******************************* REGISTERED CUSTOMER MAIN PAGE *********************************')
        print("\t\t[1] View Details of each category  \n\t\t[2] View Events")
        print("\t\t[3] Buy Tickets \n\t\t[4] View Purchase History \n\t\t[5] Exit")

        regCustomerMenu = int(input('Select Your Option to enjoy the feature: '))

        if regCustomerMenu == 1:
            print(
                '\n********************************* DISPLAY ALL RECORDS FOR CATEGORY '
                '************************************')
            display_category()
            while True:
                try:
                    restart = str(input("Enter 'Y' to go Back to Menu: ").lower())
                    if restart == 'y':
                        Registered_Customer_Main()
                        break
                    print("Invalid Value entered")
                except Exception as e:
                    print(e)
            break
        elif regCustomerMenu == 2:
            print('\n****************** DISPLAY ALL RECORDS FOR EACH CATEGORY *********************')
            display_All_Events()
            while True:
                try:
                    restart = str(input("Enter 'Y' to go Back to Menu: ").lower())
                    if restart == 'y':
                        Registered_Customer_Main()
                        break
                    print("Invalid Value entered")
                except Exception as e:
                    print(e)
            break
        elif regCustomerMenu == 3:
            display_All_Events()
            buy_Ticket(current_user[0])
            break
        elif regCustomerMenu == 4:
            view_Purchase_History(current_user[0])
            while True:
                try:
                    restart = str(input("Enter 'Y' to go Back to Menu: ").lower())
                    if restart == 'y':
                        Registered_Customer_Main()
                        break
                    print("Invalid Value entered")
                except Exception as e:
                    print(e)
            break
        elif regCustomerMenu == 5:
            print("Thank you for using the system!")
            main()
            break
        else:
            print("Invalid User Input")


def Non_Registered_Customer_Main():
    nonRegCustomerMenu = 0
    while nonRegCustomerMenu < 4:
        print('\n******************************* NON REGISTERED CUSTOMER MAIN PAGE *********************************')
        print("\t\t[1] View all events as per category   \n\t\t[2] Register")
        print("\t\t[3] Exit\n")

        nonRegCustomerMenu = int(input('Select Your Optional to enjoy the feature: '))
        if nonRegCustomerMenu == 1:
            print('\n****************** DISPLAY ALL RECORDS FOR EACH CATEGORY *********************')
            display_category()
            while True:
                try:
                    restart = str(input("Enter 'Y' to go Back to Menu: ").lower())
                    if restart == 'y':
                        Non_Registered_Customer_Main()
                        break
                    print("Invalid Value entered")
                except Exception as e:
                    print(e)
            break
        elif nonRegCustomerMenu == 2:
            customer_Registration()
            break
        elif nonRegCustomerMenu == 3:
            print("Thank You For Using The System")
            main()
        else:
            print("Invalid User Input")
        restart = str(input("Do You Wish to Continue(Y/N): ").lower())
        if restart == 'y':
            nonRegCustomerMenu()
        else:
            print("Thank You For Using The System")
            main()


# System Start
main()
