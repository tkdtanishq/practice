import random
bal=random.randint(0,50000)
line='-'*146
print(line)
print("| SIMPLE BANK APPLICATION |")
print(line)
c=random.randint(1000000000000000,9999999999999999)
card=input("Card: Press Enter")
if card == "":
    print("Processing...")
else:
    print("Error:Invalid input")
print(line)
pin=int(input("Enter your 6-digit PIN: "))
pins=str(pin)
if len(pins)!=6:
    print("Error:Invalid input")
    print(line)
else:
    while True:
        menu = input("\nSelect Money Transaction:\n1. Balance Enquiry\t\t2. Money Withdrawal\n3. Money Deposit\t\t4. Exit\nSelect option: ")
        if menu == "1":
            print(f"\nBalance: ₹{bal}")
            print(line)
        elif menu == "2":
            withdraw=int(input("\nAmount: ₹"))
            if 0<withdraw<=bal:
                if withdraw%100==0:
                    den=int(input("\nSelect preferred denomination (₹100 / ₹200 / ₹500):"))
                    note=withdraw//den
                    print(f"Collect the amount: {note} of {den}")
                    bal-=den
                    print(line)
                else:
                    print("Error:Invalid input")
            elif withdraw>bal:
                print("Error:Low Balance")
            else:
                print("Error:Invalid input")
        elif menu == "3":
            deposit=int(input("\nPlease insert notes into the cash acceptor: ₹"))
            print("Counting notes…")
            print(f"Amount detected: ₹{deposit}")
            bal+=deposit
            print(line)
        elif menu == "4":
            rec=input("\nWould you like a receipt?\nYes:y\nNo:n\nChoice: ")
            if rec == 'y':
                print(line)
                print(f"CARD NUMBER: {c}\n\nCURRENT BALANCE: {bal}")
                print(line)
                break
            elif rec == 'n':
                print(line)
                print("Quiting...")
                print(line)
                break
        else:
            print("Error:Invalid input")