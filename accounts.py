import random
from account import Account

class Accounts:
    def __init__(self, database):
        self.db = database
        self.accounts = {}
        self.load_all_accounts()

    def load_all_accounts(self):
        for acc in self.db.data["accounts"]:
            self.accounts[acc] = self.db.data["accounts"][acc]

    def generate_account_number(self):
        return random.randint(1000000000, 9999999999)

    def dump_accounts(self):
        self.db.data["accounts"] = self.accounts
        self.db.dump_data()

    def create_account(self):
        name = input("Enter account name : ")
        contact = int(input("Enter contact number : "))
        email = input("Enter email : ")
        pwd = input("Enter password : ")
        details = {
            "Name": name,
            "Contact": contact,
            "Email": email,
            "Password": pwd,
        }
        while True:
            acc_no = self.generate_account_number()
            if acc_no not in self.accounts:
                details["AccountNumber"] = acc_no
                self.accounts[acc_no] = details
                break
        self.dump_accounts()

    def delete_account(self):
        email = input("Enter email : ")
        pwd = input("Enter password : ")
        for acc in self.accounts:
            cemail = self.accounts[acc]["Email"]
            cpwd = self.accounts[acc]["Password"]
            if email == cemail and pwd == cpwd:
                del self.accounts[acc]
                self.dump_accounts()
                break
        else:
            print("Invalid credentials")

    def manage_account(self):
        email = input("Enter email : ")
        pwd = input("Enter password : ")
        for acc in self.accounts:
            cemail = self.accounts[acc]["Email"]
            cpwd = self.accounts[acc]["Password"]
            if email == cemail and pwd == cpwd:
                account = Account(self.accounts[acc], self.db)
                account.manage()
                break
        else:
            print("Invalid credentials")

    def account_details(self):
        for acc in self.accounts:
            detail = self.accounts[acc]
            acc_no = detail["AccountNumber"]
            email = detail["Email"]
            name = detail["Name"]
            contact = detail["Contact"]
            print(
                f"Account Number : {acc_no} | Email : {email} | Name : {name} | Contact : {contact}"
            )
