# BASIC USER INFORMATION MANAGEMENT SYSTEM:
'''
class User:
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone

class UserManagementSystem:
    def __init__(self):
        self.users=[]

    def add_user(self,user):
        self.users.append(user)
        print("User added successfully.")

    def remove_user(self,email):
        for user in self.users:
            if user.email==email:
                self.users.remove(user)
                print("User removed successfully.")
                return
        print("User not found.")

    def search_user(self,email):
        for user in self.users:
            if user.email==email:
                print("Name:", user.name)
                print("Email:", user.email)
                print("Phone:", user.phone)
                return
        print("User not found.")

    def display_all_users(self):
        if not self.users:
            print("No users found.")
            return
        print("All Users:")
        for user in self.users:
            print("Name:", user.name)
            print("Email:", user.email)
            print("Phone:", user.phone)
            print()

def main():
    user_management_system=UserManagementSystem()

    while True:
        print("\nUser Information Management System")
        print("1. Add User")
        print("2. Remove User")
        print("3. Search User")
        print("4. Display All Users")
        print("5. Exit")

        choice=input("Enter your choice: ")

        if choice=="1":
            name=input("Enter name: ")
            email=input("Enter email: ")
            phone=input("Enter phone: ")
            new_user=User(name, email, phone)
            user_management_system.add_user(new_user)

        elif choice=="2":
            email=input("Enter email of the user to remove: ")
            user_management_system.remove_user(email)

        elif choice=="3":
            email=input("Enter email of the user to search: ")
            user_management_system.search_user(email)

        elif choice=="4":
            user_management_system.display_all_users()

        elif choice=="5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__=="__main__":
    main()
'''

# UPDATED CONDITIONS FOR USER INFORMATIONS INPUT:

import re

class User:
    def __init__(self,name,email,phone):
        if len(name)>40:
            raise ValueError("Name should be less than 40 characters.")
        self.name=name

        if not re.match(r"[^@]+@[^@]+\.[^@]+",email):
            raise ValueError("Invalid email format.")
        self.email=email

        if not re.match(r"^\+\d{12}$",phone):
            raise ValueError("Invalid phone format, it should be like this: +country code10-digit number")
        self.phone=phone

class UserManagementSystem:
    def __init__(self):
        self.users=[]

    def add_user(self,user):
        self.users.append(user)
        print("User added successfully.")

    def remove_user(self,email):
        for user in self.users:
            if user.email==email:
                self.users.remove(user)
                print("User removed successfully.")
                return
        print("User not found.")

    def search_user(self,email):
        for user in self.users:
            if user.email==email:
                print("Name:", user.name)
                print("Email:", user.email)
                print("Phone:", user.phone)
                return
        print("User not found.")

    def display_all_users(self):
        if not self.users:
            print("No users found.")
            return
        print("All Users:")
        for user in self.users:
            print("Name:", user.name)
            print("Email:", user.email)
            print("Phone:", user.phone)
            print()

def main():
    user_management_system=UserManagementSystem()

    while True:
        print("\nUser Information Management System")
        print("1. Add User")
        print("2. Remove User")
        print("3. Search User")
        print("4. Display All Users")
        print("5. Exit")

        choice=input("Enter your choice: ")

        if choice=="1":
            name=input("Enter name: ")
            email=input("Enter email: ")
            phone=input("Enter phone (in the format +<country code><10-digit number>): ")
            try:
                new_user=User(name, email, phone)
                user_management_system.add_user(new_user)
            except ValueError as e:
                print("Error:", e)

        elif choice=="2":
            email=input("Enter email of the user to remove: ")
            user_management_system.remove_user(email)

        elif choice=="3":
            email=input("Enter email of the user to search: ")
            user_management_system.search_user(email)

        elif choice=="4":
            user_management_system.display_all_users()

        elif choice=="5":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 5.")

if __name__=="__main__":
    main()
