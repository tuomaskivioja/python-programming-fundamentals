
BALANCE = 10000

transaction_amount = int(input("what is the sum of the transaction? "))

if transaction_amount < 0:
    print("error, transaction mustr be non-zero")
else:
    if transaction_amount <= BALANCE:
        print("approved")
    else:
        print("not approved")