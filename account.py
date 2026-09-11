class Account:
    def __init__(self, details, database):
        self.details = details
        self.db = database
        self.transactions = self.get_transactions_from_db()

    def get_transactions_from_db(self):
        acc_no = self.details["AccountNumber"]
        if acc_no in self.db.data["transactions"]:
            return self.db.data["transactions"][acc_no]
        return []

    def get_previous_balance(self):
        if len(self.transactions) == 0:
            return 0
        else:
            return self.transactions[-1]["CurrentBalance"]

    def add_transaction(self, type, amount):
        pb = self.get_previous_balance()
        cb = pb + amount if type == "deposit" else pb - amount
        t = {
            "Id": len(self.transactions) + 1,
            "Type": type,
            "PreviousBalance": pb,
            "Amount": amount,
            "CurrentBalance": cb,
        }
        self.transactions.append(t)
        acc_no = self.details["AccountNumber"]
        self.db.data["transactions"][acc_no] = self.transactions
        self.db.dump_data()

    def deposit(self):
        amount = float(input("Enter amount : "))
        if amount > 0:
            self.add_transaction("deposit", amount)
        else:
            print("Invalid amount")

    def withdraw(self):
        amount = float(input("Enter amount : "))
        if amount > 0:
            pb = self.get_previous_balance()
            if amount <= pb:
                self.add_transaction("withdraw", amount)
            else:
                print("Insufficient balance")
        else:
            print("Invalid amount")

    def view_balance(self):
        pb = self.get_previous_balance()
        print(f"Current balance : {pb}")

    def view_transactions(self):
        for t in self.transactions:
            print(t)

    def manage(self):
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. View Balance")
            print("4. View Transactions")
            print("5. Logout")
            option = int(input("Enter option : "))
            if option not in range(1, 6):
                print("Invalid option")
            if option == 5:
                break
            if option == 1:
                self.deposit()
            if option == 2:
                self.withdraw()
            if option == 3:
                self.view_balance()
            if option == 4:
                self.view_transactions()
