from accounts import Accounts
from db import Database

db = Database()
accounts = Accounts(database=db)

while True:
    print("1. Create Account.")
    print("2. Delete Account.")
    print("3. Manage Account.")
    print("4. Account Details.")
    print("5. Exit.")
    option = int(input("Enter option : "))
    if option not in range(1, 6):
        print("Invalid option")
    if option == 5:
        break
    if option == 1:
        accounts.create_account()
    if option == 2:
        accounts.delete_account()
    if option == 3:
        accounts.manage_account()
    if option == 4:
        accounts.account_details()
