
transaction1 = {"sum": 10.2, "date": "2022-01-02", "currency": "gbp"}
transaction2 = {"sum": 22.2, "date": "2022-03-30", "currency": "gbp"}
transaction3 = {"sum": 14.4, "date": "2022-05-02", "currency": "gbp"}
transaction4 = {"sum": 36.2, "date": "2022-02-2", "currency": "gbp"}
transaction5 = {"sum": 93.4, "date": "2022-11-02", "currency": "gbp"}
transactions = [transaction1, transaction2, transaction3]

transactions.append(transaction4)

transactions.append(transaction5)

filtered_transactions = []

for transaction in transactions:
    if transaction['sum'] > 20:
        filtered_transactions.append(transaction)
    
    else:
        print(transaction)
        
# for filtered_transaction in filtered_transactions:
#     print(filtered_transaction)